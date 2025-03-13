# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

# src/__init__.py

from modifyModels import *
from modifyModels import *
from scaleModels import *
from modelControl import *
from checkModel import *
from generateSyntheticData import *
from modifyMeshModels import *


""" HUMAN MODEL PART"""

linkDimensions = {
    "Neck": {"X": None, "Y": None, "Z": None},
    "T8": {"X": None, "Y": None, "Z": None},
    "T12": {"X": None, "Y": None, "Z": None},
    "L3": {"X": None, "Y": None, "Z": None},
    "L5": {"X": None, "Y": None, "Z": None},
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
    "Heel": {"X": None, "Y": None, "Z": None},
}

linkMass = {
    "Head_mass": None,
    "Neck_mass": None,
    "T8_mass": None,
    "T12_mass": None,
    "L3_mass": None,
    "L5_mass": None,
    "Shoulder_mass": None,
    "Pelvis_mass": None,
    "UpperArm_mass": None,
    "ForeArm_mass": None,
    "Hand_mass": None,
    "UpperLeg_mass": None,
    "LowerLeg_mass": None,
    "Foot_mass": None,
    "Toe_mass": None,
    "Heel_mass": None,
}

jointPosition = {
    "jL5S1": {"X": None, "Y": None, "Z": None},
    "jT9T8": {"X": None, "Y": None, "Z": None},
    "jL4L3": {"X": None, "Y": None, "Z": None},
    "jL1T12": {"X": None, "Y": None, "Z": None},
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
    "jRightHeel": {"X": None, "Y": None, "Z": None},
    "jLeftHip": {"X": None, "Y": None, "Z": None},
    "jLeftKnee": {"X": None, "Y": None, "Z": None},
    "jLeftAnkle": {"X": None, "Y": None, "Z": None},
    "jLeftBallFoot": {"X": None, "Y": None, "Z": None},
    "jLeftBirken": {"X": None, "Y": None, "Z": None},
    "jLeftHeel": {"X": None, "Y": None, "Z": None},
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

linkDimensions_norm = {
    "Neck": {"X": 0.1003184713, "Y": 0.1003184713, "Z": 0.08658},
    "T8": {"X": 0.06, "Y": 0.143745, "Z": 0.1380285},
    "T12": {"X": 0.06, "Y": 0.1, "Z": 0.087579},
    "L3": {"X": 0.06, "Y": 0.1, "Z": 0.074925},
    "L5": {"X": 0.06, "Y": 0.1, "Z": 0.0491175},
    "Pelvis": {"X": 0.225, "Y": 0.318015, "Z": 0.12987},
    "Shoulder": {"X": 0.0923566879, "Y": 0.143745, "Z": 0.115},
    "UpperArm": {"X": 0.0923566879, "Y": 0.30969, "Z": 0.0923566879},
    "ForeArm": {"X": 0.0700636942675159, "Y": 0.24309, "Z": 0.0700636942675159},
    "Hand": {"X": 0.085, "Y": 0.17982, "Z": 0.025},
    "UpperLeg": {"X": 0.1560509554, "Y": 0.1560509554, "Z": 0.407925},
    "LowerLeg": {"X": 0.1082802548, "Y": 0.1082802548, "Z": 0.40959},
    "Head": {"X": 0.21645, "Y": 0.21645, "Z": 0.21645},
    "Foot": {"X": 0.25308, "Y": 0.091575, "Z": 0.064935},
    "Toe": {"X": 0.0025308, "Y": 0.091575, "Z": 0.064935},
    "Heel": {"X": 0.0025308, "Y": 0.091575, "Z": 0.064935},
}

meshLinksName = [
    "Head",
    "LeftFoot",
    "LeftForeArm",
    "LeftHand",
    "LeftLowerLeg",
    "LeftShoulder",
    "LeftToe",
    "LeftHeel",
    "LeftUpperArm",
    "LeftUpperLeg",
    "Neck",
    "Pelvis",
    "RightFoot",
    "RightForeArm",
    "RightHand",
    "RightLowerLeg",
    "RightShoulder",
    "RightToe",
    "RightHeel",
    "RightUpperArm",
    "RightUpperLeg",
    "T8",
    "T12",
    "L3",
    "L5",
]

meshSpinalCordName = [
    "Neck_SpinalCord",
    "T8_SpinalCord",
    "T12_SpinalCord",
    "L3_SpinalCord",
    "L5_SpinalCord",
    "Pelvis_SpinalCord",
]

meshMusclesName = [
    "LeftUpperArm_LeftBicBrac",
    "LeftUpperArm_LeftTricBrac",
    "LeftForeArm_LeftExtCarp",
    "LeftForeArm_LeftFlexCarp",
    "LeftUpperLeg_LeftBicFem",
    "LeftUpperLeg_LeftRecFem",
    "LeftLowerLeg_LeftGasLat",
    "LeftLowerLeg_LeftGasMed",
    "LeftLowerLeg_LeftTibAnt",
    "T8_LeftErcSpin",
    "T12_LeftErcSpin",
    "L3_LeftErcSpin",
    "L5_LeftErcSpin",
    "T12_LeftRecAbd",
    "L3_LeftRecAbd",
    "L5_LeftRecAbd",
    "T8_RightErcSpin",
    "T12_RightErcSpin",
    "L3_RightErcSpin",
    "L5_RightErcSpin",
    "T12_RightRecAbd",
    "L3_RightRecAbd",
    "L5_RightRecAbd",
    "Pelvis_LeftErcSpin",
    "Pelvis_LeftRecAbd",
    "Pelvis_RightErcSpin",
    "Pelvis_RightRecAbd",
    "RightUpperArm_RightBicBrac",
    "RightUpperArm_RightTricBrac",
    "RightForeArm_RightExtCarp",
    "RightForeArm_RightFlexCarp",
    "RightUpperLeg_RightBicFem",
    "RightUpperLeg_RightRecFem",
    "RightLowerLeg_RightGasLat",
    "RightLowerLeg_RightGasMed",
    "RightLowerLeg_RightTibAnt",
]

map_link_to_muscles = {
    "Head": [],
    "LeftFoot": [],
    "LeftForeArm": ["LeftForeArm_LeftFlexCarp", "LeftForeArm_LeftExtCarp"],
    "LeftHand": [],
    "LeftLowerLeg": ["LeftLowerLeg_LeftTibAnt", "LeftLowerLeg_LeftGasMed", "LeftLowerLeg_LeftGasLat"],
    "LeftShoulder": [],
    "LeftToe": [],
    "LEftHeel": [],
    "LeftUpperArm": ["LeftUpperArm_LeftTricBrac", "LeftUpperArm_LeftBicBrac"],
    "LeftUpperLeg": ["LeftUpperLeg_LeftRecFem", "LeftUpperLeg_LeftBicFem"],
    "T8": [
        "T8_LeftErcSpin",
        "T8_RightErcSpin",
    ],
    "T12": [
        "T12_LeftErcSpin",
        "T12_LeftRecAbd",
        "T12_RightErcSpin",
        "T12_RightRecAbd",
    ],
    "L3": [
        "L3_LeftErcSpin",
        "L3_LeftRecAbd",
        "L3_RightErcSpin",
        "L3_RightRecAbd",
    ],
    "L5": [
        "L5_LeftErcSpin",
        "L5_LeftRecAbd",
        "L5_RightErcSpin",
        "L5_RightRecAbd",
    ],
    "Neck": [],
    "Pelvis": [
        "Pelvis_RightRecAbd",
        "Pelvis_RightErcSpin",
        "Pelvis_LeftRecAbd",
        "Pelvis_LeftErcSpin",
    ],
    "RightFoot": [],
    "RightForeArm": ["RightForeArm_RightFlexCarp", "RightForeArm_RightExtCarp"],
    "RightHand": [],
    "RightLowerLeg": ["RightLowerLeg_RightTibAnt", "RightLowerLeg_RightGasMed", "RightLowerLeg_RightGasLat"],
    "RightShoulder": [],
    "RightToe": [],
    "RightHeel": [],
    "RightUpperArm": ["RightUpperArm_RightTricBrac", "RightUpperArm_RightBicBrac"],
    "RightUpperLeg": ["RightUpperLeg_RightRecFem", "RightUpperLeg_RightBicFem"],
}

mesh_name_mapping = {
    "Head": "Head",
    "LeftFoot": "Foot",
    "RightFoot": "Foot",
    "LeftForeArm": "ForeArm",
    "RightForeArm": "ForeArm",
    "LeftHand": "Hand",
    "RightHand": "Hand",
    "LeftLowerLeg": "LowerLeg",
    "RightLowerLeg": "LowerLeg",
    "LeftShoulder": "Shoulder",
    "RightShoulder": "Shoulder",
    "LeftToe": "Toe",
    "LeftHeel": "Heel",
    "RightToe": "Toe",
    "RightHeel": "Heel",
    "LeftUpperArm": "UpperArm",
    "RightUpperArm": "UpperArm",
    "LeftUpperLeg": "UpperLeg",
    "RightUpperLeg": "UpperLeg",
    "Neck": "Neck",
    "Pelvis": "Pelvis",
    "T8": "T8",
    "T12": "T12",
    "L3": "L3",
    "L5": "L5",
}

map_link_to_spinal_cord = {
    "Neck": "Neck_SpinalCord",
    "T8": "T8_SpinalCord",
    "T12": "T12_SpinalCord",
    "L3": "L3_SpinalCord",
    "L5": "L5_SpinalCord",
    "Pelvis": "Pelvis_SpinalCord",
}
