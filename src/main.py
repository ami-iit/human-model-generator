# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from modifyModels import *
from scaleModels import *
from modelControl import *
from checkModel import *
import idyntree.bindings as iDynTree
from urdfModifiers.utils import *
from generateSyntheticData import *
import os
import sys


""" 
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| PARAMETERS | THE FUNCTION OF PARAMETERS                                                                                                                  |  
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| H          | height of the subject to be modelled.                                                                                                       |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| m          | mass of the subject to be modelled.                                                                                                         |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Model      | type of model to be used based on different theoretical approaches: `DeLeva` (see De Leva, et. al 1996) or `Dumas` (see Dumas, et. al 2007) |   
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| FileName   | name of the file with which the .urdf model will be saved.                                                                                  |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Control    | generates a table with estimated anthropometric measurements for each body segment: `On` or `Off`.                                          |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
"""


MODEL_TYPE = "Dumas"  # "DeLeva" or "Dumas"

""" OPTIONS"""

OPT_CHECK_CONSISTENCY_MODEL = True

OPT_TYPE_MOVEMENT = "random"  # "physio" or "random"
OPT_VISUALIZZATION_MOVEMENT = True

""" ANTHROPOMETRIC MEASUREMENTS"""

H = 1.85
m = 103

# some neck,trunk,arm and leg dimensions
linkDimensions = {
    "Neck_x": 0.115,
    "UpperTrunk_x": 0.235,
    "LowerTrunk_x": 0.235,
    "Pelvis_x": 0.235,
    "Shoulder_x": 0.075,
    "UpperArm_x": 0.075,
    "ForeArm_x": 0.07,
    "Hand_z": 0.035,
    "Hand_x": 0.08,
    "UpperLeg_x": 0.155,
    "LowerLeg_x": 0.125,
}

""" COSTANT"""

URDF_MAIN_FOLDER = "models"
URDF_TEMPLATE_FILE_FOLDER = "humanModelTemplate"
URDF_TEMPLATE_FILE_NAME = "humanModelTemplate.urdf"
URDF_TEMPLATE_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    URDF_MAIN_FOLDER,
    URDF_TEMPLATE_FILE_FOLDER,
    URDF_TEMPLATE_FILE_NAME,
)
URDF_FILE_FOLDER = "humanModels"
# URDF_FILE_NAME = "Model.urdf"
URDF_FILE_NAME = input("\n[INPUT] Insert the model name: ") + ".urdf"


os.makedirs(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        URDF_MAIN_FOLDER,
        URDF_FILE_FOLDER,
    ),
    exist_ok=True,
)

URDF_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
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
linkDimensions = scaleLink(H, MODEL_TYPE, linkDimensions)
robot = modifyLinkDimention(linkDimensions, robot)
#################################################################
# MASS
#################################################################
linkMass = scaleMass(m, MODEL_TYPE)
robot = modifyLinkmass(linkMass, robot)
#################################################################
# JOINT
#################################################################
jointPosition = scaleJoint(linkDimensions)
robot = modifyJointPosition(robot, jointPosition)
#################################################################
# MUSCLE FRAMES
#################################################################
jointMusclePosition = scaleMuscleJoint(linkDimensions)
robot = modifyMuscleJointPosition(robot, jointMusclePosition)

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
        )
    ),
    "Kg",
)
print(
    "[INFO] Model height:",
    str(
        linkDimensions["Head_x"]
        + linkDimensions["Neck_z"]
        + linkDimensions["UpperTrunk_z"]
        + linkDimensions["LowerTrunk_z"]
        + linkDimensions["Pelvis_z"]
        + linkDimensions["UpperLeg_z"]
        + linkDimensions["LowerLeg_z"]
        + linkDimensions["Foot_z"]
    ),
    "m",
)

#################################################################
# CHECK CONSISTENCY MODEL
#################################################################
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


#################################################################
# PHYSICALLY CONSISTENCE TESTS
#################################################################
Links = linkPhysicallyConsistence(dynComp)

print("[INFO] Model links:  " + str(len(Links)))
print("[INFO] Model joints: " + str(NrOfJoints))
print("[INFO] Model DoFs:   " + str(ndofs))

#################################################################
# GENERATION OF MOVEMENT
#################################################################
print("\n[CHECK] PHYSICAL CONSISTENCY TESTS START")
if OPT_TYPE_MOVEMENT == "physio":
    generated_Movement = genSynthPhysMov(JOINTLIST, ndofs)
elif OPT_TYPE_MOVEMENT == "random":
    generated_Movement = genSynthRandMov(ndofs, -360, 360, 3, 100)
else:
    print(
        "[ERROR] You did not choose a valid movement type. Consistency check not performed."
    )
    sys.exit(1)


print("\n       1. Synthetic motion dataset generated \u2713")


s = generated_Movement
ds = [0] * ndofs
gravity = [0.0, 0.0, -9.81]
quaternion_idyn = iDynTree.Vector4([1, 0, 0, 0])
G_T_b_rot = iDynTree.Rotation()
G_T_b_rot.fromQuaternion(quaternion_idyn)
G_T_b_pos = iDynTree.Position([0, 0, 1])
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


#################################################################
# VISUALIZZATION MODEL
#################################################################
if OPT_VISUALIZZATION_MOVEMENT:
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
    viz.modelViz("ModelVisualizer").setPositions(G_T_base, s[:, 0])
    num_rows, num_cols = s.shape
    indx = 1
    while indx < num_cols:
        viz.modelViz("ModelVisualizer").setPositions(G_T_base, s[:, indx])
        viz.draw()
        indx += 1
        if indx >= num_cols:
            viz.close()

print("\n[CHECK] PHYSICAL CONSISTENCY TESTS COMPLETED")

measurementControl(linkMass, linkDimensions)
