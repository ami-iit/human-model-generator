# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

import numpy as np


def scaleLink(H, linkDimensions, MODEL_TYPE):
    # Links' length and width modification

    # Common dimensions
    linkDimensions["Head"]["X"] = 0.13 * H
    linkDimensions["Head"]["Y"] = 0.13 * H
    linkDimensions["Head"]["Z"] = 0.13 * H

    linkDimensions["Neck"]["Z"] = 0.052 * H

    linkDimensions["UpperArm"]["Y"] = 0.186 * H

    linkDimensions["ForeArm"]["Y"] = 0.146 * H

    linkDimensions["Hand"]["Y"] = 0.108 * H

    linkDimensions["UpperLeg"]["Z"] = 0.245 * H

    linkDimensions["LowerLeg"]["Z"] = 0.246 * H

    linkDimensions["Foot"]["X"] = 0.152 * H
    linkDimensions["Foot"]["Y"] = 0.055 * H
    linkDimensions["Foot"]["Z"] = 0.039 * H

    # Model-specific dimensions
    if MODEL_TYPE == "Dumas":
        linkDimensions["UpperTrunk"]["Z"] = 0.167 * H
        linkDimensions["UpperTrunk"]["Y"] = 0.259 * H / 3

        linkDimensions["Shoulder"]["X"] = linkDimensions["UpperArm"].get("X", 0)
        linkDimensions["Shoulder"]["Y"] = 0.259 * H / 3

        linkDimensions["LowerTrunk"]["Z"] = 0.067 * H
        linkDimensions["LowerTrunk"]["Y"] = 0.174 * H

        linkDimensions["Pelvis"]["Z"] = 0.054 * H
        linkDimensions["Pelvis"]["Y"] = 0.191 * H

    elif MODEL_TYPE == "DeLeva":
        linkDimensions["UpperTrunk"]["Z"] = 0.11 * H
        linkDimensions["UpperTrunk"]["Y"] = 0.259 * H / 3

        linkDimensions["Shoulder"]["X"] = linkDimensions["UpperArm"].get("X", 0)
        linkDimensions["Shoulder"]["Y"] = 0.259 * H / 3

        linkDimensions["LowerTrunk"]["Z"] = 0.1 * H
        linkDimensions["LowerTrunk"]["Y"] = 0.174 * H

        linkDimensions["Pelvis"]["Z"] = 0.078 * H
        linkDimensions["Pelvis"]["Y"] = 0.191 * H

    # Toe dimensions
    linkDimensions["Toe"]["X"] = linkDimensions["Foot"]["X"] / 100
    linkDimensions["Toe"]["Y"] = linkDimensions["Foot"]["Y"]
    linkDimensions["Toe"]["Z"] = linkDimensions["Foot"]["Z"]

    return linkDimensions


