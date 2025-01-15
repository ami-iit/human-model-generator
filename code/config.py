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

H = 1.65
m = 78.0


# some neck,trunk,arm and leg dimensions in [m]
from src import linkDimensions

linkDimensions["Neck"]["X"] = linkDimensions["Neck"]["Y"] = 0.105
linkDimensions["UpperTrunk"]["X"] = 0.21
linkDimensions["LowerTrunk"]["X"] = 0.21
linkDimensions["Pelvis"]["X"] = 0.21
linkDimensions["Shoulder"]["X"] = linkDimensions["Shoulder"]["Z"] = 0.0775
linkDimensions["UpperArm"]["X"] = linkDimensions["UpperArm"]["Z"] = 0.0775
linkDimensions["ForeArm"]["X"] = linkDimensions["ForeArm"]["Z"] = 0.0675
linkDimensions["Hand"]["Z"] = 0.0275
linkDimensions["Hand"]["X"] = 0.075
linkDimensions["UpperLeg"]["X"] = linkDimensions["UpperLeg"]["Y"] = 0.14
linkDimensions["LowerLeg"]["X"] = linkDimensions["LowerLeg"]["Y"] = 0.105
