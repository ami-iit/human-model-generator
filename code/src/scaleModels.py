# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

import numpy as np


def scaleLink(H, MODEL_TYPE, linkDimensions):
    # Links' length and width modification

    linkDimensions.update(
        {
            "Head_x": 0.13 * H,
            "Neck_z": 0.052 * H,
            "UpperArm_y": 0.186 * H,
            "ForeArm_y": 0.146 * H,
            "Hand_y": 0.108 * H,
            "UpperLeg_z": 0.245 * H,
            "LowerLeg_z": 0.246 * H,
            "Foot_z": 0.039 * H,
            "Foot_y": 0.055 * H,
            "Foot_x": 0.152 * H,
        }
    )
    if MODEL_TYPE == "Dumas":
        # Dumas, et. al 2007 & Dumas, et. al 2015 correction
        linkDimensions.update(
            {
                "UpperTrunk_z": 0.167 * H,
                "UpperTrunk_y": (0.259 * H) / 3,
                "Shoulder_x": linkDimensions["UpperArm_x"],
                "Shoulder_y": (0.259 * H) / 3,
                "LowerTrunk_z": 0.067 * H,
                "LowerTrunk_y": 0.174 * H,
                "Pelvis_z": 0.054 * H,
                "Pelvis_y": 0.191 * H,
            }
        )
    elif MODEL_TYPE == "DeLeva":
        ##De Leva, et. al 1996 correction
        linkDimensions.update(
            {
                "UpperTrunk_z": 0.11 * H,
                "UpperTrunk_y": (0.259 * H) / 3,
                "Shoulder_x": linkDimensions["UpperArm_x"],
                "Shoulder_y": (0.259 * H) / 3,
                "LowerTrunk_z": 0.1 * H,
                "LowerTrunk_y": 0.174 * H,
                "Pelvis_z": 0.078 * H,
                "Pelvis_y": 0.191 * H,
            }
        )

    linkDimensions.update(
        {
            "Toe_x": linkDimensions["Foot_x"] / 100,
            "Toe_y": linkDimensions["Foot_y"],
            "Toe_z": linkDimensions["Foot_z"],
        }
    )

    return linkDimensions


def scaleJoint(linkDimensions):
    # Joints' position modification

    # Pelvis - LowerTrunk
    jointPosition = {
        "jL5S1_z": linkDimensions["Pelvis_z"]
        + linkDimensions["UpperLeg_z"]
        + linkDimensions["LowerLeg_z"]
        + linkDimensions["Foot_z"],
        "jT9T8_z": linkDimensions["LowerTrunk_z"],  # LowerTrunk - UpperTrunk
        "jC7RightShoulder_y": -linkDimensions["UpperTrunk_y"] / 2,
        "jC7RightShoulder_z": (
            linkDimensions["UpperTrunk_z"] - linkDimensions["Shoulder_x"] / 2
        ),  # UpperTrunk - RightShoulder(Uppertrunk)
        "jC7LeftShoulder_y": linkDimensions["UpperTrunk_y"] / 2,
        "jC7LeftShoulder_z": (
            linkDimensions["UpperTrunk_z"] - linkDimensions["Shoulder_x"] / 2
        ),  # UpperTrunk - LeftShoulder(Uppertrunk)
        "jT1C7_z": linkDimensions["UpperTrunk_z"],  # UpperTrunk - Neck
        "jC1Head_z": linkDimensions["Neck_z"],  # UpperTrunk - Neck
        "jRightShoulder_y": -linkDimensions[
            "UpperTrunk_y"
        ],  # UpperTrunk - Right Shoulder
        "jRightElbow_y": -linkDimensions["UpperArm_y"],  # Right Elbow
        "jRightWrist_y": -linkDimensions["ForeArm_y"],  # Right Wrist
        "jRightHandCOM_y": -linkDimensions["Hand_y"] / 2,
        "jLeftShoulder_y": linkDimensions["UpperTrunk_y"],  # UpperTrunk - Left Shoulder
        "jLeftElbow_y": linkDimensions["UpperArm_y"],  # Left Elbow
        "jLeftWrist_y": linkDimensions["ForeArm_y"],  # Left Wrist
        "jLeftHandCOM_y": linkDimensions["Hand_y"] / 2,
        "jRightHip_y": -(
            (linkDimensions["Pelvis_y"] / 2) - (linkDimensions["UpperLeg_x"] / 2)
        ),  # Right Hip
        "jRightHip_z": (
            (
                linkDimensions["UpperLeg_z"]
                + linkDimensions["LowerLeg_z"]
                + linkDimensions["Foot_z"]
            )
        ),
        "jRightKnee_z": -linkDimensions["UpperLeg_z"],  # Right Knee
        "jRightAnkle_x": 0,  # Right Ankle
        "jRightAnkle_z": -linkDimensions["LowerLeg_z"],
        "jRightBallFoot_x": (
            linkDimensions["LowerLeg_x"] / 2
            + (abs(linkDimensions["LowerLeg_x"] - linkDimensions["Foot_x"]))
            + linkDimensions["Toe_x"] / 2
        ),  # Right Toe
        "jRightBallFoot_z": -linkDimensions["Foot_z"] / 2,
        "jLeftHip_y": (linkDimensions["Pelvis_y"] / 2)
        - (linkDimensions["UpperLeg_x"] / 2),  # Left Hip
        "jLeftHip_z": (
            (
                linkDimensions["UpperLeg_z"]
                + linkDimensions["LowerLeg_z"]
                + linkDimensions["Foot_z"]
            )
        ),
        "jLeftKnee_z": -linkDimensions["UpperLeg_z"],  # Left Knee
        "jLeftAnkle_x": 0,  # Left Ankle
        "jLeftAnkle_z": -linkDimensions["LowerLeg_z"],
        "jLeftBallFoot_x": (
            linkDimensions["LowerLeg_x"] / 2
            + (abs(linkDimensions["LowerLeg_x"] - linkDimensions["Foot_x"]))
            + linkDimensions["Toe_x"] / 2
        ),  # Left Toe
        "jLeftBallFoot_z": -linkDimensions["Foot_z"] / 2,
        "jRightBirken_x": 0.037,  # Fixed joint position based on shoes dimension
        "jRightBirken_z": -linkDimensions["Foot_z"] - 0.055,
        "jLeftBirken_x": 0.037,
        "jLeftBirken_z": -linkDimensions["Foot_z"] - 0.055,
    }

    return jointPosition


