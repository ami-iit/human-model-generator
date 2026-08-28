# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

"""
|:-----------------------------:|
|                               |
|    HUMAN MODEL GENERATOR      |
|                               |
|:-----------------------------:|
"""

import copy
import dataclasses
import importlib.resources
import os

import idyntree.bindings as iDynTree
import numpy as np
from urdfModifiers.utils import *

from .config import Config, DEFAULT_CONFIG
from .checkModel import isPositiveDefinite, linkPhysicallyConsistence
from .generateSyntheticData import genSynthRandMov
from .modelControl import measurementControl
from .modifyMeshModels import (
    createScalingParamMesh,
    getScalingParam,
    updateRobotWithBones,
    updateRobotWithMesh,
    updateRobotWithMuscles,
)
from .modifyModels import (
    modifyJointPosition,
    modifyLinkDimension,
    modifyLinkmass,
    modifyMuscleJointPosition,
)
from .scaleModels import scaleJoint, scaleLink, scaleMass, scaleMuscleJoint
from . import (
    jointMusclePosition,
    jointPosition,
    linkDimensions,
    linkDimensions_norm,
    linkMass,
    map_link_to_muscles,
    map_link_to_spinal_cord,
    mesh_name_mapping,
    meshLinksName,
)

URDF_TEMPLATE_FILE_FOLDER = "humanModelTemplate"
URDF_TEMPLATE_FILE_NAME = "humanModelTemplate.urdf"
URDF_MESHES_FILE_FOLDER = "meshes"


