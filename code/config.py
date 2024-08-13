# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""

OPT_CHECK_CONSISTENCY_MODEL = False  # 'True' or 'False
OPT_TYPE_MOVEMENT = "random"  # "physio" or "random"
OPT_VISUALIZZATION_MOVEMENT = False  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = False  # 'True' or 'False

""" ANTHROPOMETRIC MEASUREMENTS"""

MODEL_TYPE = "DeLeva"  # "DeLeva" or "Dumas"

H = 1.65
m = 96

# some neck,trunk,arm and leg dimensions
linkDimensions = {
    "Neck_x": 0.13,
    "UpperTrunk_x": 0.30,
    "LowerTrunk_x": 0.30,
    "Pelvis_x": 0.30,
    "Shoulder_x": 0.09,
    "UpperArm_x": 0.09,
    "ForeArm_x": 0.09,
    "Hand_z": 0.045,
    "Hand_x": 0.08,
    "UpperLeg_x": 0.15,
    "LowerLeg_x": 0.115,
}