def scaleJoint(linkDimensions, jointPosition):
    # Joints' position modification
    jointPosition["jL5S1"]["X"] = 0
    jointPosition["jL5S1"]["Y"] = 0
    jointPosition["jL5S1"]["Z"] = linkDimensions["Pelvis"]["Z"] / 2

    jointPosition["jT9T8"]["X"] = 0
    jointPosition["jT9T8"]["Y"] = 0
    jointPosition["jT9T8"]["Z"] = linkDimensions["LowerTrunk"]["Z"]

    jointPosition["jC7RightShoulder"]["X"] = 0
    jointPosition["jC7RightShoulder"]["Y"] = -linkDimensions["UpperTrunk"]["Y"] / 2
    jointPosition["jC7RightShoulder"]["Z"] = (
        linkDimensions["UpperTrunk"]["Z"] - linkDimensions["Shoulder"]["X"] / 2
    )

    jointPosition["jC7LeftShoulder"]["X"] = 0
    jointPosition["jC7LeftShoulder"]["Y"] = linkDimensions["UpperTrunk"]["Y"] / 2
    jointPosition["jC7LeftShoulder"]["Z"] = (
        linkDimensions["UpperTrunk"]["Z"] - linkDimensions["Shoulder"]["X"] / 2
    )

    jointPosition["jT1C7"]["X"] = 0
    jointPosition["jT1C7"]["Y"] = 0
    jointPosition["jT1C7"]["Z"] = linkDimensions["UpperTrunk"]["Z"]

    jointPosition["jC1Head"]["X"] = 0
    jointPosition["jC1Head"]["Y"] = 0
    jointPosition["jC1Head"]["Z"] = linkDimensions["Neck"]["Z"]

    jointPosition["jRightShoulder"]["X"] = 0
    jointPosition["jRightShoulder"]["Y"] = -linkDimensions["UpperTrunk"]["Y"]

    jointPosition["jRightElbow"]["X"] = 0
    jointPosition["jRightElbow"]["Y"] = -linkDimensions["UpperArm"]["Y"]

    jointPosition["jRightWrist"]["X"] = 0
    jointPosition["jRightWrist"]["Y"] = -linkDimensions["ForeArm"]["Y"]

    jointPosition["jRightHandCOM"]["X"] = 0
    jointPosition["jRightHandCOM"]["Y"] = -linkDimensions["Hand"]["Y"] / 2

    jointPosition["jLeftShoulder"]["X"] = 0
    jointPosition["jLeftShoulder"]["Y"] = linkDimensions["UpperTrunk"]["Y"]

    jointPosition["jLeftElbow"]["X"] = 0
    jointPosition["jLeftElbow"]["Y"] = linkDimensions["UpperArm"]["Y"]

    jointPosition["jLeftWrist"]["X"] = 0
    jointPosition["jLeftWrist"]["Y"] = linkDimensions["ForeArm"]["Y"]

    jointPosition["jLeftHandCOM"]["X"] = 0
    jointPosition["jLeftHandCOM"]["Y"] = linkDimensions["Hand"]["Y"] / 2

    jointPosition["jRightHip"]["X"] = 0
    jointPosition["jRightHip"]["Y"] = -(
        linkDimensions["Pelvis"]["Y"] / 2 - linkDimensions["UpperLeg"]["X"] / 2
    )
    jointPosition["jRightHip"]["Z"] = -linkDimensions["Pelvis"]["Z"] / 2

    jointPosition["jRightKnee"]["X"] = 0
    jointPosition["jRightKnee"]["Y"] = 0
    jointPosition["jRightKnee"]["Z"] = -linkDimensions["UpperLeg"]["Z"]

    jointPosition["jRightAnkle"]["X"] = 0
    jointPosition["jRightAnkle"]["Y"] = 0
    jointPosition["jRightAnkle"]["Z"] = -linkDimensions["LowerLeg"]["Z"]

    jointPosition["jRightBallFoot"]["X"] = (
        linkDimensions["LowerLeg"]["X"] / 2
        + abs(linkDimensions["LowerLeg"]["X"] - linkDimensions["Foot"]["X"])
        + linkDimensions["Toe"]["X"] / 2
    )
    jointPosition["jRightBallFoot"]["Y"] = 0
    jointPosition["jRightBallFoot"]["Z"] = -linkDimensions["Foot"]["Z"] / 2

    jointPosition["jLeftHip"]["X"] = 0
    jointPosition["jLeftHip"]["Y"] = (
        linkDimensions["Pelvis"]["Y"] / 2 - linkDimensions["UpperLeg"]["X"] / 2
    )
    jointPosition["jLeftHip"]["Z"] = -linkDimensions["Pelvis"]["Z"] / 2

    jointPosition["jLeftKnee"]["X"] = 0
    jointPosition["jLeftKnee"]["Y"] = 0
    jointPosition["jLeftKnee"]["Z"] = -linkDimensions["UpperLeg"]["Z"]

    jointPosition["jLeftAnkle"]["X"] = 0
    jointPosition["jLeftAnkle"]["Y"] = 0
    jointPosition["jLeftAnkle"]["Z"] = -linkDimensions["LowerLeg"]["Z"]

    jointPosition["jLeftBallFoot"]["X"] = (
        linkDimensions["LowerLeg"]["X"] / 2
        + abs(linkDimensions["LowerLeg"]["X"] - linkDimensions["Foot"]["X"])
        + linkDimensions["Toe"]["X"] / 2
    )
    jointPosition["jLeftBallFoot"]["Y"] = 0
    jointPosition["jLeftBallFoot"]["Z"] = -linkDimensions["Foot"]["Z"] / 2

    jointPosition["jRightBirken"]["X"] = 0.037
    jointPosition["jRightBirken"]["Y"] = 0
    jointPosition["jRightBirken"]["Z"] = -linkDimensions["Foot"]["Z"] - 0.055

    jointPosition["jLeftBirken"]["X"] = 0.037
    jointPosition["jLeftBirken"]["Y"] = 0
    jointPosition["jLeftBirken"]["Z"] = -linkDimensions["Foot"]["Z"] - 0.055

    return jointPosition