def scaleMuscleJoint(linkDimensions):

    pi = np.pi

    # Biceps
    jointMusclePosition = {
        "jRightBicBrac_RUA_x": (-1)
        * (linkDimensions["UpperArm_x"] / 2)
        * np.cos((pi / 2)),
        "jRightBicBrac_RUA_z": (linkDimensions["UpperArm_x"] / 2) * np.sin((pi / 2)),
        "jRightBicBrac_RFA_x": (-1) * (linkDimensions["ForeArm_x"] / 2) * np.cos((pi)),
        "jRightBicBrac_RFA_z": (linkDimensions["ForeArm_x"] / 2) * np.sin((pi / 2)),
        "jLeftBicBrac_LUA_x": (linkDimensions["UpperArm_x"] / 2) * np.cos((pi / 2)),
        "jLeftBicBrac_LUA_z": (linkDimensions["UpperArm_x"] / 2) * np.sin((pi / 2)),
        "jLeftBicBrac_LFA_x": (linkDimensions["ForeArm_x"] / 2) * np.cos((0)),
        "jLeftBicBrac_LFA_z": (linkDimensions["ForeArm_x"] / 2)
        * np.sin((0)),  # Triceps
        "jRightTricBrac_RUA_x": (-1) * (linkDimensions["UpperArm_x"] / 2) * np.cos((0)),
        "jRightTricBrac_RUA_z": (linkDimensions["UpperArm_x"] / 2) * np.sin((0)),
        "jRightTricBrac_RFA_x": (linkDimensions["ForeArm_x"] / 2) * np.cos((0)),
        "jRightTricBrac_RFA_z": (linkDimensions["ForeArm_x"] / 2) * np.sin((0)),
        "jLeftTricBrac_LUA_x": (-1) * (linkDimensions["UpperArm_x"] / 2) * np.cos((pi)),
        "jLeftTricBrac_LUA_z": (linkDimensions["UpperArm_x"] / 2) * np.sin((pi)),
        "jLeftTricBrac_LFA_x": (-1) * (linkDimensions["ForeArm_x"] / 2) * np.cos((pi)),
        "jLeftTricBrac_LFA_z": (linkDimensions["ForeArm_x"] / 2)
        * np.sin((pi)),  # Flexor carpi radialis
        "jRightFlexCarp_RFA_x": (-1) * (linkDimensions["ForeArm_x"] / 2) * np.cos((0)),
        "jRightFlexCarp_RFA_z": (linkDimensions["ForeArm_x"] / 2) * np.sin((0)),
        "jRightFlexCarp_RH_x": linkDimensions["Hand_x"] / 5,
        "jRightFlexCarp_RH_y": -linkDimensions["Hand_y"] / 2,
        "jRightFlexCarp_RH_z": linkDimensions["Hand_z"] / 2,
        "jLeftFlexCarp_LFA_x": (linkDimensions["ForeArm_x"] / 2) * np.cos((pi)),
        "jLeftFlexCarp_LFA_z": (linkDimensions["ForeArm_x"] / 2) * np.sin((pi)),
        "jLeftFlexCarp_LH_x": linkDimensions["Hand_x"] / 5,
        "jLeftFlexCarp_LH_y": linkDimensions["Hand_y"] / 2,
        "jLeftFlexCarp_LH_z": linkDimensions["Hand_z"] / 2,  # Extensor carpi radialis
        "jRightExtCarp_RFA_x": (-1) * (linkDimensions["ForeArm_x"] / 2) * np.cos((pi)),
        "jRightExtCarp_RFA_z": (linkDimensions["ForeArm_x"] / 2) * np.sin((pi)),
        "jRightExtCarp_RH_x": linkDimensions["Hand_x"] / 5,
        "jRightExtCarp_RH_y": -linkDimensions["Hand_y"] / 2,
        "jRightExtCarp_RH_z": -linkDimensions["Hand_z"] / 2,
        "jLeftExtCarp_LFA_x": (linkDimensions["ForeArm_x"] / 2) * np.cos((pi)),
        "jLeftExtCarp_LFA_z": (linkDimensions["ForeArm_x"] / 2) * np.sin((pi)),
        "jLeftExtCarp_LH_x": linkDimensions["Hand_x"] / 5,
        "jLeftExtCarp_LH_y": linkDimensions["Hand_y"] / 2,
        "jLeftExtCarp_LH_z": -linkDimensions["Hand_z"]
        / 2,  # Erector spinae longissimus
        "jRightErSpin_RUT_x": -linkDimensions["UpperTrunk_x"] / 2,
        "jRightErSpin_RUT_y": -linkDimensions["UpperTrunk_y"] / 2,
        "jRightErSpin_RUT_z": linkDimensions["UpperTrunk_z"],
        "jRightErSpin_RP_x": -linkDimensions["Pelvis_x"] / 2,
        "jLeftErSpin_LUT_x": -linkDimensions["UpperTrunk_x"] / 2,
        "jLeftErSpin_LUT_y": linkDimensions["UpperTrunk_y"] / 2,
        "jLeftErSpin_LUT_z": linkDimensions["UpperTrunk_z"],
        "jLeftErSpin_LP_x": -linkDimensions["Pelvis_x"] / 2,  # Rectus abdominis
        "jRightRecAbd_RUT_x": linkDimensions["UpperTrunk_x"] / 2,
        "jRightRecAbd_RUT_y": -linkDimensions["UpperTrunk_y"] / 2,
        "jRightRecAbd_RP_x": linkDimensions["Pelvis_x"] / 2,
        "jLeftRecAbd_LUT_x": linkDimensions["UpperTrunk_x"] / 2,
        "jLeftRecAbd_LUT_y": linkDimensions["UpperTrunk_y"] / 2,
        "jLeftRecAbd_LP_x": linkDimensions["Pelvis_x"] / 2,  # Biceps femoris
        "jRightBicFem_RUL_x": (linkDimensions["UpperLeg_x"] / 2) * np.sin((3 / 2 * pi)),
        "jRightBicFem_RUL_y": (
            (-1) * (linkDimensions["LowerLeg_x"] / 2) * np.cos((3 / 2 * pi))
        ),
        "jRightBicFem_RLL_x": (linkDimensions["LowerLeg_x"] / 2) * np.sin(0),
        "jRightBicFem_RLL_y": (-1) * (linkDimensions["LowerLeg_x"] / 2) * np.cos(0),
        "jLeftBicFem_LUL_x": (linkDimensions["UpperLeg_x"] / 2) * np.sin((3 / 2 * pi)),
        "jLeftBicFem_LUL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((3 / 2 * pi)),
        "jLeftBicFem_LLL_x": (linkDimensions["LowerLeg_x"] / 2) * np.sin(pi),
        "jLeftBicFem_LLL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos(pi),  # Rectus femoris
        "jRightRecFem_RP_x": linkDimensions["Pelvis_x"] / 2,
        "jRightRecFem_RP_y": -linkDimensions["Pelvis_y"] / 3,
        "jRightRecFem_RP_z": linkDimensions["Pelvis_z"] / 2,
        "jRightRecFem_RLL_x": (linkDimensions["LowerLeg_x"] / 2) * np.sin((pi / 2)),
        "jRightRecFem_RLL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((pi / 2)),
        "jLeftRecFem_LP_x": linkDimensions["Pelvis_x"] / 2,
        "jLeftRecFem_LP_y": linkDimensions["Pelvis_y"] / 3,
        "jLeftRecFem_LP_z": linkDimensions["Pelvis_z"] / 2,
        "jLeftRecFem_LLL_x": (linkDimensions["LowerLeg_x"] / 2) * np.sin((pi / 2)),
        "jLeftRecFem_LLL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((pi / 2)),  # Tibialis anterior
        "jRightTibAnt_RLL_x": (linkDimensions["LowerLeg_x"] / 2) * np.sin((pi / 2)),
        "jRightTibAnt_RLL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((pi / 2)),
        "jRightTibAnt_RF_x": linkDimensions["Foot_x"] / 2,
        "jRightTibAnt_RF_y": linkDimensions["Foot_y"] / 2,
        "jLeftTibAnt_LLL_x": (linkDimensions["LowerLeg_x"] / 2) * np.sin((pi / 2)),
        "jLeftTibAnt_LLL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((pi / 2)),
        "jLeftTibAnt_LF_x": linkDimensions["Foot_x"] / 2,
        "jLeftTibAnt_LF_y": -linkDimensions["Foot_y"] / 2,  # Gastrocnemius medialis
        "jRightGasMed_RUL_x": (linkDimensions["UpperLeg_x"] / 2) * np.sin((4 / 3 * pi)),
        "jRightGasMed_RUL_y": (
            (-1) * (linkDimensions["LowerLeg_x"] / 2) * np.cos((4 / 3 * pi))
        ),
        "jRightGasMed_RUL_z": -linkDimensions["UpperLeg_z"],
        "jRightGasMed_RF_z": -linkDimensions["Foot_z"] / 2,
        "jLeftGasMed_LUL_x": (linkDimensions["UpperLeg_x"] / 2) * np.sin((5 / 3 * pi)),
        "jLeftGasMed_LUL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((5 / 3 * pi)),
        "jLeftGasMed_LUL_z": -linkDimensions["UpperLeg_z"],
        "jLeftGasMed_LF_z": -linkDimensions["Foot_z"] / 2,  # Gastrocnemius lateralis
        "jRightGasLat_RUL_x": (linkDimensions["UpperLeg_x"] / 2) * np.sin((5 / 3 * pi)),
        "jRightGasLat_RUL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((5 / 3 * pi)),
        "jRightGasLat_RUL_z": -linkDimensions["UpperLeg_z"],
        "jRightGasLat_RF_z": -linkDimensions["Foot_z"] / 2,
        "jLeftGasLat_LUL_x": (linkDimensions["UpperLeg_x"] / 2) * np.sin((4 / 3 * pi)),
        "jLeftGasLat_LUL_y": (-1)
        * (linkDimensions["LowerLeg_x"] / 2)
        * np.cos((4 / 3 * pi)),
        "jLeftGasLat_LUL_z": -linkDimensions["UpperLeg_z"],
        "jLeftGasLat_LF_z": -linkDimensions["Foot_z"] / 2,
    }

    return jointMusclePosition


