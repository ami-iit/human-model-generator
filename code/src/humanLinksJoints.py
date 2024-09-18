# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause


""" HUMAN MODEL PART"""

linkDimensions = {
    "Neck": {"X": None, "Y": None, "Z": None},
    "UpperTrunk": {"X": None, "Y": None, "Z": None},
    "LowerTrunk": {"X": None, "Y": None, "Z": None},
    "Pelvis": {"X": None, "Y": None, "Z": None},
    "Shoulder": {"X": None, "Y": None, "Z": None},
    "UpperArm": {"X": None, "Y": None, "Z": None},
    "ForeArm": {"X": None, "Y": None, "Z": None},
    "Hand": {"X": None, "Y": None, "Z": None},
    "UpperLeg": {"X": None, "Y": None, "Z": None},
    "LowerLeg": {"X": None, "Y": None, "Z": None},
    "Head": {"X": None, "Y": None, "Z": None},
    "Foot": {"X": None, "Y": None, "Z": None},
    "Toe": {"X": None, "Y": None, "Z": None},
}

linkMass = {
    "Head_mass": None,
    "Neck_mass": None,
    "UpperTrunk_mass": None,
    "LowerTrunk_mass": None,
    "Shoulder_mass": None,
    "Pelvis_mass": None,
    "UpperArm_mass": None,
    "ForeArm_mass": None,
    "Hand_mass": None,
    "UpperLeg_mass": None,
    "LowerLeg_mass": None,
    "Foot_mass": None,
    "Toe_mass": None,
}


jointPosition = {
    "jL5S1": {"X": None, "Y": None, "Z": None},
    "jT9T8": {"X": None, "Y": None, "Z": None},
    "jC7RightShoulder": {"X": None, "Y": None, "Z": None},
    "jC7LeftShoulder": {"X": None, "Y": None, "Z": None},
    "jT1C7": {"X": None, "Y": None, "Z": None},
    "jC1Head": {"X": None, "Y": None, "Z": None},
    "jRightShoulder": {"X": None, "Y": None, "Z": None},
    "jRightElbow": {"X": None, "Y": None, "Z": None},
    "jRightWrist": {"X": None, "Y": None, "Z": None},
    "jRightHandCOM": {"X": None, "Y": None, "Z": None},
    "jLeftShoulder": {"X": None, "Y": None, "Z": None},
    "jLeftElbow": {"X": None, "Y": None, "Z": None},
    "jLeftWrist": {"X": None, "Y": None, "Z": None},
    "jLeftHandCOM": {"X": None, "Y": None, "Z": None},
    "jRightHip": {"X": None, "Y": None, "Z": None},
    "jRightKnee": {"X": None, "Y": None, "Z": None},
    "jRightAnkle": {"X": None, "Y": None, "Z": None},
    "jRightBallFoot": {"X": None, "Y": None, "Z": None},
    "jRightBirken": {"X": None, "Y": None, "Z": None},
    "jLeftHip": {"X": None, "Y": None, "Z": None},
    "jLeftKnee": {"X": None, "Y": None, "Z": None},
    "jLeftAnkle": {"X": None, "Y": None, "Z": None},
    "jLeftBallFoot": {"X": None, "Y": None, "Z": None},
    "jLeftBirken": {"X": None, "Y": None, "Z": None},
}

jointMusclePosition = {
    # Biceps
    "jRightBicBrac_RUA": {"X": None, "Y": None, "Z": None},
    "jRightBicBrac_RFA": {"X": None, "Y": None, "Z": None},
    "jLeftBicBrac_LUA": {"X": None, "Y": None, "Z": None},
    "jLeftBicBrac_LFA": {"X": None, "Y": None, "Z": None},
    # Triceps
    "jRightTricBrac_RUA": {"X": None, "Y": None, "Z": None},
    "jRightTricBrac_RFA": {"X": None, "Y": None, "Z": None},
    "jLeftTricBrac_LUA": {"X": None, "Y": None, "Z": None},
    "jLeftTricBrac_LFA": {"X": None, "Y": None, "Z": None},
    # Flexor carpi radialis
    "jRightFlexCarp_RFA": {"X": None, "Y": None, "Z": None},
    "jRightFlexCarp_RH": {"X": None, "Y": None, "Z": None},
    "jLeftFlexCarp_LFA": {"X": None, "Y": None, "Z": None},
    "jLeftFlexCarp_LH": {"X": None, "Y": None, "Z": None},
    # Extensor carpi radialis
    "jRightExtCarp_RFA": {"X": None, "Y": None, "Z": None},
    "jRightExtCarp_RH": {"X": None, "Y": None, "Z": None},
    "jLeftExtCarp_LFA": {"X": None, "Y": None, "Z": None},
    "jLeftExtCarp_LH": {"X": None, "Y": None, "Z": None},
    # Erector spinae longissimus
    "jRightErSpin_RUT": {"X": None, "Y": None, "Z": None},
    "jRightErSpin_RP": {"X": None, "Y": None, "Z": None},
    "jLeftErSpin_LUT": {"X": None, "Y": None, "Z": None},
    "jLeftErSpin_LP": {"X": None, "Y": None, "Z": None},
    # Rectus abdominis
    "jRightRecAbd_RUT": {"X": None, "Y": None, "Z": None},
    "jRightRecAbd_RP": {"X": None, "Y": None, "Z": None},
    "jLeftRecAbd_LUT": {"X": None, "Y": None, "Z": None},
    "jLeftRecAbd_LP": {"X": None, "Y": None, "Z": None},
    # Biceps femoris
    "jRightBicFem_RUL": {"X": None, "Y": None, "Z": None},
    "jRightBicFem_RLL": {"X": None, "Y": None, "Z": None},
    "jLeftBicFem_LUL": {"X": None, "Y": None, "Z": None},
    "jLeftBicFem_LLL": {"X": None, "Y": None, "Z": None},
    # Rectus femoris
    "jRightRecFem_RP": {"X": None, "Y": None, "Z": None},
    "jRightRecFem_RLL": {"X": None, "Y": None, "Z": None},
    "jLeftRecFem_LP": {"X": None, "Y": None, "Z": None},
    "jLeftRecFem_LLL": {"X": None, "Y": None, "Z": None},
    # Tibialis anterior
    "jRightTibAnt_RLL": {"X": None, "Y": None, "Z": None},
    "jRightTibAnt_RF": {"X": None, "Y": None, "Z": None},
    "jLeftTibAnt_LLL": {"X": None, "Y": None, "Z": None},
    "jLeftTibAnt_LF": {"X": None, "Y": None, "Z": None},
    # Gastrocnemius medialis
    "jRightGasMed_RUL": {"X": None, "Y": None, "Z": None},
    "jRightGasMed_RF": {"X": None, "Y": None, "Z": None},
    "jLeftGasMed_LUL": {"X": None, "Y": None, "Z": None},
    "jLeftGasMed_LF": {"X": None, "Y": None, "Z": None},
    # Gastrocnemius lateralis
    "jRightGasLat_RUL": {"X": None, "Y": None, "Z": None},
    "jRightGasLat_RF": {"X": None, "Y": None, "Z": None},
    "jLeftGasLat_LUL": {"X": None, "Y": None, "Z": None},
    "jLeftGasLat_LF": {"X": None, "Y": None, "Z": None},
}
