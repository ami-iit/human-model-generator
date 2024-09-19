# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_TYPE_MOVEMENT = "random"  # "physio" or "random"
OPT_VISUALIZZATION_MOVEMENT = True  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = True  # 'True' or 'False

""" ANTHROPOMETRIC MEASUREMENTS"""

MODEL_TYPE = "DeLeva"  # "DeLeva" or "Dumas"

H = 1.85
m = 103


from src.humanLinksJoints import linkDimensions

# some neck,trunk,arm and leg dimensions

linkDimensions["Neck"]["X"] = linkDimensions["Neck"]["Y"] = 0.115
linkDimensions["UpperTrunk"]["X"] = 0.235
linkDimensions["LowerTrunk"]["X"] = 0.235
linkDimensions["Pelvis"]["X"] = 0.235
linkDimensions["Shoulder"]["X"] = linkDimensions["Shoulder"]["Z"] = 0.075
linkDimensions["UpperArm"]["X"] = linkDimensions["UpperArm"]["Z"] = 0.075
linkDimensions["ForeArm"]["X"] = linkDimensions["ForeArm"]["Z"] = 0.07
linkDimensions["Hand"]["Z"] = 0.035
linkDimensions["Hand"]["X"] = 0.08
linkDimensions["UpperLeg"]["X"] = linkDimensions["UpperLeg"]["Y"] = 0.155
linkDimensions["LowerLeg"]["X"] = linkDimensions["LowerLeg"]["Y"] = 0.125
