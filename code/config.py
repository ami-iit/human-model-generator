# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_TYPE_MOVEMENT = "physio"  # "physio" or "random"
OPT_VISUALIZZATION_MOVEMENT = True  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = True  # 'True' or 'False

""" ANTHROPOMETRIC MEASUREMENTS"""

MODEL_TYPE = "DeLeva"  # "DeLeva" or "Dumas"

H = 1.70
m = 60

# some neck,trunk,arm and leg dimensions
linkDimensions = {
    "Neck_x": 0.095,
    "UpperTrunk_x": 0.175,
    "LowerTrunk_x": 0.175,
    "Pelvis_x": 0.175,
    "Shoulder_x": 0.06,
    "UpperArm_x": 0.06,
    "ForeArm_x": 0.055,
    "Hand_z": 0.025,
    "Hand_x": 0.072,
    "UpperLeg_x": 0.125,
    "LowerLeg_x": 0.09,
}
