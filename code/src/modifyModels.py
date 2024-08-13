# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from applyScaling import *


def modifyLinkDimention(linkDimensions, robot):
    ##############################################################################################
    # LINK MODIFICATION
    ##############################################################################################

    # PELVI
    setLinkLength(
        "Pelvis",
        linkDimensions["Pelvis_z"],
        None,
        0,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "Pelvis", linkDimensions["Pelvis_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "Pelvis", linkDimensions["Pelvis_x"], None, None, "X", "BOX", robot
    )  # width

    # LOWER TRUNK
    setLinkLength(
        "LowerTrunk",
        linkDimensions["LowerTrunk_z"],
        None,
        linkDimensions["LowerTrunk_z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "LowerTrunk", linkDimensions["LowerTrunk_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "LowerTrunk", linkDimensions["LowerTrunk_x"], None, None, "X", "BOX", robot
    )  # width

    # UPPER TRUNK
    setLinkLength(
        "UpperTrunk",
        linkDimensions["UpperTrunk_z"],
        None,
        linkDimensions["UpperTrunk_z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "UpperTrunk", linkDimensions["UpperTrunk_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "UpperTrunk", linkDimensions["UpperTrunk_x"], None, None, "X", "BOX", robot
    )  # width

    # RIGHT SHOULDER
    setLinkLength(
        "RightShoulder",
        None,
        linkDimensions["Shoulder_x"] / 2,
        None,
        "Z",
        "CYLINDER",
        robot,
    )
    setLinkLength(
        "RightShoulder",
        linkDimensions["Shoulder_y"],
        None,
        -linkDimensions["Shoulder_y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )  # width

    # LEFT SHOULDER
    setLinkLength(
        "LeftShoulder",
        None,
        linkDimensions["Shoulder_x"] / 2,
        None,
        "Z",
        "CYLINDER",
        robot,
    )
    setLinkLength(
        "LeftShoulder",
        linkDimensions["Shoulder_y"],
        None,
        linkDimensions["Shoulder_y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )  # width

    # NECK
    setLinkLength(
        "Neck",
        linkDimensions["Neck_z"],
        linkDimensions["Neck_x"] / 2,
        linkDimensions["Neck_z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # HEAD
    setLinkLength(
        "Head",
        None,
        linkDimensions["Head_x"] / 2,
        linkDimensions["Head_x"] / 2,
        "Z",
        "SPHERE",
        robot,
    )

    # RIGHT UPPERARM
    setLinkLength(
        "RightUpperArm",
        linkDimensions["UpperArm_y"],
        linkDimensions["UpperArm_x"] / 2,
        -linkDimensions["UpperArm_y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # RIGHT FOREARM
    setLinkLength(
        "RightForeArm",
        linkDimensions["ForeArm_y"],
        linkDimensions["ForeArm_x"] / 2,
        -linkDimensions["ForeArm_y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # RIGHT HAND
    setLinkLength(
        "RightHand",
        linkDimensions["Hand_y"],
        None,
        -linkDimensions["Hand_y"] / 2,
        "Y",
        "BOX",
        robot,
    )
    setLinkLength("RightHand", linkDimensions["Hand_x"], None, None, "X", "BOX", robot)
    setLinkLength("RightHand", linkDimensions["Hand_z"], None, None, "Z", "BOX", robot)

    # LEFT UPPERARM
    setLinkLength(
        "LeftUpperArm",
        linkDimensions["UpperArm_y"],
        linkDimensions["UpperArm_x"] / 2,
        linkDimensions["UpperArm_y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # LEFT FOREARM
    setLinkLength(
        "LeftForeArm",
        linkDimensions["ForeArm_y"],
        linkDimensions["ForeArm_x"] / 2,
        linkDimensions["ForeArm_y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # LEFT HAND
    setLinkLength(
        "LeftHand",
        linkDimensions["Hand_y"],
        None,
        linkDimensions["Hand_y"] / 2,
        "Y",
        "BOX",
        robot,
    )
    setLinkLength("LeftHand", linkDimensions["Hand_x"], None, None, "X", "BOX", robot)
    setLinkLength("LeftHand", linkDimensions["Hand_z"], None, None, "Z", "BOX", robot)

    # RIGHT THIGH
    setLinkLength(
        "RightUpperLeg",
        linkDimensions["UpperLeg_z"],
        linkDimensions["UpperLeg_x"] / 2,
        -linkDimensions["UpperLeg_z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # RIGHT LOWERLEG
    setLinkLength(
        "RightLowerLeg",
        linkDimensions["LowerLeg_z"],
        linkDimensions["LowerLeg_x"] / 2,
        -linkDimensions["LowerLeg_z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # RIGHT FOOT
    setLinkLength(
        "RightFoot",
        linkDimensions["Foot_z"],
        None,
        -linkDimensions["Foot_z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "RightFoot", linkDimensions["Foot_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "RightFoot",
        linkDimensions["Foot_x"],
        None,
        abs((linkDimensions["LowerLeg_x"] / 2) - (linkDimensions["Foot_x"] / 2)),
        "X",
        "BOX",
        robot,
    )

    # RIGHT TOE
    setLinkLength("RightToe", linkDimensions["Toe_z"], None, None, "Z", "BOX", robot)
    setLinkLength(
        "RightToe", linkDimensions["Toe_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "RightToe", linkDimensions["Toe_x"], None, None, "X", "BOX", robot
    )  # deep

    # LEFT THIGH
    setLinkLength(
        "LeftUpperLeg",
        linkDimensions["UpperLeg_z"],
        linkDimensions["UpperLeg_x"] / 2,
        -linkDimensions["UpperLeg_z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # LEFT LOWERLEG
    setLinkLength(
        "LeftLowerLeg",
        linkDimensions["LowerLeg_z"],
        linkDimensions["LowerLeg_x"] / 2,
        -linkDimensions["LowerLeg_z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # LEFT FOOT
    setLinkLength(
        "LeftFoot",
        linkDimensions["Foot_z"],
        None,
        -linkDimensions["Foot_z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "LeftFoot", linkDimensions["Foot_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "LeftFoot",
        linkDimensions["Foot_x"],
        None,
        abs((linkDimensions["LowerLeg_x"] / 2) - (linkDimensions["Foot_x"] / 2)),
        "X",
        "BOX",
        robot,
    )  # deep

    # LEFT TOE
    setLinkLength("LeftToe", linkDimensions["Toe_z"], None, None, "Z", "BOX", robot)
    setLinkLength(
        "LeftToe", linkDimensions["Toe_y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "LeftToe", linkDimensions["Toe_x"], None, None, "X", "BOX", robot
    )  # deep

    return robot


def modifyLinkmass(linkMass, robot):
    ##############################################################################################
    # MASS MODIFICATION
    ##############################################################################################

    setMassPercentage("Pelvis", linkMass["Pelvis_mass"], "Z", robot)
    setMassPercentage("LowerTrunk", linkMass["LowerTrunk_mass"], "Z", robot)
    setMassPercentage("UpperTrunk", linkMass["UpperTrunk_mass"], "Z", robot)

    setMassPercentage("RightShoulder", linkMass["Shoulder_mass"], "Z", robot)
    setMassPercentage("LeftShoulder", linkMass["Shoulder_mass"], "Z", robot)

    setMassPercentage("Neck", linkMass["Neck_mass"], "Z", robot)
    setMassPercentage("Head", linkMass["Head_mass"], "Z", robot)

    setMassPercentage("RightUpperArm", linkMass["UpperArm_mass"], "Z", robot)
    setMassPercentage("LeftUpperArm", linkMass["UpperArm_mass"], "Z", robot)

    setMassPercentage("RightForeArm", linkMass["ForeArm_mass"], "Z", robot)
    setMassPercentage("LeftForeArm", linkMass["ForeArm_mass"], "Z", robot)

    setMassPercentage("RightHand", linkMass["Hand_mass"], "Z", robot)
    setMassPercentage("LeftHand", linkMass["Hand_mass"], "Z", robot)

    setMassPercentage("RightUpperLeg", linkMass["UpperLeg_mass"], "Z", robot)
    setMassPercentage("LeftUpperLeg", linkMass["UpperLeg_mass"], "Z", robot)

    setMassPercentage("RightLowerLeg", linkMass["LowerLeg_mass"], "Z", robot)
    setMassPercentage("LeftLowerLeg", linkMass["LowerLeg_mass"], "Z", robot)

    setMassPercentage("RightFoot", linkMass["Foot_mass"], "Z", robot)
    setMassPercentage("LeftFoot", linkMass["Foot_mass"], "Z", robot)

    setMassPercentage("RightToe", linkMass["Toe_mass"], "Z", robot)
    setMassPercentage("LeftToe", linkMass["Toe_mass"], "Z", robot)

    return robot


def modifyJointPosition(robot, jointPosition):
    ##############################################################################################
    # JOINT MODIFICATION
    ##############################################################################################

    # JOINT PELVI-LowerTrunk
    setJointPosition("jL5S1_rotx", jointPosition["jL5S1_z"], "Z", robot)

    # JOINT LowerTrunk-UpperTrunk
    setJointPosition("jT9T8_rotx", jointPosition["jT9T8_z"], "Z", robot)

    # JOINT UpperTrunk-RightShoulder
    setJointPosition(
        "jC7RightShoulder_rotx", jointPosition["jC7RightShoulder_z"], "Z", robot
    )
    setJointPosition(
        "jC7RightShoulder_rotx", jointPosition["jC7RightShoulder_y"], "Y", robot
    )

    # JOINT UpperTrunk-LeftShoulder
    setJointPosition(
        "jC7LeftShoulder_rotx", jointPosition["jC7LeftShoulder_z"], "Z", robot
    )
    setJointPosition(
        "jC7LeftShoulder_rotx", jointPosition["jC7LeftShoulder_y"], "Y", robot
    )

    # JOINT UPPERTRUNK - NECK
    setJointPosition("jT1C7_rotx", jointPosition["jT1C7_z"], "Z", robot)

    # JOINT NECK - HEAD
    setJointPosition("jC1Head_rotx", jointPosition["jC1Head_z"], "Z", robot)

    # JOINT RIGHT SHOULDER
    setJointPosition(
        "jRightShoulder_rotx", jointPosition["jRightShoulder_y"], "Y", robot
    )

    # JOINT RIGHT ELBOW
    setJointPosition("jRightElbow_roty", jointPosition["jRightElbow_y"], "Y", robot)

    # JOINT RIGHT WRIST
    setJointPosition("jRightWrist_rotx", jointPosition["jRightWrist_y"], "Y", robot)

    # JOINT RIGHT HAND COM
    setJointPosition("jRightHandCOM", jointPosition["jRightHandCOM_y"], "Y", robot)

    # JOINT LEFT SHOULDER
    setJointPosition("jLeftShoulder_rotx", jointPosition["jLeftShoulder_y"], "Y", robot)

    # JOINT LEFT ELBOW
    setJointPosition("jLeftElbow_roty", jointPosition["jLeftElbow_y"], "Y", robot)

    # JOINT LEFT WRIST
    setJointPosition("jLeftWrist_rotx", jointPosition["jLeftWrist_y"], "Y", robot)

    # JOINT LEFT HAND COM
    setJointPosition("jLeftHandCOM", jointPosition["jLeftHandCOM_y"], "Y", robot)

    # JOINT RIGHT HIP
    setJointPosition("jRightHip_rotx", jointPosition["jRightHip_y"], "Y", robot)
    setJointPosition("jRightHip_rotx", jointPosition["jRightHip_z"], "Z", robot)

    # JOINT RIGHT KNEE
    setJointPosition("jRightKnee_roty", jointPosition["jRightKnee_z"], "Z", robot)

    # JOINT RIGHT ANKLE
    setJointPosition("jRightAnkle_rotx", jointPosition["jRightAnkle_z"], "Z", robot)
    setJointPosition("jRightAnkle_rotx", jointPosition["jRightAnkle_x"], "X", robot)

    # JOINT RIGHT TOE
    setJointPosition(
        "jRightBallFoot_roty", jointPosition["jRightBallFoot_x"], "X", robot
    )
    setJointPosition(
        "jRightBallFoot_roty", jointPosition["jRightBallFoot_z"], "Z", robot
    )

    # JOINT RIGHT FT SENSOR
    setJointPosition("jRightBirken_roty", jointPosition["jRightBirken_x"], "X", robot)
    setJointPosition("jRightBirken_roty", jointPosition["jRightBirken_z"], "Z", robot)

    # JOINT LEFT HIP
    setJointPosition("jLeftHip_rotx", jointPosition["jLeftHip_y"], "Y", robot)
    setJointPosition("jLeftHip_rotx", jointPosition["jLeftHip_z"], "Z", robot)

    # JOINT LEFT KNEE
    setJointPosition("jLeftKnee_roty", jointPosition["jLeftKnee_z"], "Z", robot)

    # JOINT LEFT ANKLE
    setJointPosition("jLeftAnkle_rotx", jointPosition["jLeftAnkle_z"], "Z", robot)
    setJointPosition("jLeftAnkle_rotx", jointPosition["jLeftAnkle_x"], "X", robot)

    # JOINT RIGHT TOE
    setJointPosition("jLeftBallFoot_roty", jointPosition["jLeftBallFoot_x"], "X", robot)
    setJointPosition("jLeftBallFoot_roty", jointPosition["jLeftBallFoot_z"], "Z", robot)

    # JOINT RIGHT FT SENSOR
    setJointPosition("jLeftBirken_roty", jointPosition["jLeftBirken_x"], "X", robot)
    setJointPosition("jLeftBirken_roty", jointPosition["jLeftBirken_z"], "Z", robot)

    return robot


def modifyMuscleJointPosition(robot, jointMusclePosition):
    ##############################################################################################
    # MUSCLE FRAME
    ##############################################################################################

    # Biceps
    setJointPosition(
        "jRightBicBrac_RUA", jointMusclePosition["jRightBicBrac_RUA_x"], "X", robot
    )
    setJointPosition(
        "jRightBicBrac_RUA", jointMusclePosition["jRightBicBrac_RUA_z"], "Z", robot
    )
    setJointPosition(
        "jRightBicBrac_RFA", jointMusclePosition["jRightBicBrac_RFA_x"], "X", robot
    )
    setJointPosition(
        "jRightBicBrac_RFA", jointMusclePosition["jRightBicBrac_RFA_z"], "Z", robot
    )
    setJointPosition(
        "jLeftBicBrac_LUA", jointMusclePosition["jLeftBicBrac_LUA_x"], "X", robot
    )
    setJointPosition(
        "jLeftBicBrac_LUA", jointMusclePosition["jLeftBicBrac_LUA_z"], "Z", robot
    )
    setJointPosition(
        "jLeftBicBrac_LFA", jointMusclePosition["jLeftBicBrac_LFA_x"], "X", robot
    )
    setJointPosition(
        "jLeftBicBrac_LFA", jointMusclePosition["jLeftBicBrac_LFA_z"], "Z", robot
    )

    # Triceps
    setJointPosition(
        "jRightTricBrac_RUA", jointMusclePosition["jRightTricBrac_RUA_x"], "X", robot
    )
    setJointPosition(
        "jRightTricBrac_RUA", jointMusclePosition["jRightTricBrac_RUA_z"], "Z", robot
    )
    setJointPosition(
        "jRightTricBrac_RFA", jointMusclePosition["jRightTricBrac_RFA_x"], "X", robot
    )
    setJointPosition(
        "jRightTricBrac_RFA", jointMusclePosition["jRightTricBrac_RFA_z"], "Z", robot
    )
    setJointPosition(
        "jLeftTricBrac_LUA", jointMusclePosition["jLeftTricBrac_LUA_x"], "X", robot
    )
    setJointPosition(
        "jLeftTricBrac_LUA", jointMusclePosition["jLeftTricBrac_LUA_z"], "Z", robot
    )
    setJointPosition(
        "jLeftTricBrac_LFA", jointMusclePosition["jLeftTricBrac_LFA_x"], "X", robot
    )
    setJointPosition(
        "jLeftTricBrac_LFA", jointMusclePosition["jLeftTricBrac_LFA_z"], "Z", robot
    )

    # Flexor carpi radialis
    setJointPosition(
        "jRightFlexCarp_RFA", jointMusclePosition["jRightFlexCarp_RFA_x"], "X", robot
    )
    setJointPosition(
        "jRightFlexCarp_RFA", jointMusclePosition["jRightFlexCarp_RFA_z"], "Z", robot
    )
    setJointPosition(
        "jRightFlexCarp_RH", jointMusclePosition["jRightFlexCarp_RH_x"], "X", robot
    )
    setJointPosition(
        "jRightFlexCarp_RH", jointMusclePosition["jRightFlexCarp_RH_y"], "Y", robot
    )
    setJointPosition(
        "jRightFlexCarp_RH", jointMusclePosition["jRightFlexCarp_RH_z"], "Z", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LFA", jointMusclePosition["jLeftFlexCarp_LFA_x"], "X", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LFA", jointMusclePosition["jLeftFlexCarp_LFA_z"], "Z", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LH", jointMusclePosition["jLeftFlexCarp_LH_x"], "X", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LH", jointMusclePosition["jLeftFlexCarp_LH_y"], "Y", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LH", jointMusclePosition["jLeftFlexCarp_LH_z"], "Z", robot
    )

    # Extensor carpi radialis
    setJointPosition(
        "jRightExtCarp_RFA", jointMusclePosition["jRightExtCarp_RFA_x"], "X", robot
    )
    setJointPosition(
        "jRightExtCarp_RFA", jointMusclePosition["jRightExtCarp_RFA_z"], "Z", robot
    )
    setJointPosition(
        "jRightExtCarp_RH", jointMusclePosition["jRightExtCarp_RH_x"], "X", robot
    )
    setJointPosition(
        "jRightExtCarp_RH", jointMusclePosition["jRightExtCarp_RH_y"], "Y", robot
    )
    setJointPosition(
        "jRightExtCarp_RH", jointMusclePosition["jRightExtCarp_RH_z"], "Z", robot
    )
    setJointPosition(
        "jLeftExtCarp_LFA", jointMusclePosition["jLeftExtCarp_LFA_x"], "X", robot
    )
    setJointPosition(
        "jLeftExtCarp_LFA", jointMusclePosition["jLeftExtCarp_LFA_z"], "Z", robot
    )
    setJointPosition(
        "jLeftExtCarp_LH", jointMusclePosition["jLeftExtCarp_LH_x"], "X", robot
    )
    setJointPosition(
        "jLeftExtCarp_LH", jointMusclePosition["jLeftExtCarp_LH_y"], "Y", robot
    )
    setJointPosition(
        "jLeftExtCarp_LH", jointMusclePosition["jLeftExtCarp_LH_z"], "Z", robot
    )

    # Erector spinae longissimus
    setJointPosition(
        "jRightErSpin_RUT", jointMusclePosition["jRightErSpin_RUT_x"], "X", robot
    )
    setJointPosition(
        "jRightErSpin_RUT", jointMusclePosition["jRightErSpin_RUT_y"], "Y", robot
    )
    setJointPosition(
        "jRightErSpin_RUT", jointMusclePosition["jRightErSpin_RUT_z"], "Z", robot
    )
    setJointPosition(
        "jRightErSpin_RP", jointMusclePosition["jRightErSpin_RP_x"], "X", robot
    )
    setJointPosition(
        "jLeftErSpin_LUT", jointMusclePosition["jLeftErSpin_LUT_x"], "X", robot
    )
    setJointPosition(
        "jLeftErSpin_LUT", jointMusclePosition["jLeftErSpin_LUT_y"], "Y", robot
    )
    setJointPosition(
        "jLeftErSpin_LUT", jointMusclePosition["jLeftErSpin_LUT_z"], "Z", robot
    )
    setJointPosition(
        "jLeftErSpin_LP", jointMusclePosition["jLeftErSpin_LP_x"], "X", robot
    )

    # Rectus abdominis
    setJointPosition(
        "jRightRecAbd_RUT", jointMusclePosition["jRightRecAbd_RUT_x"], "X", robot
    )
    setJointPosition(
        "jRightRecAbd_RUT", jointMusclePosition["jRightRecAbd_RUT_y"], "Y", robot
    )
    setJointPosition(
        "jRightRecAbd_RP", jointMusclePosition["jRightRecAbd_RP_x"], "X", robot
    )
    setJointPosition(
        "jLeftRecAbd_LUT", jointMusclePosition["jLeftRecAbd_LUT_x"], "X", robot
    )
    setJointPosition(
        "jLeftRecAbd_LUT", jointMusclePosition["jLeftRecAbd_LUT_y"], "Y", robot
    )

    # Biceps femoris
    setJointPosition(
        "jRightBicFem_RUL", jointMusclePosition["jRightBicFem_RUL_x"], "X", robot
    )
    setJointPosition(
        "jRightBicFem_RUL", jointMusclePosition["jRightBicFem_RUL_y"], "Y", robot
    )
    setJointPosition(
        "jRightBicFem_RLL", jointMusclePosition["jRightBicFem_RLL_x"], "X", robot
    )
    setJointPosition(
        "jRightBicFem_RLL", jointMusclePosition["jRightBicFem_RLL_y"], "Y", robot
    )
    setJointPosition(
        "jLeftBicFem_LUL", jointMusclePosition["jLeftBicFem_LUL_x"], "X", robot
    )
    setJointPosition(
        "jLeftBicFem_LUL", jointMusclePosition["jLeftBicFem_LUL_y"], "Y", robot
    )
    setJointPosition(
        "jLeftBicFem_LLL", jointMusclePosition["jLeftBicFem_LLL_x"], "X", robot
    )
    setJointPosition(
        "jLeftBicFem_LLL", jointMusclePosition["jLeftBicFem_LLL_y"], "Y", robot
    )

    # Rectus femoris
    setJointPosition(
        "jRightRecFem_RP", jointMusclePosition["jRightRecFem_RP_x"], "X", robot
    )
    setJointPosition(
        "jRightRecFem_RP", jointMusclePosition["jRightRecFem_RP_y"], "Y", robot
    )
    setJointPosition(
        "jRightRecFem_RP", jointMusclePosition["jRightRecFem_RP_z"], "Z", robot
    )
    setJointPosition(
        "jRightRecFem_RLL", jointMusclePosition["jRightRecFem_RLL_x"], "X", robot
    )
    setJointPosition(
        "jRightRecFem_RLL", jointMusclePosition["jRightRecFem_RLL_y"], "Y", robot
    )
    setJointPosition(
        "jLeftRecFem_LP", jointMusclePosition["jLeftRecFem_LP_x"], "X", robot
    )
    setJointPosition(
        "jLeftRecFem_LP", jointMusclePosition["jLeftRecFem_LP_y"], "Y", robot
    )
    setJointPosition(
        "jLeftRecFem_LP", jointMusclePosition["jLeftRecFem_LP_z"], "Z", robot
    )
    setJointPosition(
        "jLeftRecFem_LLL", jointMusclePosition["jLeftRecFem_LLL_x"], "X", robot
    )
    setJointPosition(
        "jLeftRecFem_LLL", jointMusclePosition["jLeftRecFem_LLL_y"], "Y", robot
    )

    # Tibialis anterior
    setJointPosition(
        "jRightTibAnt_RLL", jointMusclePosition["jRightTibAnt_RLL_x"], "X", robot
    )
    setJointPosition(
        "jRightTibAnt_RLL", jointMusclePosition["jRightTibAnt_RLL_y"], "Y", robot
    )
    setJointPosition(
        "jRightTibAnt_RF", jointMusclePosition["jRightTibAnt_RF_x"], "X", robot
    )
    setJointPosition(
        "jRightTibAnt_RF", jointMusclePosition["jRightTibAnt_RF_y"], "Y", robot
    )
    setJointPosition(
        "jLeftTibAnt_LLL", jointMusclePosition["jLeftTibAnt_LLL_x"], "X", robot
    )
    setJointPosition(
        "jLeftTibAnt_LLL", jointMusclePosition["jLeftTibAnt_LLL_y"], "Y", robot
    )
    setJointPosition(
        "jLeftTibAnt_LF", jointMusclePosition["jLeftTibAnt_LF_x"], "X", robot
    )
    setJointPosition(
        "jLeftTibAnt_LF", jointMusclePosition["jLeftTibAnt_LF_y"], "Y", robot
    )

    # Gastrocnemius medialis
    setJointPosition(
        "jRightGasMed_RUL", jointMusclePosition["jRightGasMed_RUL_x"], "X", robot
    )
    setJointPosition(
        "jRightGasMed_RUL", jointMusclePosition["jRightGasMed_RUL_y"], "Y", robot
    )
    setJointPosition(
        "jRightGasMed_RUL", jointMusclePosition["jRightGasMed_RUL_z"], "Z", robot
    )
    setJointPosition(
        "jRightGasMed_RF", jointMusclePosition["jRightGasMed_RF_z"], "Z", robot
    )
    setJointPosition(
        "jRightGasMed_RF", jointMusclePosition["jRightGasMed_RF_x"], "X", robot
    )
    setJointPosition(
        "jLeftGasMed_LUL", jointMusclePosition["jLeftGasMed_LUL_x"], "X", robot
    )
    setJointPosition(
        "jLeftGasMed_LUL", jointMusclePosition["jLeftGasMed_LUL_y"], "Y", robot
    )
    setJointPosition(
        "jLeftGasMed_LUL", jointMusclePosition["jLeftGasMed_LUL_z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasMed_LF", jointMusclePosition["jLeftGasMed_LF_z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasMed_LF", jointMusclePosition["jLeftGasMed_LF_x"], "X", robot
    )

    # Gastrocnemius lateralis
    setJointPosition(
        "jRightGasLat_RUL", jointMusclePosition["jRightGasLat_RUL_x"], "X", robot
    )
    setJointPosition(
        "jRightGasLat_RUL", jointMusclePosition["jRightGasLat_RUL_y"], "Y", robot
    )
    setJointPosition(
        "jRightGasLat_RUL", jointMusclePosition["jRightGasLat_RUL_z"], "Z", robot
    )
    setJointPosition(
        "jRightGasLat_RF", jointMusclePosition["jRightGasLat_RF_z"], "Z", robot
    )
    setJointPosition(
        "jRightGasLat_RF", jointMusclePosition["jRightGasLat_RF_x"], "X", robot
    )
    setJointPosition(
        "jLeftGasLat_LUL", jointMusclePosition["jLeftGasLat_LUL_x"], "X", robot
    )
    setJointPosition(
        "jLeftGasLat_LUL", jointMusclePosition["jLeftGasLat_LUL_y"], "Y", robot
    )
    setJointPosition(
        "jLeftGasLat_LUL", jointMusclePosition["jLeftGasLat_LUL_z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasLat_LF", jointMusclePosition["jLeftGasLat_LF_z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasLat_LF", jointMusclePosition["jLeftGasLat_LF_x"], "X", robot
    )

    return robot