def generate_model(
    model_name: str,
    config: Config = DEFAULT_CONFIG,
    output_dir: str | None = None,
    link_dimension_overrides: dict | None = None,
    mesh_package_prefix: str | None = None,
    **overrides,
) -> str:
    """Generate a scaled human URDF model; returns the path of the written file.

    Pure library entry point: no interactive prompts, no filesystem-based config discovery.
    `overrides` are applied on top of `config` (see `dataclasses.replace`), e.g. H=1.8, m=75.
    `link_dimension_overrides` optionally overrides individual link X/Y/Z anthropometric dimensions,
    e.g. {"Neck": {"X": 0.32}}.
    `mesh_package_prefix`, if set, replaces the local meshes folder with `<prefix>/meshes`
    in the mesh filenames written to the URDF (e.g. "package://human-gazebo/meshes").
    """
    if overrides:
        config = dataclasses.replace(config, **overrides)

    models_dir = importlib.resources.files("humanmodelgenerator") / "models"
    urdf_template_file_path = str(
        models_dir / URDF_TEMPLATE_FILE_FOLDER / URDF_TEMPLATE_FILE_NAME
    )
    if mesh_package_prefix:
        urdf_meshes_file_path = f"{mesh_package_prefix}/{URDF_MESHES_FILE_FOLDER}"
    else:
        urdf_meshes_file_path = str(models_dir / URDF_TEMPLATE_FILE_FOLDER / URDF_MESHES_FILE_FOLDER)

    urdf_file_name = model_name + ".urdf"

    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), "humanModels")
    os.makedirs(output_dir, exist_ok=True)
    urdf_file_path = os.path.join(output_dir, urdf_file_name)

    dummy_file = "no_gazebo_plugins.urdf"

    # Extract the <gazebo> tags from the urdf, as they collide with the library
    robot, gazebo_plugin_text = utils.load_robot_and_gazebo_plugins(
        urdf_template_file_path, dummy_file
    )

    # deep-copy shared package-level dicts so repeated generate_model() calls don't accumulate mutations
    #################################################################
    # LINK
    #################################################################
    local_link_dimensions = copy.deepcopy(linkDimensions)
    if link_dimension_overrides:
        for link_name, axes in link_dimension_overrides.items():
            local_link_dimensions[link_name].update(axes)
    local_link_dimensions = scaleLink(config.H, local_link_dimensions)
    robot = modifyLinkDimension(local_link_dimensions, robot)
    #################################################################
    # MASS
    #################################################################
    local_link_mass = scaleMass(config.m, copy.deepcopy(linkMass))
    robot = modifyLinkmass(local_link_mass, robot)
    #################################################################
    # JOINT
    #################################################################
    local_joint_position = scaleJoint(local_link_dimensions, copy.deepcopy(jointPosition))
    robot = modifyJointPosition(local_joint_position, robot)
    #################################################################
    # MUSCLE FRAMES
    #################################################################
    local_joint_muscle_position = scaleMuscleJoint(local_link_dimensions, copy.deepcopy(jointMusclePosition))
    robot = modifyMuscleJointPosition(local_joint_muscle_position, robot)
    #################################################################
    # ADD MESH
    #################################################################
    scaling_param = getScalingParam(local_link_dimensions, linkDimensions_norm)
    scaling_param_mesh = createScalingParamMesh(scaling_param, meshLinksName, mesh_name_mapping)

    if config.OPT_VISUALIZATION_MESH:
        robot = updateRobotWithMesh(
            scaling_param_mesh,
            urdf_meshes_file_path,
            robot,
            config.OPT_COLOR_LINK_MESH,
        )

        if config.OPT_VISUALIZATION_MUSCLES:
            robot = updateRobotWithMuscles(
                scaling_param_mesh,
                map_link_to_muscles,
                urdf_meshes_file_path,
                robot,
                config.OPT_COLOR_MUSCLE_MESH,
            )

    if config.OPT_VISUALIZATION_SPINALCORD:
        robot = updateRobotWithBones(
            scaling_param_mesh,
            map_link_to_spinal_cord,
            urdf_meshes_file_path,
            robot,
            config.OPT_COLOR_SPINALCORD_MESH,
        )

    # Write URDF to a new file, also adding back the previously removed <gazebo> tags
    utils.write_urdf_to_file(robot, urdf_file_path, gazebo_plugin_text)

    print("[OUTPUT] Model successfully created. \u2713")
    print("[OUTPUT] Model successfully saved. \u2713")
    print(
        "\n[INFO] Model mass:  ",
        str(
            round(
                local_link_mass["Head_mass"]
                + local_link_mass["Neck_mass"]
                + local_link_mass["T8_mass"]
                + local_link_mass["T12_mass"]
                + local_link_mass["L3_mass"]
                + local_link_mass["L5_mass"]
                + (local_link_mass["Shoulder_mass"] * 2)
                + local_link_mass["Pelvis_mass"]
                + (local_link_mass["UpperArm_mass"] * 2)
                + (local_link_mass["ForeArm_mass"] * 2)
                + (local_link_mass["Hand_mass"] * 2)
                + (local_link_mass["UpperLeg_mass"] * 2)
                + (local_link_mass["LowerLeg_mass"] * 2)
                + (local_link_mass["Foot_mass"] * 2)
                + (local_link_mass["Toe_mass"] * 2)
                + (local_link_mass["Heel_mass"] * 2),
                2,
            )
        ),
        "Kg",
    )

    print(
        "[INFO] Model height:",
        str(
            round(
                local_link_dimensions["Head"]["Z"]
                + local_link_dimensions["Neck"]["Z"]
                + local_link_dimensions["T8"]["Z"]
                + local_link_dimensions["T12"]["Z"]
                + local_link_dimensions["L3"]["Z"]
                + local_link_dimensions["L5"]["Z"]
                + local_link_dimensions["Pelvis"]["Z"]
                + local_link_dimensions["UpperLeg"]["Z"]
                + local_link_dimensions["LowerLeg"]["Z"]
                + local_link_dimensions["Foot"]["Z"],
                2,
            )
        ),
        "m",
    )

    #################################################################
    # LOAD THE MODEL
    #################################################################

    dynComp = iDynTree.KinDynComputations()
    mdlLoader = iDynTree.ModelLoader()
    mdlLoader.loadModelFromFile(urdf_file_path)
    dynComp.loadRobotModel(mdlLoader.model())
    ndofs = dynComp.model().getNrOfDOFs()

    linkPhysicallyConsistence(dynComp)

    #################################################################
    # PHYSICALLY CONSISTENCE TESTS
    #################################################################

    if config.OPT_CHECK_CONSISTENCY_MODEL:
        print("\n[CHECK] PHYSICAL CONSISTENCY TESTS START")

        generated_movement = genSynthRandMov(ndofs, -360, 360, 3, 100)

        print("\n       1. Synthetic motion dataset generated \u2713")

        s = generated_movement
        ds = [0] * ndofs
        gravity = [0.0, 0.0, -9.81]
        quaternion_idyn = iDynTree.Vector4([1, 0, 0, 0])
        G_T_b_rot = iDynTree.Rotation()
        G_T_b_rot.fromQuaternion(quaternion_idyn)
        G_T_b_pos = iDynTree.Position([0, 0, 0])
        G_T_base = iDynTree.Transform(G_T_b_rot, G_T_b_pos)
        base_vel = iDynTree.Twist([0, 0, 0, 0, 0, 0])

        dynComp.setFloatingBase("Pelvis")
        mass_mx = iDynTree.MatrixDynSize()

        num_rows, num_cols = s.shape

        indx = 1
        indxPos = 0
        threshold = -1e-5
        positivity = []

        while indx < num_cols:
            dynComp.setRobotState(G_T_base, s[:, indx], base_vel, ds, gravity)
            dynComp.getFreeFloatingMassMatrix(mass_mx)
            BooleanCheck, mass_mxNumpy, eig = isPositiveDefinite(mass_mx)
            positivity.append(BooleanCheck)
            if not positivity[indxPos]:
                if np.min(eig) > threshold:
                    print(
                        f"\n[WARRING] The mass matrix contains an eigenvalue that is negative but greater than {threshold}, for the {indx}th samples."
                    )
                else:
                    print(
                        f"\n[WARRING] The mass matrix is not positive definite for the {indx}th samples."
                    )
            indx += 1
            indxPos += 1

        if np.all(positivity):
            print(
                "\n       2. Mass matrix remains positive throughout the entire dataset \u2713 "
            )
        print("\n[CHECK] PHYSICAL CONSISTENCY TESTS COMPLETED")

    #################################################################
    # VISUALIZZATION MODEL
    #################################################################
    if config.OPT_VISUALIZZATION_MODEL:
        print("\n[INFO] Visualization :\n")
        viz = iDynTree.Visualizer()
        vizOpt = iDynTree.VisualizerOptions()
        vizOpt.winWidth = 1500
        vizOpt.winHeight = 1000
        viz.init(vizOpt)

        env = viz.enviroment()
        env.setElementVisibility("floor_grid", True)
        env.setElementVisibility("world_frame", True)
        viz.setColorPalette("meshcat")
        cam = viz.camera()
        cam.setPosition(iDynTree.Position(2, 1, 2.5))
        viz.camera().animator().enableMouseControl(True)

        viz.addModel(mdlLoader.model(), "ModelVisualizer")

        gravity = [0.0, 0.0, -9.81]
        quaternion_idyn = iDynTree.Vector4([1, 0, 0, 0])
        G_T_b_rot = iDynTree.Rotation()
        G_T_b_rot.fromQuaternion(quaternion_idyn)
        G_T_b_pos = iDynTree.Position([0, 0, 0])
        G_T_base = iDynTree.Transform(G_T_b_rot, G_T_b_pos)
        s = [0] * ndofs

        viz.modelViz("ModelVisualizer").setPositions(G_T_base, s)

        while viz.run():
            viz.draw()

    if config.OPT_VISUALIZZATION_MEASUREOFCONTROL:
        measurementControl(local_link_mass, local_link_dimensions)

    return urdf_file_path
