# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from applyScaling import *


def modifyLinkDimention(linkDimensions, robot):
    ##############################################################################################
    # LINK MODIFICATION
    ##############################################################################################

    # PELVIS
    setLinkLength("Pelvis", linkDimensions["Pelvis"]["Z"], None, 0, "Z", "BOX", robot)
    setLinkLength(
        "Pelvis", linkDimensions["Pelvis"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "Pelvis", linkDimensions["Pelvis"]["X"], None, None, "X", "BOX", robot
    )  # width

    # LOWER TRUNK
    setLinkLength(
        "LowerTrunk",
        linkDimensions["LowerTrunk"]["Z"],
        None,
        linkDimensions["LowerTrunk"]["Z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "LowerTrunk", linkDimensions["LowerTrunk"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "LowerTrunk", linkDimensions["LowerTrunk"]["X"], None, None, "X", "BOX", robot
    )  # width

    # UPPER TRUNK
    setLinkLength(
        "UpperTrunk",
        linkDimensions["UpperTrunk"]["Z"],
        None,
        linkDimensions["UpperTrunk"]["Z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "UpperTrunk", linkDimensions["UpperTrunk"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "UpperTrunk", linkDimensions["UpperTrunk"]["X"], None, None, "X", "BOX", robot
    )  # width

    # RIGHT SHOULDER
    setLinkLength(
        "RightShoulder",
        None,
        linkDimensions["Shoulder"]["X"] / 2,
        None,
        "Z",
        "CYLINDER",
        robot,
    )
    setLinkLength(
        "RightShoulder",
        linkDimensions["Shoulder"]["Y"],
        None,
        -linkDimensions["Shoulder"]["Y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )  # width

    # LEFT SHOULDER
    setLinkLength(
        "LeftShoulder",
        None,
        linkDimensions["Shoulder"]["X"] / 2,
        None,
        "Z",
        "CYLINDER",
        robot,
    )
    setLinkLength(
        "LeftShoulder",
        linkDimensions["Shoulder"]["Y"],
        None,
        linkDimensions["Shoulder"]["Y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )  # width

    # NECK
    setLinkLength(
        "Neck",
        linkDimensions["Neck"]["Z"],
        linkDimensions["Neck"]["X"] / 2,
        linkDimensions["Neck"]["Z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # HEAD
    setLinkLength(
        "Head",
        None,
        linkDimensions["Head"]["X"] / 2,
        linkDimensions["Head"]["X"] / 2,
        "Z",
        "SPHERE",
        robot,
    )

    # RIGHT UPPER ARM
    setLinkLength(
        "RightUpperArm",
        linkDimensions["UpperArm"]["Y"],
        linkDimensions["UpperArm"]["X"] / 2,
        -linkDimensions["UpperArm"]["Y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # RIGHT FOREARM
    setLinkLength(
        "RightForeArm",
        linkDimensions["ForeArm"]["Y"],
        linkDimensions["ForeArm"]["X"] / 2,
        -linkDimensions["ForeArm"]["Y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # RIGHT HAND
    setLinkLength(
        "RightHand",
        linkDimensions["Hand"]["Y"],
        None,
        -linkDimensions["Hand"]["Y"] / 2,
        "Y",
        "BOX",
        robot,
    )
    setLinkLength(
        "RightHand", linkDimensions["Hand"]["X"], None, None, "X", "BOX", robot
    )
    setLinkLength(
        "RightHand", linkDimensions["Hand"]["Z"], None, None, "Z", "BOX", robot
    )

    # LEFT UPPER ARM
    setLinkLength(
        "LeftUpperArm",
        linkDimensions["UpperArm"]["Y"],
        linkDimensions["UpperArm"]["X"] / 2,
        linkDimensions["UpperArm"]["Y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # LEFT FOREARM
    setLinkLength(
        "LeftForeArm",
        linkDimensions["ForeArm"]["Y"],
        linkDimensions["ForeArm"]["X"] / 2,
        linkDimensions["ForeArm"]["Y"] / 2,
        "Y",
        "CYLINDER",
        robot,
    )

    # LEFT HAND
    setLinkLength(
        "LeftHand",
        linkDimensions["Hand"]["Y"],
        None,
        linkDimensions["Hand"]["Y"] / 2,
        "Y",
        "BOX",
        robot,
    )
    setLinkLength(
        "LeftHand", linkDimensions["Hand"]["X"], None, None, "X", "BOX", robot
    )
    setLinkLength(
        "LeftHand", linkDimensions["Hand"]["Z"], None, None, "Z", "BOX", robot
    )

    # RIGHT THIGH
    setLinkLength(
        "RightUpperLeg",
        linkDimensions["UpperLeg"]["Z"],
        linkDimensions["UpperLeg"]["X"] / 2,
        -linkDimensions["UpperLeg"]["Z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # RIGHT LOWER LEG
    setLinkLength(
        "RightLowerLeg",
        linkDimensions["LowerLeg"]["Z"],
        linkDimensions["LowerLeg"]["X"] / 2,
        -linkDimensions["LowerLeg"]["Z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # RIGHT FOOT
    setLinkLength(
        "RightFoot",
        linkDimensions["Foot"]["Z"],
        None,
        -linkDimensions["Foot"]["Z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "RightFoot", linkDimensions["Foot"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "RightFoot",
        linkDimensions["Foot"]["X"],
        None,
        abs((linkDimensions["LowerLeg"]["X"] / 2) - (linkDimensions["Foot"]["X"] / 2)),
        "X",
        "BOX",
        robot,
    )

    # RIGHT TOE
    setLinkLength("RightToe", linkDimensions["Toe"]["Z"], None, None, "Z", "BOX", robot)
    setLinkLength(
        "RightToe", linkDimensions["Toe"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "RightToe", linkDimensions["Toe"]["X"], None, None, "X", "BOX", robot
    )  # depth

    # LEFT THIGH
    setLinkLength(
        "LeftUpperLeg",
        linkDimensions["UpperLeg"]["Z"],
        linkDimensions["UpperLeg"]["X"] / 2,
        -linkDimensions["UpperLeg"]["Z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # LEFT LOWER LEG
    setLinkLength(
        "LeftLowerLeg",
        linkDimensions["LowerLeg"]["Z"],
        linkDimensions["LowerLeg"]["X"] / 2,
        -linkDimensions["LowerLeg"]["Z"] / 2,
        "Z",
        "CYLINDER",
        robot,
    )

    # LEFT FOOT
    setLinkLength(
        "LeftFoot",
        linkDimensions["Foot"]["Z"],
        None,
        -linkDimensions["Foot"]["Z"] / 2,
        "Z",
        "BOX",
        robot,
    )
    setLinkLength(
        "LeftFoot", linkDimensions["Foot"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "LeftFoot",
        linkDimensions["Foot"]["X"],
        None,
        abs((linkDimensions["LowerLeg"]["X"] / 2) - (linkDimensions["Foot"]["X"] / 2)),
        "X",
        "BOX",
        robot,
    )  # depth

    # LEFT TOE
    setLinkLength("LeftToe", linkDimensions["Toe"]["Z"], None, None, "Z", "BOX", robot)
    setLinkLength(
        "LeftToe", linkDimensions["Toe"]["Y"], None, None, "Y", "BOX", robot
    )  # width
    setLinkLength(
        "LeftToe", linkDimensions["Toe"]["X"], None, None, "X", "BOX", robot
    )  # depth

    return robot


def modifyLinkmass(linkMass, robot):
    ##############################################################################################
    # MASS MODIFICATION
    ##############################################################################################

    # MASS PELVIS
    setMassPercentage("Pelvis", linkMass["Pelvis_mass"], "Z", robot)

    # MASS LOWER TRUNK
    setMassPercentage("LowerTrunk", linkMass["LowerTrunk_mass"], "Z", robot)

    # MASS UPPER TRUNK
    setMassPercentage("UpperTrunk", linkMass["UpperTrunk_mass"], "Z", robot)

    # MASS RIGHT SHOULDER
    setMassPercentage("RightShoulder", linkMass["Shoulder_mass"], "Z", robot)

    # MASS LEFT SHOULDER
    setMassPercentage("LeftShoulder", linkMass["Shoulder_mass"], "Z", robot)

    # MASS NECK
    setMassPercentage("Neck", linkMass["Neck_mass"], "Z", robot)

    # MASS HEAD
    setMassPercentage("Head", linkMass["Head_mass"], "Z", robot)

    # MASS RIGHT UPPER ARM
    setMassPercentage("RightUpperArm", linkMass["UpperArm_mass"], "Z", robot)

    # MASS LEFT UPPER ARM
    setMassPercentage("LeftUpperArm", linkMass["UpperArm_mass"], "Z", robot)

    # MASS RIGHT FOREARM
    setMassPercentage("RightForeArm", linkMass["ForeArm_mass"], "Z", robot)

    # MASS LEFT FOREARM
    setMassPercentage("LeftForeArm", linkMass["ForeArm_mass"], "Z", robot)

    # MASS RIGHT HAND
    setMassPercentage("RightHand", linkMass["Hand_mass"], "Z", robot)

    # MASS LEFT HAND
    setMassPercentage("LeftHand", linkMass["Hand_mass"], "Z", robot)

    # MASS RIGHT UPPER LEG
    setMassPercentage("RightUpperLeg", linkMass["UpperLeg_mass"], "Z", robot)

    # MASS LEFT UPPER LEG
    setMassPercentage("LeftUpperLeg", linkMass["UpperLeg_mass"], "Z", robot)

    # MASS RIGHT LOWER LEG
    setMassPercentage("RightLowerLeg", linkMass["LowerLeg_mass"], "Z", robot)

    # MASS LEFT LOWER LEG
    setMassPercentage("LeftLowerLeg", linkMass["LowerLeg_mass"], "Z", robot)

    # MASS RIGHT FOOT
    setMassPercentage("RightFoot", linkMass["Foot_mass"], "Z", robot)

    # MASS LEFT FOOT
    setMassPercentage("LeftFoot", linkMass["Foot_mass"], "Z", robot)

    # MASS RIGHT TOE
    setMassPercentage("RightToe", linkMass["Toe_mass"], "Z", robot)

    # MASS LEFT TOE
    setMassPercentage("LeftToe", linkMass["Toe_mass"], "Z", robot)

    return robot


def modifyJointPosition(jointPosition, robot):
    ##############################################################################################
    # JOINT MODIFICATION
    ##############################################################################################

    # JOINT PELVI-LowerTrunk
    setJointPosition("jL5S1_rotx", jointPosition["jL5S1"]["Z"], "Z", robot)

    # JOINT LowerTrunk-UpperTrunk
    setJointPosition("jT9T8_rotx", jointPosition["jT9T8"]["Z"], "Z", robot)

    # JOINT UpperTrunk-RightShoulder
    setJointPosition(
        "jC7RightShoulder_rotx", jointPosition["jC7RightShoulder"]["Z"], "Z", robot
    )
    setJointPosition(
        "jC7RightShoulder_rotx", jointPosition["jC7RightShoulder"]["Y"], "Y", robot
    )

    # JOINT UpperTrunk-LeftShoulder
    setJointPosition(
        "jC7LeftShoulder_rotx", jointPosition["jC7LeftShoulder"]["Z"], "Z", robot
    )
    setJointPosition(
        "jC7LeftShoulder_rotx", jointPosition["jC7LeftShoulder"]["Y"], "Y", robot
    )

    # JOINT UPPERTRUNK - NECK
    setJointPosition("jT1C7_rotx", jointPosition["jT1C7"]["Z"], "Z", robot)

    # JOINT NECK - HEAD
    setJointPosition("jC1Head_rotx", jointPosition["jC1Head"]["Z"], "Z", robot)

    # JOINT RIGHT SHOULDER
    setJointPosition(
        "jRightShoulder_rotx", jointPosition["jRightShoulder"]["Y"], "Y", robot
    )

    # JOINT RIGHT ELBOW
    setJointPosition("jRightElbow_roty", jointPosition["jRightElbow"]["Y"], "Y", robot)

    # JOINT RIGHT WRIST
    setJointPosition("jRightWrist_rotx", jointPosition["jRightWrist"]["Y"], "Y", robot)

    # JOINT RIGHT HAND COM
    setJointPosition("jRightHandCOM", jointPosition["jRightHandCOM"]["Y"], "Y", robot)

    # JOINT LEFT SHOULDER
    setJointPosition(
        "jLeftShoulder_rotx", jointPosition["jLeftShoulder"]["Y"], "Y", robot
    )

    # JOINT LEFT ELBOW
    setJointPosition("jLeftElbow_roty", jointPosition["jLeftElbow"]["Y"], "Y", robot)

    # JOINT LEFT WRIST
    setJointPosition("jLeftWrist_rotx", jointPosition["jLeftWrist"]["Y"], "Y", robot)

    # JOINT LEFT HAND COM
    setJointPosition("jLeftHandCOM", jointPosition["jLeftHandCOM"]["Y"], "Y", robot)

    # JOINT RIGHT HIP
    setJointPosition("jRightHip_rotx", jointPosition["jRightHip"]["Y"], "Y", robot)
    setJointPosition("jRightHip_rotx", jointPosition["jRightHip"]["Z"], "Z", robot)

    # JOINT RIGHT KNEE
    setJointPosition("jRightKnee_roty", jointPosition["jRightKnee"]["Z"], "Z", robot)

    # JOINT RIGHT ANKLE
    setJointPosition("jRightAnkle_rotx", jointPosition["jRightAnkle"]["Z"], "Z", robot)
    setJointPosition("jRightAnkle_rotx", jointPosition["jRightAnkle"]["X"], "X", robot)

    # JOINT RIGHT TOE
    setJointPosition(
        "jRightBallFoot_roty", jointPosition["jRightBallFoot"]["X"], "X", robot
    )
    setJointPosition(
        "jRightBallFoot_roty", jointPosition["jRightBallFoot"]["Z"], "Z", robot
    )

    # JOINT RIGHT FT SENSOR
    setJointPosition(
        "jRightBirken_roty", jointPosition["jRightBirken"]["X"], "X", robot
    )
    setJointPosition(
        "jRightBirken_roty", jointPosition["jRightBirken"]["Z"], "Z", robot
    )

    # JOINT LEFT HIP
    setJointPosition("jLeftHip_rotx", jointPosition["jLeftHip"]["Y"], "Y", robot)
    setJointPosition("jLeftHip_rotx", jointPosition["jLeftHip"]["Z"], "Z", robot)

    # JOINT LEFT KNEE
    setJointPosition("jLeftKnee_roty", jointPosition["jLeftKnee"]["Z"], "Z", robot)

    # JOINT LEFT ANKLE
    setJointPosition("jLeftAnkle_rotx", jointPosition["jLeftAnkle"]["Z"], "Z", robot)
    setJointPosition("jLeftAnkle_rotx", jointPosition["jLeftAnkle"]["X"], "X", robot)

    # JOINT LEFT TOE
    setJointPosition(
        "jLeftBallFoot_roty", jointPosition["jLeftBallFoot"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftBallFoot_roty", jointPosition["jLeftBallFoot"]["Z"], "Z", robot
    )

    # JOINT LEFT FT SENSOR
    setJointPosition("jLeftBirken_roty", jointPosition["jLeftBirken"]["X"], "X", robot)
    setJointPosition("jLeftBirken_roty", jointPosition["jLeftBirken"]["Z"], "Z", robot)

    return robot


def modifyMuscleJointPosition(jointMusclePosition, robot):
    ##############################################################################################
    # MUSCLE FRAME
    ##############################################################################################

    # Biceps
    setJointPosition(
        "jRightBicBrac_RUA", jointMusclePosition["jRightBicBrac_RUA"]["X"], "X", robot
    )
    setJointPosition(
        "jRightBicBrac_RUA", jointMusclePosition["jRightBicBrac_RUA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightBicBrac_RFA", jointMusclePosition["jRightBicBrac_RFA"]["X"], "X", robot
    )
    setJointPosition(
        "jRightBicBrac_RFA", jointMusclePosition["jRightBicBrac_RFA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftBicBrac_LUA", jointMusclePosition["jLeftBicBrac_LUA"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftBicBrac_LUA", jointMusclePosition["jLeftBicBrac_LUA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftBicBrac_LFA", jointMusclePosition["jLeftBicBrac_LFA"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftBicBrac_LFA", jointMusclePosition["jLeftBicBrac_LFA"]["Z"], "Z", robot
    )

    # Triceps
    setJointPosition(
        "jRightTricBrac_RUA", jointMusclePosition["jRightTricBrac_RUA"]["X"], "X", robot
    )
    setJointPosition(
        "jRightTricBrac_RUA", jointMusclePosition["jRightTricBrac_RUA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightTricBrac_RFA", jointMusclePosition["jRightTricBrac_RFA"]["X"], "X", robot
    )
    setJointPosition(
        "jRightTricBrac_RFA", jointMusclePosition["jRightTricBrac_RFA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftTricBrac_LUA", jointMusclePosition["jLeftTricBrac_LUA"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftTricBrac_LUA", jointMusclePosition["jLeftTricBrac_LUA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftTricBrac_LFA", jointMusclePosition["jLeftTricBrac_LFA"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftTricBrac_LFA", jointMusclePosition["jLeftTricBrac_LFA"]["Z"], "Z", robot
    )

    # Flexor carpi radialis
    setJointPosition(
        "jRightFlexCarp_RFA", jointMusclePosition["jRightFlexCarp_RFA"]["X"], "X", robot
    )
    setJointPosition(
        "jRightFlexCarp_RFA", jointMusclePosition["jRightFlexCarp_RFA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightFlexCarp_RH", jointMusclePosition["jRightFlexCarp_RH"]["X"], "X", robot
    )
    setJointPosition(
        "jRightFlexCarp_RH", jointMusclePosition["jRightFlexCarp_RH"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightFlexCarp_RH", jointMusclePosition["jRightFlexCarp_RH"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LFA", jointMusclePosition["jLeftFlexCarp_LFA"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LFA", jointMusclePosition["jLeftFlexCarp_LFA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LH", jointMusclePosition["jLeftFlexCarp_LH"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LH", jointMusclePosition["jLeftFlexCarp_LH"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftFlexCarp_LH", jointMusclePosition["jLeftFlexCarp_LH"]["Z"], "Z", robot
    )

    # Extensor carpi radialis
    setJointPosition(
        "jRightExtCarp_RFA", jointMusclePosition["jRightExtCarp_RFA"]["X"], "X", robot
    )
    setJointPosition(
        "jRightExtCarp_RFA", jointMusclePosition["jRightExtCarp_RFA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightExtCarp_RH", jointMusclePosition["jRightExtCarp_RH"]["X"], "X", robot
    )
    setJointPosition(
        "jRightExtCarp_RH", jointMusclePosition["jRightExtCarp_RH"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightExtCarp_RH", jointMusclePosition["jRightExtCarp_RH"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftExtCarp_LFA", jointMusclePosition["jLeftExtCarp_LFA"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftExtCarp_LFA", jointMusclePosition["jLeftExtCarp_LFA"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftExtCarp_LH", jointMusclePosition["jLeftExtCarp_LH"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftExtCarp_LH", jointMusclePosition["jLeftExtCarp_LH"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftExtCarp_LH", jointMusclePosition["jLeftExtCarp_LH"]["Z"], "Z", robot
    )

    # Erector spinae longissimus
    setJointPosition(
        "jRightErSpin_RUT", jointMusclePosition["jRightErSpin_RUT"]["X"], "X", robot
    )
    setJointPosition(
        "jRightErSpin_RUT", jointMusclePosition["jRightErSpin_RUT"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightErSpin_RUT", jointMusclePosition["jRightErSpin_RUT"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightErSpin_RP", jointMusclePosition["jRightErSpin_RP"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftErSpin_LUT", jointMusclePosition["jLeftErSpin_LUT"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftErSpin_LUT", jointMusclePosition["jLeftErSpin_LUT"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftErSpin_LUT", jointMusclePosition["jLeftErSpin_LUT"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftErSpin_LP", jointMusclePosition["jLeftErSpin_LP"]["X"], "X", robot
    )

    # Rectus abdominis
    setJointPosition(
        "jRightRecAbd_RUT", jointMusclePosition["jRightRecAbd_RUT"]["X"], "X", robot
    )
    setJointPosition(
        "jRightRecAbd_RUT", jointMusclePosition["jRightRecAbd_RUT"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightRecAbd_RP", jointMusclePosition["jRightRecAbd_RP"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftRecAbd_LUT", jointMusclePosition["jLeftRecAbd_LUT"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftRecAbd_LUT", jointMusclePosition["jLeftRecAbd_LUT"]["Y"], "Y", robot
    )

    # Biceps femoris
    setJointPosition(
        "jRightBicFem_RUL", jointMusclePosition["jRightBicFem_RUL"]["X"], "X", robot
    )
    setJointPosition(
        "jRightBicFem_RUL", jointMusclePosition["jRightBicFem_RUL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightBicFem_RLL", jointMusclePosition["jRightBicFem_RLL"]["X"], "X", robot
    )
    setJointPosition(
        "jRightBicFem_RLL", jointMusclePosition["jRightBicFem_RLL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftBicFem_LUL", jointMusclePosition["jLeftBicFem_LUL"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftBicFem_LUL", jointMusclePosition["jLeftBicFem_LUL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftBicFem_LLL", jointMusclePosition["jLeftBicFem_LLL"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftBicFem_LLL", jointMusclePosition["jLeftBicFem_LLL"]["Y"], "Y", robot
    )

    # Rectus femoris
    setJointPosition(
        "jRightRecFem_RP", jointMusclePosition["jRightRecFem_RP"]["X"], "X", robot
    )
    setJointPosition(
        "jRightRecFem_RP", jointMusclePosition["jRightRecFem_RP"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightRecFem_RP", jointMusclePosition["jRightRecFem_RP"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightRecFem_RLL", jointMusclePosition["jRightRecFem_RLL"]["X"], "X", robot
    )
    setJointPosition(
        "jRightRecFem_RLL", jointMusclePosition["jRightRecFem_RLL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftRecFem_LP", jointMusclePosition["jLeftRecFem_LP"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftRecFem_LP", jointMusclePosition["jLeftRecFem_LP"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftRecFem_LP", jointMusclePosition["jLeftRecFem_LP"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftRecFem_LLL", jointMusclePosition["jLeftRecFem_LLL"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftRecFem_LLL", jointMusclePosition["jLeftRecFem_LLL"]["Y"], "Y", robot
    )

    # Tibialis anterior
    setJointPosition(
        "jRightTibAnt_RLL", jointMusclePosition["jRightTibAnt_RLL"]["X"], "X", robot
    )
    setJointPosition(
        "jRightTibAnt_RLL", jointMusclePosition["jRightTibAnt_RLL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightTibAnt_RF", jointMusclePosition["jRightTibAnt_RF"]["X"], "X", robot
    )
    setJointPosition(
        "jRightTibAnt_RF", jointMusclePosition["jRightTibAnt_RF"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftTibAnt_LLL", jointMusclePosition["jLeftTibAnt_LLL"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftTibAnt_LLL", jointMusclePosition["jLeftTibAnt_LLL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftTibAnt_LF", jointMusclePosition["jLeftTibAnt_LF"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftTibAnt_LF", jointMusclePosition["jLeftTibAnt_LF"]["Y"], "Y", robot
    )

    # Gastrocnemius medialis
    setJointPosition(
        "jRightGasMed_RUL", jointMusclePosition["jRightGasMed_RUL"]["X"], "X", robot
    )
    setJointPosition(
        "jRightGasMed_RUL", jointMusclePosition["jRightGasMed_RUL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightGasMed_RUL", jointMusclePosition["jRightGasMed_RUL"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightGasMed_RF", jointMusclePosition["jRightGasMed_RF"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightGasMed_RF", jointMusclePosition["jRightGasMed_RF"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftGasMed_LUL", jointMusclePosition["jLeftGasMed_LUL"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftGasMed_LUL", jointMusclePosition["jLeftGasMed_LUL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftGasMed_LUL", jointMusclePosition["jLeftGasMed_LUL"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasMed_LF", jointMusclePosition["jLeftGasMed_LF"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasMed_LF", jointMusclePosition["jLeftGasMed_LF"]["X"], "X", robot
    )

    # Gastrocnemius lateralis
    setJointPosition(
        "jRightGasLat_RUL", jointMusclePosition["jRightGasLat_RUL"]["X"], "X", robot
    )
    setJointPosition(
        "jRightGasLat_RUL", jointMusclePosition["jRightGasLat_RUL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jRightGasLat_RUL", jointMusclePosition["jRightGasLat_RUL"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightGasLat_RF", jointMusclePosition["jRightGasLat_RF"]["Z"], "Z", robot
    )
    setJointPosition(
        "jRightGasLat_RF", jointMusclePosition["jRightGasLat_RF"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftGasLat_LUL", jointMusclePosition["jLeftGasLat_LUL"]["X"], "X", robot
    )
    setJointPosition(
        "jLeftGasLat_LUL", jointMusclePosition["jLeftGasLat_LUL"]["Y"], "Y", robot
    )
    setJointPosition(
        "jLeftGasLat_LUL", jointMusclePosition["jLeftGasLat_LUL"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasLat_LF", jointMusclePosition["jLeftGasLat_LF"]["Z"], "Z", robot
    )
    setJointPosition(
        "jLeftGasLat_LF", jointMusclePosition["jLeftGasLat_LF"]["X"], "X", robot
    )


    return robot
