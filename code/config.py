# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""
import numpy as np

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_VISUALIZZATION_MODEL = True  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = False  # 'True' or 'False
OPT_VISUALIZATION_MESH = True  # 'True' or 'False
OPT_VISUALIZATION_MUSCLES = True  # 'True' or 'False
OPT_VISUALIZATION_SPINALCORD = True  # 'True' or 'False



OPT_COLOR_LINK_MESH = [0.9922, 0.8667, 0.7922, 1.0]
OPT_COLOR_MUSCLE_MESH = [0.9922, 0.8667, 0.7922, 1.0]
OPT_COLOR_SPINALCORD_MESH = [0.9922, 0.8667, 0.7922, 1.0]


""" ANTHROPOMETRIC MEASUREMENTS"""

H = 1.665
m = 59.0


# some neck,trunk,arm and leg dimensions in [m]
from src import linkDimensions

linkDimensions["Neck"]["X"] = linkDimensions["Neck"]["Y"] = 0.1003184713
linkDimensions["T8"]["X"] = linkDimensions["T12"]["X"] = linkDimensions["L3"]["X"] = linkDimensions["L5"]["X"] = 0.06
linkDimensions["Pelvis"]["X"] = 0.225
linkDimensions["Shoulder"]["Z"] = 0.115
linkDimensions["UpperArm"]["X"] = linkDimensions["UpperArm"]["Z"] = 0.0923566879
linkDimensions["ForeArm"]["X"] = linkDimensions["ForeArm"]["Z"] = 0.0700636942675159
linkDimensions["Hand"]["Z"] = 0.025
linkDimensions["Hand"]["X"] = 0.085
linkDimensions["UpperLeg"]["X"] = linkDimensions["UpperLeg"]["Y"] = 0.1560509554
linkDimensions["LowerLeg"]["X"] = linkDimensions["LowerLeg"]["Y"] = 0.1082802548