def scaleMuscleJoint(linkDimensions, jointMusclePosition):
    pi = np.pi


    # Biceps brachialis
    jointMusclePosition["jRightBicBrac_RUA"]["X"] = (-1) * (linkDimensions["UpperArm"]["X"] / 2) * np.cos((pi / 2))
    jointMusclePosition["jRightBicBrac_RUA"]["Y"] = 0
    jointMusclePosition["jRightBicBrac_RUA"]["Z"] = (linkDimensions["UpperArm"]["X"] / 2) * np.sin((pi / 2))
    
    jointMusclePosition["jRightBicBrac_RFA"]["X"] = (-1) * (linkDimensions["ForeArm"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jRightBicBrac_RFA"]["Y"] = 0
    jointMusclePosition["jRightBicBrac_RFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin((pi / 2))
    
    jointMusclePosition["jLeftBicBrac_LUA"]["X"] = (linkDimensions["UpperArm"]["X"] / 2) * np.cos((pi / 2))
    jointMusclePosition["jLeftBicBrac_LUA"]["Y"] = 0
    jointMusclePosition["jLeftBicBrac_LUA"]["Z"] = (linkDimensions["UpperArm"]["X"] / 2) * np.sin((pi / 2))
    
    jointMusclePosition["jLeftBicBrac_LFA"]["X"] = (linkDimensions["ForeArm"]["X"] / 2) * np.cos(0)
    jointMusclePosition["jLeftBicBrac_LFA"]["Y"] = 0
    jointMusclePosition["jLeftBicBrac_LFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(0)
    
    # Triceps
    jointMusclePosition["jRightTricBrac_RUA"]["X"] = (-1) * (linkDimensions["UpperArm"]["X"] / 2) * np.cos(0)
    jointMusclePosition["jRightTricBrac_RUA"]["Y"] = 0
    jointMusclePosition["jRightTricBrac_RUA"]["Z"] = (linkDimensions["UpperArm"]["X"] / 2) * np.sin(0)
    
    jointMusclePosition["jRightTricBrac_RFA"]["X"] = (linkDimensions["ForeArm"]["X"] / 2) * np.cos(0)
    jointMusclePosition["jRightTricBrac_RFA"]["Y"] = 0
    jointMusclePosition["jRightTricBrac_RFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(0)
    
    jointMusclePosition["jLeftTricBrac_LUA"]["X"] = (-1) * (linkDimensions["UpperArm"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jLeftTricBrac_LUA"]["Y"] = 0
    jointMusclePosition["jLeftTricBrac_LUA"]["Z"] = (linkDimensions["UpperArm"]["X"] / 2) * np.sin(pi)
    
    jointMusclePosition["jLeftTricBrac_LFA"]["X"] = (-1) * (linkDimensions["ForeArm"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jLeftTricBrac_LFA"]["Y"] = 0
    jointMusclePosition["jLeftTricBrac_LFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(pi)
    
    # Flexor carpi radialis
    jointMusclePosition["jRightFlexCarp_RFA"]["X"] = (-1) * (linkDimensions["ForeArm"]["X"] / 2) * np.cos(0)
    jointMusclePosition["jRightFlexCarp_RFA"]["Y"] = 0
    jointMusclePosition["jRightFlexCarp_RFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(0)
    
    jointMusclePosition["jRightFlexCarp_RH"]["X"] = linkDimensions["Hand"]["X"] / 5
    jointMusclePosition["jRightFlexCarp_RH"]["Y"] = -linkDimensions["Hand"]["Y"] / 2
    jointMusclePosition["jRightFlexCarp_RH"]["Z"] = linkDimensions["Hand"]["Z"] / 2

    jointMusclePosition["jLeftFlexCarp_LFA"]["X"] = (linkDimensions["ForeArm"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jLeftFlexCarp_LFA"]["Y"] = 0
    jointMusclePosition["jLeftFlexCarp_LFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(pi)
    
    jointMusclePosition["jLeftFlexCarp_LH"]["X"] = linkDimensions["Hand"]["X"] / 5
    jointMusclePosition["jLeftFlexCarp_LH"]["Y"] = linkDimensions["Hand"]["Y"] / 2
    jointMusclePosition["jLeftFlexCarp_LH"]["Z"] = linkDimensions["Hand"]["Z"] / 2

    # Extensor carpi radialis
    jointMusclePosition["jRightExtCarp_RFA"]["X"] = (-1) * (linkDimensions["ForeArm"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jRightExtCarp_RFA"]["Y"] = 0
    jointMusclePosition["jRightExtCarp_RFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(pi)
    
    jointMusclePosition["jRightExtCarp_RH"]["X"] = linkDimensions["Hand"]["X"] / 5
    jointMusclePosition["jRightExtCarp_RH"]["Y"] = -linkDimensions["Hand"]["Y"] / 2
    jointMusclePosition["jRightExtCarp_RH"]["Z"] = -linkDimensions["Hand"]["Z"] / 2

    jointMusclePosition["jLeftExtCarp_LFA"]["X"] = (linkDimensions["ForeArm"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jLeftExtCarp_LFA"]["Y"] = 0
    jointMusclePosition["jLeftExtCarp_LFA"]["Z"] = (linkDimensions["ForeArm"]["X"] / 2) * np.sin(pi)
    
    jointMusclePosition["jLeftExtCarp_LH"]["X"] = linkDimensions["Hand"]["X"] / 5
    jointMusclePosition["jLeftExtCarp_LH"]["Y"] = linkDimensions["Hand"]["Y"] / 2
    jointMusclePosition["jLeftExtCarp_LH"]["Z"] = -linkDimensions["Hand"]["Z"]

    # Erector Spinae
    jointMusclePosition["jRightErSpin_RUT"]["X"] = -linkDimensions["UpperTrunk"]["X"] / 2
    jointMusclePosition["jRightErSpin_RUT"]["Y"] = -linkDimensions["UpperTrunk"]["Y"] / 2
    jointMusclePosition["jRightErSpin_RUT"]["Z"] = linkDimensions["UpperTrunk"]["Z"]
    
    jointMusclePosition["jRightErSpin_RP"]["X"] = -linkDimensions["Pelvis"]["X"] / 2
    jointMusclePosition["jRightErSpin_RP"]["Y"] = 0
    jointMusclePosition["jRightErSpin_RP"]["Z"] = 0

    jointMusclePosition["jLeftErSpin_LUT"]["X"] = -linkDimensions["UpperTrunk"]["X"] / 2
    jointMusclePosition["jLeftErSpin_LUT"]["Y"] = linkDimensions["UpperTrunk"]["Y"] / 2
    jointMusclePosition["jLeftErSpin_LUT"]["Z"] = linkDimensions["UpperTrunk"]["Z"]
    
    jointMusclePosition["jLeftErSpin_LP"]["X"] = -linkDimensions["Pelvis"]["X"] / 2
    jointMusclePosition["jLeftErSpin_LP"]["Y"] = 0
    jointMusclePosition["jLeftErSpin_LP"]["Z"] = 0

    # Rectus Abdominis
    jointMusclePosition["jRightRecAbd_RUT"]["X"] = linkDimensions["UpperTrunk"]["X"] / 2
    jointMusclePosition["jRightRecAbd_RUT"]["Y"] = -linkDimensions["UpperTrunk"]["Y"] / 2
    jointMusclePosition["jRightRecAbd_RUT"]["Z"] = 0
    jointMusclePosition["jRightRecAbd_RP"]["X"] = linkDimensions["Pelvis"]["X"] / 2
    jointMusclePosition["jRightRecAbd_RP"]["Y"] = 0
    jointMusclePosition["jRightRecAbd_RP"]["Z"] = 0

    jointMusclePosition["jLeftRecAbd_LUT"]["X"] = linkDimensions["UpperTrunk"]["X"] / 2
    jointMusclePosition["jLeftRecAbd_LUT"]["Y"] = linkDimensions["UpperTrunk"]["Y"] / 2
    jointMusclePosition["jLeftRecAbd_LUT"]["Z"] = 0
    jointMusclePosition["jLeftRecAbd_LP"]["X"] = linkDimensions["Pelvis"]["X"] / 2
    jointMusclePosition["jLeftRecAbd_LP"]["Y"] = 0
    jointMusclePosition["jLeftRecAbd_LP"]["Z"] = 0

    # Biceps femoris
    jointMusclePosition["jRightBicFem_RUL"]["X"] = (linkDimensions["UpperLeg"]["X"] / 2) * np.sin((3 / 2) * pi)
    jointMusclePosition["jRightBicFem_RUL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos((3 / 2) * pi)
    jointMusclePosition["jRightBicFem_RUL"]["Z"] = 0
    jointMusclePosition["jRightBicFem_RLL"]["X"] = (linkDimensions["LowerLeg"]["X"] / 2) * np.sin(0)
    jointMusclePosition["jRightBicFem_RLL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos(0)
    jointMusclePosition["jRightBicFem_RLL"]["Z"] = 0

    jointMusclePosition["jLeftBicFem_LUL"]["X"] = (linkDimensions["UpperLeg"]["X"] / 2) * np.sin((3 / 2) * pi)
    jointMusclePosition["jLeftBicFem_LUL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos((3 / 2) * pi)
    jointMusclePosition["jLeftBicFem_LUL"]["Z"] = 0
    jointMusclePosition["jLeftBicFem_LLL"]["X"] = (linkDimensions["LowerLeg"]["X"] / 2) * np.sin(pi)
    jointMusclePosition["jLeftBicFem_LLL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos(pi)
    jointMusclePosition["jLeftBicFem_LLL"]["Z"] = 0

    # Rectus femoris
    jointMusclePosition["jRightRecFem_RP"]["X"] = linkDimensions["Pelvis"]["X"] / 2
    jointMusclePosition["jRightRecFem_RP"]["Y"] = -linkDimensions["Pelvis"]["Y"] / 3
    jointMusclePosition["jRightRecFem_RP"]["Z"] = -linkDimensions["Pelvis"]["Z"] / 2
    jointMusclePosition["jRightRecFem_RLL"]["X"] = (linkDimensions["LowerLeg"]["X"] / 2) * np.sin(pi / 2)
    jointMusclePosition["jRightRecFem_RLL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos(pi / 2)
    jointMusclePosition["jRightRecFem_RLL"]["Z"] = 0

    jointMusclePosition["jLeftRecFem_LP"]["X"] = linkDimensions["Pelvis"]["X"] / 2
    jointMusclePosition["jLeftRecFem_LP"]["Y"] = linkDimensions["Pelvis"]["Y"] / 3
    jointMusclePosition["jLeftRecFem_LP"]["Z"] = -linkDimensions["Pelvis"]["Z"] / 2
    jointMusclePosition["jLeftRecFem_LLL"]["X"] = (linkDimensions["LowerLeg"]["X"] / 2) * np.sin(pi / 2)
    jointMusclePosition["jLeftRecFem_LLL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos(pi / 2)
    jointMusclePosition["jLeftRecFem_LLL"]["Z"] = 0

    # Tibialis anterior
    jointMusclePosition["jRightTibAnt_RLL"]["X"] = (linkDimensions["LowerLeg"]["X"] / 2) * np.sin(pi / 2)
    jointMusclePosition["jRightTibAnt_RLL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos(pi / 2)
    jointMusclePosition["jRightTibAnt_RLL"]["Z"] = 0
    jointMusclePosition["jRightTibAnt_RF"]["X"] = linkDimensions["Foot"]["X"] / 2
    jointMusclePosition["jRightTibAnt_RF"]["Y"] = linkDimensions["Foot"]["Y"] / 2
    jointMusclePosition["jRightTibAnt_RF"]["Z"] = 0

    jointMusclePosition["jLeftTibAnt_LLL"]["X"] = (linkDimensions["LowerLeg"]["X"] / 2) * np.sin(pi / 2)
    jointMusclePosition["jLeftTibAnt_LLL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos(pi / 2)
    jointMusclePosition["jLeftTibAnt_LLL"]["Z"] = 0
    jointMusclePosition["jLeftTibAnt_LF"]["X"] = linkDimensions["Foot"]["X"] / 2
    jointMusclePosition["jLeftTibAnt_LF"]["Y"] = -linkDimensions["Foot"]["Y"] / 2
    jointMusclePosition["jLeftTibAnt_LF"]["Z"] = 0

    # Gastrocnemius medialis
    jointMusclePosition["jRightGasMed_RUL"]["X"] = (linkDimensions["UpperLeg"]["X"] / 2) * np.sin((4 / 3) * pi)
    jointMusclePosition["jRightGasMed_RUL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos((4 / 3) * pi)
    jointMusclePosition["jRightGasMed_RUL"]["Z"] = -linkDimensions["UpperLeg"]["Z"]
    jointMusclePosition["jRightGasMed_RF"]["X"] = -(linkDimensions["LowerLeg"]["X"] / 2)
    jointMusclePosition["jRightGasMed_RF"]["Y"] = 0
    jointMusclePosition["jRightGasMed_RF"]["Z"] = -linkDimensions["Foot"]["Z"] / 2

    jointMusclePosition["jLeftGasMed_LUL"]["X"] = (linkDimensions["UpperLeg"]["X"] / 2) * np.sin((5 / 3) * pi)
    jointMusclePosition["jLeftGasMed_LUL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos((5 / 3) * pi)
    jointMusclePosition["jLeftGasMed_LUL"]["Z"] = -linkDimensions["UpperLeg"]["Z"]
    jointMusclePosition["jLeftGasMed_LF"]["X"] = -(linkDimensions["LowerLeg"]["X"] / 2)
    jointMusclePosition["jLeftGasMed_LF"]["Y"] = 0
    jointMusclePosition["jLeftGasMed_LF"]["Z"] = -linkDimensions["Foot"]["Z"] / 2

    # Gastrocnemius lateralis
    jointMusclePosition["jRightGasLat_RUL"]["X"] = (linkDimensions["UpperLeg"]["X"] / 2) * np.sin((5 / 3) * pi)
    jointMusclePosition["jRightGasLat_RUL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos((5 / 3) * pi)
    jointMusclePosition["jRightGasLat_RUL"]["Z"] = -linkDimensions["UpperLeg"]["Z"]
    jointMusclePosition["jRightGasLat_RF"]["X"] = -(linkDimensions["LowerLeg"]["X"] / 2)
    jointMusclePosition["jRightGasLat_RF"]["Y"] = 0
    jointMusclePosition["jRightGasLat_RF"]["Z"] = -linkDimensions["Foot"]["Z"] / 2

    jointMusclePosition["jLeftGasLat_LUL"]["X"] = (linkDimensions["UpperLeg"]["X"] / 2) * np.sin((4 / 3) * pi)
    jointMusclePosition["jLeftGasLat_LUL"]["Y"] = (-1) * (linkDimensions["LowerLeg"]["X"] / 2) * np.cos((4 / 3) * pi)
    jointMusclePosition["jLeftGasLat_LUL"]["Z"] = -linkDimensions["UpperLeg"]["Z"]
    jointMusclePosition["jLeftGasLat_LF"]["X"] = -(linkDimensions["LowerLeg"]["X"] / 2)
    jointMusclePosition["jLeftGasLat_LF"]["Y"] = 0
    jointMusclePosition["jLeftGasLat_LF"]["Z"] = -linkDimensions["Foot"]["Z"] / 2

    return jointMusclePosition


def scaleMass(TotalMass, linkMass, MODEL_TYPE):
    if MODEL_TYPE == "Dumas":
        # Dumas, et. al 2007 & Dumas, et. al 2015 correction
        linkMass["Head_mass"] = 0.0479 * TotalMass
        linkMass["Neck_mass"] = 0.0191 * TotalMass
        linkMass["UpperTrunk_mass"] = 0.0945 * TotalMass
        linkMass["LowerTrunk_mass"] = 0.035 * TotalMass
        linkMass["Shoulder_mass"] = 0.0945 * TotalMass
        linkMass["Pelvis_mass"] = 0.1435 * TotalMass
        linkMass["UpperArm_mass"] = 0.023 * TotalMass
        linkMass["ForeArm_mass"] = 0.015 * TotalMass
        linkMass["Hand_mass"] = 0.0055 * TotalMass
        linkMass["UpperLeg_mass"] = 0.1345 * TotalMass
        linkMass["LowerLeg_mass"] = 0.0465 * TotalMass
        linkMass["Foot_mass"] = (0.011 * TotalMass) - ((0.011 * TotalMass) / 100)
        linkMass["Toe_mass"] = 0.011 * TotalMass / 100

    elif MODEL_TYPE == "DeLeva":
        # De Leva, et. al 1996 correction
        linkMass["Head_mass"] = 0.0487 * TotalMass
        linkMass["Neck_mass"] = 0.0194 * TotalMass
        linkMass["UpperTrunk_mass"] = 0.0523 * TotalMass
        linkMass["LowerTrunk_mass"] = 0.1549 * TotalMass
        linkMass["Shoulder_mass"] = 0.0523 * TotalMass
        linkMass["Pelvis_mass"] = 0.1183 * TotalMass
        linkMass["UpperArm_mass"] = 0.0263 * TotalMass
        linkMass["ForeArm_mass"] = 0.015 * TotalMass
        linkMass["Hand_mass"] = 0.0059 * TotalMass
        linkMass["UpperLeg_mass"] = 0.1447 * TotalMass
        linkMass["LowerLeg_mass"] = 0.0457 * TotalMass
        linkMass["Foot_mass"] = (0.0133 * TotalMass) - ((0.0133 * TotalMass) / 100)
        linkMass["Toe_mass"] = 0.0133 * TotalMass / 100

    else:
        raise ValueError("Invalid model type. Choose 'Dumas' or 'DeLeva'.")

    return linkMass
