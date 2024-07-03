# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_TYPE_MOVEMENT = "physio"  # "physio" or "random"
OPT_VISUALIZZATION_MOVEMENT = True  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = True  # 'True' or 'False

""" ANTHROPOMETRIC MEASUREMENTS"""

MODEL_TYPE = "Dumas"  # "DeLeva" or "Dumas"

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