def scaleMass(TotalMass, MODEL_TYPE):

    if MODEL_TYPE == "Dumas":
        # Dumas, et. al 2007 & Dumas, et. al 2015 correction
        linkMass = {
            "Head_mass": 0.0479 * TotalMass,
            "Neck_mass": 0.0191 * TotalMass,
            "UpperTrunk_mass": 0.0945 * TotalMass,
            "LowerTrunk_mass": 0.035 * TotalMass,
            "Shoulder_mass": 0.0945 * TotalMass,
            "Pelvis_mass": 0.1435 * TotalMass,
            "UpperArm_mass": 0.023 * TotalMass,
            "ForeArm_mass": 0.015 * TotalMass,
            "Hand_mass": 0.0055 * TotalMass,
            "UpperLeg_mass": 0.1345 * TotalMass,
            "LowerLeg_mass": 0.0465 * TotalMass,
            "Foot_mass": (0.011 * TotalMass) - ((0.011 * TotalMass) / 100),
            "Toe_mass": 0.011 * TotalMass / 100,
        }

    elif MODEL_TYPE == "DeLeva":
        # De Leva, et. al 1996 correction
        linkMass = {
            "Head_mass": 0.0487 * TotalMass,
            "Neck_mass": 0.0194 * TotalMass,
            "UpperTrunk_mass": 0.0523 * TotalMass,
            "LowerTrunk_mass": 0.1549 * TotalMass,
            "Shoulder_mass": 0.0523 * TotalMass,
            "Pelvis_mass": 0.1183 * TotalMass,
            "UpperArm_mass": 0.0263 * TotalMass,
            "ForeArm_mass": 0.015 * TotalMass,
            "Hand_mass": 0.0059 * TotalMass,
            "UpperLeg_mass": 0.1447 * TotalMass,
            "LowerLeg_mass": 0.0457 * TotalMass,
            "Foot_mass": (0.0133 * TotalMass) - ((0.0133 * TotalMass) / 100),
            "Toe_mass": 0.0133 * TotalMass / 100,
        }

    else:
        raise ValueError("Invalid model type. Choose 'Dumas' or 'DeLeva'.")

    return linkMass
