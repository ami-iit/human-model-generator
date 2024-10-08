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

import os
import sys
import idyntree.bindings as iDynTree
from urdfModifiers.utils import *

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src import *
from config import *


""" COSTANT"""

URDF_MAIN_FOLDER = "models"
URDF_TEMPLATE_FILE_FOLDER = "humanModelTemplate"
URDF_TEMPLATE_FILE_NAME = "humanModelTemplate.urdf"
URDF_MESHES_FILE_FOLDER = "meshes"

URDF_TEMPLATE_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    URDF_MAIN_FOLDER,
    URDF_TEMPLATE_FILE_FOLDER,
    URDF_TEMPLATE_FILE_NAME,
)

URDF_MESHES_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    URDF_MAIN_FOLDER,
    URDF_TEMPLATE_FILE_FOLDER,
    URDF_MESHES_FILE_FOLDER,
)

URDF_FILE_FOLDER = "humanModels"
URDF_FILE_NAME = input("\n[INPUT] Insert the model name: ") + ".urdf"


os.makedirs(
    os.path.join(
        os.path.dirname(__file__),
        URDF_MAIN_FOLDER,
        URDF_FILE_FOLDER,
    ),
    exist_ok=True,
)

URDF_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    URDF_MAIN_FOLDER,
    URDF_FILE_FOLDER,
    URDF_FILE_NAME,
)


dummy_file = "no_gazebo_plugins.urdf"

# Extract the <gazebo> tags from the urdf, as they collide with the library
robot, gazebo_plugin_text = utils.load_robot_and_gazebo_plugins(
    URDF_TEMPLATE_FILE_PATH, dummy_file
)


#################################################################
# LINK
#################################################################
linkDimensions = scaleLink(H, linkDimensions)
robot = modifyLinkDimention(linkDimensions, robot)
#################################################################
# MASS
#################################################################
linkMass = scaleMass(m, linkMass)
robot = modifyLinkmass(linkMass, robot)
#################################################################
# JOINT
#################################################################
jointPosition = scaleJoint(linkDimensions, jointPosition)
robot = modifyJointPosition(jointPosition, robot)
#################################################################
# MUSCLE FRAMES
#################################################################
jointMusclePosition = scaleMuscleJoint(linkDimensions, jointMusclePosition)
robot = modifyMuscleJointPosition(jointMusclePosition, robot)
#################################################################
# ADD MESH
#################################################################
scalingParam = getScalingParam(linkDimensions, linkDimensions_norm)
scalingParamMesh = createScalingParamMesh(
    scalingParam, meshLinksName, mesh_name_mapping
)
robot = updateRobotWithMeshAndMuscles(
    scalingParamMesh,
    map_link_to_muscles,
    URDF_MESHES_FILE_PATH,
    robot,
    OPT_COLOR_LINK_MESH,
    OPT_COLOR_MUSCLE_MESH,
)

# Write URDF to a new file, also adding back the previously removed <gazebo> tags
utils.write_urdf_to_file(robot, URDF_FILE_PATH, gazebo_plugin_text)

print("[OUTPUT] Model successfully created. \u2713")
print("[OUTPUT] Model successfully saved. \u2713")
print(
    "\n[INFO] Model mass:  ",
    str(
        round(
            linkMass["Head_mass"]
            + linkMass["Neck_mass"]
            + linkMass["UpperTrunk_mass"]
            + (linkMass["Shoulder_mass"] * 2)
            + linkMass["LowerTrunk_mass"]
            + linkMass["Pelvis_mass"]
            + (linkMass["UpperArm_mass"] * 2)
            + (linkMass["ForeArm_mass"] * 2)
            + (linkMass["Hand_mass"] * 2)
            + (linkMass["UpperLeg_mass"] * 2)
            + (linkMass["LowerLeg_mass"] * 2)
            + (linkMass["Foot_mass"] * 2)
            + (linkMass["Toe_mass"] * 2),
            2,
        )
    ),
    "Kg",
)

print(
    "[INFO] Model height:",
    str(
        round(
            linkDimensions["Head"]["Z"]
            + linkDimensions["Neck"]["Z"]
            + linkDimensions["UpperTrunk"]["Z"]
            + linkDimensions["LowerTrunk"]["Z"]
            + linkDimensions["Pelvis"]["Z"]
            + linkDimensions["UpperLeg"]["Z"]
            + linkDimensions["LowerLeg"]["Z"]
            + linkDimensions["Foot"]["Z"],
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
# Possibility of inserting a reduced list of joints
JOINTLIST = []
mdlLoader.loadModelFromFile(URDF_FILE_PATH)
dynComp.loadRobotModel(mdlLoader.model())
ndofs = dynComp.model().getNrOfDOFs()
NrOfJoints = dynComp.model().getNrOfJoints()
for indxJoint in range(NrOfJoints):
    JOINTLIST.append(dynComp.model().getJointName(indxJoint))

Links = linkPhysicallyConsistence(dynComp)

#################################################################
# PHYSICALLY CONSISTENCE TESTS
#################################################################

if OPT_CHECK_CONSISTENCY_MODEL:
    print("\n[CHECK] PHYSICAL CONSISTENCY TESTS START")

    generated_Movement = genSynthRandMov(ndofs, -360, 360, 3, 100)

    print("\n       1. Synthetic motion dataset generated \u2713")

    s = generated_Movement
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
    if OPT_VISUALIZZATION_MODEL:
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
        # frames = viz.frames()
        cam = viz.camera()
        cam.setPosition(iDynTree.Position(2, 1, 2.5))
        viz.camera().animator().enableMouseControl(True)

        viz.addModel(mdlLoader.model(), "ModelVisualizer")
        s = [0] * ndofs
        ds = [0] * ndofs
        viz.modelViz("ModelVisualizer").setPositions(G_T_base, s)

        while viz.run():
            viz.draw()


if OPT_VISUALIZZATION_MEASUREOFCONTROL:
    measurementControl(linkMass, linkDimensions)
