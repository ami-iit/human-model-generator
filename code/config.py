# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_TYPE_MOVEMENT = "physio"  # "physio" or "random"
OPT_VISUALIZZATION_MOVEMENT = False  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = False  # 'True' or 'False

""" ANTHROPOMETRIC MEASUREMENTS"""

MODEL_TYPE = "Dumas"  # "DeLeva" or "Dumas"

H = 1.75
m = 68.5

# some neck,trunk,arm and leg dimensions
linkDimensions = {
    "Neck_x": 0.11,
    "UpperTrunk_x": 0.18,
    "LowerTrunk_x": 0.18,
    "Pelvis_x": 0.18,
    "Shoulder_x": 0.06,
    "UpperArm_x": 0.06,
    "ForeArm_x": 0.06,
    "Hand_z": 0.04,
    "Hand_x": 0.1,
    "UpperLeg_x": 0.115,
    "LowerLeg_x": 0.09,
}
