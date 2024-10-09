# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""
import numpy as np

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_VISUALIZZATION_MODEL = True  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = False  # 'True' or 'False


OPT_COLOR_LINK_MESH = [0.9922, 0.8667, 0.7922, 1.0]
OPT_COLOR_MUSCLE_MESH = [0.9922, 0.8667, 0.7922, 1.0]


""" ANTHROPOMETRIC MEASUREMENTS"""

H = 1.75
m = 68.5


# some neck,trunk,arm and leg dimensions in [m]
from src import linkDimensions

linkDimensions["Neck"]["X"] = linkDimensions["Neck"]["Y"] = 0.11
linkDimensions["UpperTrunk"]["X"] = 0.18
linkDimensions["LowerTrunk"]["X"] = 0.18
linkDimensions["Pelvis"]["X"] = 0.18
linkDimensions["Shoulder"]["X"] = linkDimensions["Shoulder"]["Z"] = 0.06
linkDimensions["UpperArm"]["X"] = linkDimensions["UpperArm"]["Z"] = 0.06
linkDimensions["ForeArm"]["X"] = linkDimensions["ForeArm"]["Z"] = 0.06
linkDimensions["Hand"]["Z"] = 0.04
linkDimensions["Hand"]["X"] = 0.08
linkDimensions["UpperLeg"]["X"] = linkDimensions["UpperLeg"]["Y"] = 0.115
linkDimensions["LowerLeg"]["X"] = linkDimensions["LowerLeg"]["Y"] = 0.09
