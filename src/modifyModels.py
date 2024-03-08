
# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from applyScaling import*
from scaleModels import*
from setPaths import*
from urdfModifiers.utils import *

def modifyTemplate (H,TotalMass,Neck_x,UpperTrunk_x,LowerTrunk_x,Pelvis_x,Shoulder_x,UpperArm_x,ForeArm_x,Hand_x,Hand_z,UpperLeg_x,LowerLeg_x,Model,FileName,Control):

    """
    Modifies a template URDF model based on provided parameters.

    Parameters:
        H (float): Height of the model.
        TotalMass (float): Total mass of the model.
        Neck_x (float): Dimension of the neck along the X-axis.
        UpperTrunk_x (float): Dimension of the upper trunk along the X-axis.
        LowerTrunk_x (float): Dimension of the lower trunk along the X-axis.
        Pelvis_x (float): Dimension of the pelvis along the X-axis.
        Shoulder_x (float): Dimension of the shoulders along the X-axis.
        UpperArm_x (float): Dimension of the upper arms along the X-axis.
        ForeArm_x (float): Dimension of the forearms along the X-axis.
        Hand_x (float): Dimension of the hands along the X-axis.
        Hand_z (float): Dimension of the hands along the Z-axis.
        UpperLeg_x (float): Dimension of the upper legs along the X-axis.
        LowerLeg_x (float): Dimension of the lower legs along the X-axis.
        Model (str): Name of the model.
        FileName (str): Name of the file to be modified.
        Control (str): Control flag.

    Returns:
        None
    """

    urdf_path, output_file ,dummy_file = setPathLoadAndSave (FileName)

    ##############################################################################################
    # LINK
    ##############################################################################################
    Head_x,Neck_z,UpperTrunk_z,UpperTrunk_y,Shoulder_x,Shoulder_y,\
    LowerTrunk_z,LowerTrunk_y,Pelvis_z,Pelvis_y,UpperArm_y,ForeArm_y,Hand_y,UpperLeg_z,LowerLeg_z,\
    Foot_z,Foot_y,Foot_x = scaleLink ( H , UpperArm_x , Model ) 

    ##############################################################################################
    # MASS
    ##############################################################################################
    Head_mass,Neck_mass,UpperTrunk_mass,Shoulder_mass,LowerTrunk_mass,\
    Pelvis_mass,UpperArm_mass,ForeArm_mass,Hand_mass,UpperLeg_mass,LowerLeg_mass,Foot_mass= scaleMass ( TotalMass , Model )
    
    ##############################################################################################
    # JOINT
    ##############################################################################################
    jL5S1_z,jT9T8_z,jC7RightShoulder_y,jC7RightShoulder_z,jC7LeftShoulder_y,jC7LeftShoulder_z,jT1C7_z,jC1Head_z,\
    jRightShoulder_y,jRightShoulder_z,jRightElbow_y,jRightWrist_y,jRightHandCOM_y,jLeftShoulder_y,jLeftShoulder_z,\
    jLeftElbow_y,jLeftWrist_y,jLeftHandCOM_y,jRightHip_y,jRightKnee_z,jRightAnkle_z,jRightAnkle_x,jRightBallFoot_x,\
    jRightBallFoot_z,jRightHeel_z,jLeftHip_y,jLeftKnee_z,jLeftAnkle_z,jLeftAnkle_x,jLeftBallFoot_x,jLeftBallFoot_z,\
    jLeftHeel_z,jRightBirken_x,jRightBirken_z,jLeftBirken_x,jLeftBirken_z= scaleJoint (Neck_z,UpperTrunk_z,UpperTrunk_y,Shoulder_y,Shoulder_x,LowerTrunk_z,Pelvis_z,Pelvis_y,\
                                                                                        UpperArm_y,ForeArm_y,Hand_y, UpperLeg_z,UpperLeg_x,LowerLeg_z,LowerLeg_x,Foot_z,Foot_x)

    ##############################################################################################
    # MUSCLE FRAMES
    ##############################################################################################
    jRightBicBrac_RUA_x, jRightBicBrac_RUA_z, jRightBicBrac_RFA_x,jRightBicBrac_RFA_z,\
    jLeftBicBrac_LUA_x, jLeftBicBrac_LUA_z, jLeftBicBrac_LFA_x,jLeftBicBrac_LFA_z,\
    jRightTricBrac_RUA_x,jRightTricBrac_RUA_z, jRightTricBrac_RFA_x, jRightTricBrac_RFA_z,\
    jLeftTricBrac_LUA_x,jLeftTricBrac_LUA_z, jLeftTricBrac_LFA_x,jLeftTricBrac_LFA_z,\
    jRightFlexCarp_RFA_x,jRightFlexCarp_RFA_z,jRightFlexCarp_RH_x,jRightFlexCarp_RH_y,jRightFlexCarp_RH_z,\
    jLeftFlexCarp_LFA_x,jLeftFlexCarp_LFA_z,jLeftFlexCarp_LH_x,jLeftFlexCarp_LH_y,jLeftFlexCarp_LH_z,\
    jRightExtCarp_RFA_x,jRightExtCarp_RFA_z,jRightExtCarp_RH_x,jRightExtCarp_RH_y,jRightExtCarp_RH_z,\
    jLeftExtCarp_LFA_x,jLeftExtCarp_LFA_z,jLeftExtCarp_LH_x,jLeftExtCarp_LH_y,jLeftExtCarp_LH_z,\
    jRightErSpin_RUT_x, jRightErSpin_RUT_y,jRightErSpin_RUT_z,jRightErSpin_RP_x,jLeftErSpin_LUT_x,\
    jLeftErSpin_LUT_y,jLeftErSpin_LUT_z,jLeftErSpin_LP_x,\
    jRightRecAbd_RUT_x,jRightRecAbd_RUT_y,jRightRecAbd_RP_x,jLeftRecAbd_LUT_x,jLeftRecAbd_LUT_y,jLeftRecAbd_LP_x,\
    jRightBicFem_RUL_x, jRightBicFem_RUL_y, jRightBicFem_RLL_x, jRightBicFem_RLL_y, jLeftBicFem_LUL_x, jLeftBicFem_LUL_y,\
    jLeftBicFem_LLL_x,jLeftBicFem_LLL_y,jRightRecFem_RP_x,jRightRecFem_RP_y,jRightRecFem_RP_z,jRightRecFem_RLL_x,\
    jRightRecFem_RLL_y,jLeftRecFem_LP_x,jLeftRecFem_LP_y,jLeftRecFem_LP_z,jLeftRecFem_LLL_x,jLeftRecFem_LLL_y,\
    jRightTibAnt_RLL_x,jRightTibAnt_RLL_y,jRightTibAnt_RF_x,jRightTibAnt_RF_y,jLeftTibAnt_LLL_x,jLeftTibAnt_LLL_y,jLeftTibAnt_LF_x,\
    jLeftTibAnt_LF_y,jRightGasMed_RUL_x,jRightGasMed_RUL_y,jRightGasMed_RUL_z,jRightGasMed_RF_z,jLeftGasMed_LUL_x,jLeftGasMed_LUL_y,\
    jLeftGasMed_LUL_z,jLeftGasMed_LF_z,jRightGasLat_RUL_x,jRightGasLat_RUL_y,jRightGasLat_RUL_z,jRightGasLat_RF_z,jLeftGasLat_LUL_x,\
    jLeftGasLat_LUL_y,jLeftGasLat_LUL_z,jLeftGasLat_LF_z = scaleMuscleJoint (UpperArm_x,ForeArm_x,Hand_y,Hand_x,Hand_z,UpperTrunk_z,UpperTrunk_y,UpperTrunk_x,Pelvis_x,\
                                                                             Pelvis_y,Pelvis_z,UpperLeg_z,UpperLeg_x,LowerLeg_x,Foot_z,Foot_x,Foot_y)


    # Extract the <gazebo> tags from the urdf, as they collide with the library
    robot, gazebo_plugin_text = utils.load_robot_and_gazebo_plugins(urdf_path,dummy_file)

    ##############################################################################################
    # LINK MODIFICATION
    ##############################################################################################

    # PELVI
    setLinkLength ('Pelvis',Pelvis_z,None,Pelvis_z/2,"Z",'BOX',robot) 
    setLinkLength ('Pelvis',Pelvis_y,None,None,"Y",'BOX',robot) #width
    setLinkLength ('Pelvis',Pelvis_x,None,None,"X",'BOX',robot) #width
    setMassPercentage ('Pelvis',Pelvis_mass,'Z',robot)

    # LOWERTRUNK
    setLinkLength ('LowerTrunk',LowerTrunk_z,None,LowerTrunk_z/2,"Z",'BOX',robot) 
    setLinkLength ('LowerTrunk',LowerTrunk_y,None,None,"Y",'BOX',robot) #width
    setLinkLength ('LowerTrunk',LowerTrunk_x,None,None,"X",'BOX',robot) #width
    setMassPercentage ('LowerTrunk',LowerTrunk_mass,'Z',robot)

    # UPPERTRUNK
    setLinkLength ('UpperTrunk',UpperTrunk_z,None,UpperTrunk_z/2,"Z",'BOX',robot) 
    setLinkLength ('UpperTrunk',UpperTrunk_y,None,None,"Y",'BOX',robot) #width
    setLinkLength ('UpperTrunk',UpperTrunk_x,None,None,"X",'BOX',robot) #width
    setMassPercentage ('UpperTrunk',UpperTrunk_mass,'Z',robot)

    # RIGHTSHOULDER
    setLinkLength ('RightShoulder',None,Shoulder_x/2,None,"Z",'CYLINDER',robot) 
    setLinkLength ('RightShoulder',Shoulder_y,None,-Shoulder_y/2,"Y",'CYLINDER',robot) #width
    setMassPercentage ('RightShoulder',Shoulder_mass,'Z',robot)

    # LEFTSHOULDER
    setLinkLength ('LeftShoulder',None,Shoulder_x/2,None,"Z",'CYLINDER',robot) 
    setLinkLength ('LeftShoulder',Shoulder_y,None,Shoulder_y/2,"Y",'CYLINDER',robot) #width
    setMassPercentage ('LeftShoulder',Shoulder_mass,'Z',robot)
            
    # NECK
    setLinkLength ('Neck',Neck_z,Neck_x/2,Neck_z/2,"Z",'CYLINDER',robot) 
    setMassPercentage ('Neck',Neck_mass,'Z',robot)

    # HEAD
    setLinkLength ('Head',None,Head_x/2,Head_x/2,"Z",'SPHERE',robot) 
    setMassPercentage ('Head',Head_mass,'Z',robot)

    # RIGHT UPPERARM
    setLinkLength ('RightUpperArm',UpperArm_y,UpperArm_x/2,-UpperArm_y/2,"Y",'CYLINDER',robot) 
    setMassPercentage ('RightUpperArm',UpperArm_mass,'Z',robot)

    # RIGHT FOREARM
    setLinkLength ('RightForeArm',ForeArm_y,ForeArm_x/2,-ForeArm_y/2,"Y",'CYLINDER',robot) 
    setMassPercentage ('RightForeArm',ForeArm_mass,'Z',robot)

    # RIGHT HAND
    setLinkLength ('RightHand',Hand_y,None,-Hand_y/2,"Y",'BOX',robot) 
    setLinkLength ('RightHand',Hand_x,None,None,"X",'BOX',robot) 
    setLinkLength ('RightHand',Hand_z,None,None,"Z",'BOX',robot) 
    setMassPercentage ('RightHand',Hand_mass,'Z',robot)

    # LEFT UPPERARM
    setLinkLength ('LeftUpperArm',UpperArm_y,UpperArm_x/2,UpperArm_y/2,"Y",'CYLINDER',robot) 
    setMassPercentage ('LeftUpperArm',UpperArm_mass,'Z',robot)

    # LEFT FOREARM
    setLinkLength ('LeftForeArm',ForeArm_y,ForeArm_x/2,ForeArm_y/2,"Y",'CYLINDER',robot) 
    setMassPercentage ('LeftForeArm',ForeArm_mass,'Z',robot)

    # LEFT HAND
    setLinkLength ('LeftHand',Hand_y,None,Hand_y/2,"Y",'BOX',robot) 
    setLinkLength ('LeftHand',Hand_x,None,None,"X",'BOX',robot) 
    setLinkLength ('LeftHand',Hand_z,None,None,"Z",'BOX',robot) 
    setMassPercentage ('LeftHand',Hand_mass,'Z',robot)

    # RIGHT THIGH
    setLinkLength ('RightUpperLeg',UpperLeg_z,UpperLeg_x/2,-UpperLeg_z/2,"Z",'CYLINDER',robot) 
    setMassPercentage ('RightUpperLeg',UpperLeg_mass,'Z',robot)

    # RIGHT LOWERLEG
    setLinkLength ('RightLowerLeg',LowerLeg_z,LowerLeg_x/2,-LowerLeg_z/2,"Z",'CYLINDER',robot) 
    setMassPercentage ('RightLowerLeg',LowerLeg_mass,'Z',robot)

    # RIGHT FOOT
    setLinkLength ('RightFoot',Foot_z,None,-Foot_z/2,"Z",'BOX',robot) 
    setLinkLength ('RightFoot',Foot_y,None,None,"Y",'BOX',robot) #width
    setLinkLength ('RightFoot',Foot_x,None,Foot_x/2,"X",'BOX',robot) #deep
    setMassPercentage ('RightFoot',Foot_mass,'Z',robot)

    # LEFT THIGH
    setLinkLength ('LeftUpperLeg',UpperLeg_z,UpperLeg_x/2,-UpperLeg_z/2,"Z",'CYLINDER',robot) 
    setMassPercentage ('LeftUpperLeg',UpperLeg_mass,'Z',robot)

    # LEFT LOWERLEG
    setLinkLength ('LeftLowerLeg',LowerLeg_z,LowerLeg_x/2,-LowerLeg_z/2,"Z",'CYLINDER',robot) 
    setMassPercentage ('LeftLowerLeg',LowerLeg_mass,'Z',robot)

    # LEFT FOOT
    setLinkLength ('LeftFoot',Foot_z,None,-Foot_z/2,"Z",'BOX',robot) 
    setLinkLength ('LeftFoot',Foot_y,None,None,"Y",'BOX',robot) #width
    setLinkLength ('LeftFoot',Foot_x,None,Foot_x/2,"X",'BOX',robot) #deep
    setMassPercentage ('LeftFoot',Foot_mass,'Z',robot)

    ##############################################################################################
    # JOINT MODIFICATION
    ##############################################################################################

    # JOINT PELVI-LowerTrunk
    setJointPosition ('jL5S1_rotx',jL5S1_z,'Z',robot) 

    # JOINT LowerTrunk-UpperTrunk
    setJointPosition ('jT9T8_rotx',jT9T8_z,'Z',robot) 

    # JOINT UpperTrunk-RightShoulder
    setJointPosition ('jC7RightShoulder_rotx',jC7RightShoulder_z,'Z',robot) 
    setJointPosition ('jC7RightShoulder_rotx',jC7RightShoulder_y,'Y',robot)

    # JOINT UpperTrunk-LeftShoulder
    setJointPosition ('jC7LeftShoulder_rotx',jC7LeftShoulder_z,'Z',robot) 
    setJointPosition ('jC7LeftShoulder_rotx',jC7LeftShoulder_y,'Y',robot) 

    # JOINT UPPERTRUNK - NECK
    setJointPosition ('jT1C7_rotx',jT1C7_z,'Z',robot) 

    # JOINT NECK - HEAD
    setJointPosition ('jC1Head_rotx',jC1Head_z,'Z',robot) 

    # JOINT RIGHT SHOULDER
    setJointPosition ('jRightShoulder_rotx',jRightShoulder_y,'Y',robot) 
    
    # JOINT RIGHT ELBOW
    setJointPosition ('jRightElbow_roty',jRightElbow_y,'Y',robot) 

    # JOINT RIGHT WRIST
    setJointPosition ('jRightWrist_rotx',jRightWrist_y,'Y',robot) 

    # JOINT RIGHT HAND COM
    setJointPosition ('jRightHandCOM',jRightHandCOM_y,'Y',robot) 

    # JOINT LEFT SHOULDER
    setJointPosition ('jLeftShoulder_rotx',jLeftShoulder_y,'Y',robot) 

    # JOINT LEFT ELBOW
    setJointPosition ('jLeftElbow_roty',jLeftElbow_y,'Y',robot) 

    # JOINT LEFT WRIST
    setJointPosition ('jLeftWrist_rotx',jLeftWrist_y,'Y',robot) 

    # JOINT LEFT HAND COM
    setJointPosition ('jLeftHandCOM',jLeftHandCOM_y,'Y',robot) 

    # JOINT RIGHT HIP
    setJointPosition ('jRightHip_rotx',jRightHip_y,'Y',robot) 

    # JOINT RIGHT KNEE
    setJointPosition ('jRightKnee_roty',jRightKnee_z,'Z',robot) 

    # JOINT RIGHT ANKLE
    setJointPosition ('jRightAnkle_rotx',jRightAnkle_z,'Z',robot) 
    setJointPosition ('jRightAnkle_rotx',jRightAnkle_x,'X',robot) 

    # JOINT RIGHT TOE
    setJointPosition ('jRightBallFoot_roty',jRightBallFoot_z,'Z',robot) 
    setJointPosition ('jRightBallFoot_roty',jRightBallFoot_x,'X',robot) 

    # JOINT RIGHT HEEL
    setJointPosition ('jRightHeel_roty',jRightHeel_z,'Z',robot) 

    # JOINT RIGHT FT SENSOR
    setJointPosition ('jRightBirken_roty',jRightBirken_x,'X',robot) 
    setJointPosition ('jRightBirken_roty',jRightBirken_z,'Z',robot) 

    # JOINT LEFT HIP
    setJointPosition ('jLeftHip_rotx',jLeftHip_y,'Y',robot) 

    # JOINT LEFT KNEE
    setJointPosition ('jLeftKnee_roty',jLeftKnee_z,'Z',robot) 

    # JOINT LEFT ANKLE
    setJointPosition ('jLeftAnkle_rotx',jLeftAnkle_z,'Z',robot) 
    setJointPosition ('jLeftAnkle_rotx',jLeftAnkle_x,'X',robot) 

    # JOINT LEFT TOE
    setJointPosition ('jLeftBallFoot_roty',jLeftBallFoot_z,'Z',robot) 
    setJointPosition ('jLeftBallFoot_roty',jLeftBallFoot_x,'X',robot) 

    # JOINT LEFT HEEL
    setJointPosition ('jLeftHeel_roty',jLeftHeel_z,'Z',robot) 

    # JOINT RIGHT FT SENSOR
    setJointPosition ('jLeftBirken_roty',jLeftBirken_x,'X',robot) 
    setJointPosition ('jLeftBirken_roty',jLeftBirken_z,'Z',robot) 

    ##############################################################################################
    # MUSCLE FRAME
    ##############################################################################################

    # Biceps
    setJointPosition ('jRightBicBrac_RUA',jRightBicBrac_RUA_x,'X',robot) 
    setJointPosition ('jRightBicBrac_RUA',jRightBicBrac_RUA_z,'Z',robot) 
    setJointPosition ('jRightBicBrac_RFA',jRightBicBrac_RFA_x,'X',robot) 
    setJointPosition ('jRightBicBrac_RFA',jRightBicBrac_RFA_z,'Z',robot) 
    setJointPosition ('jLeftBicBrac_LUA',jLeftBicBrac_LUA_x,'X',robot) 
    setJointPosition ('jLeftBicBrac_LUA',jLeftBicBrac_LUA_z,'Z',robot) 
    setJointPosition ('jLeftBicBrac_LFA',jLeftBicBrac_LFA_x,'X',robot) 
    setJointPosition ('jLeftBicBrac_LFA',jLeftBicBrac_LFA_z,'Z',robot) 

    # Triceps
    setJointPosition ('jRightTricBrac_RUA',jRightTricBrac_RUA_x,'X',robot) 
    setJointPosition ('jRightTricBrac_RUA',jRightTricBrac_RUA_z,'Z',robot) 
    setJointPosition ('jRightTricBrac_RFA',jRightTricBrac_RFA_x,'X',robot) 
    setJointPosition ('jRightTricBrac_RFA',jRightTricBrac_RFA_z,'Z',robot) 
    setJointPosition ('jLeftTricBrac_LUA',jLeftTricBrac_LUA_x,'X',robot) 
    setJointPosition ('jLeftTricBrac_LUA',jLeftTricBrac_LUA_z,'Z',robot) 
    setJointPosition ('jLeftTricBrac_LFA',jLeftTricBrac_LFA_x,'X',robot) 
    setJointPosition ('jLeftTricBrac_LFA',jLeftTricBrac_LFA_z,'Z',robot) 

    # Flexor carpi radialis
    setJointPosition ('jRightFlexCarp_RFA',jRightFlexCarp_RFA_x,'X',robot) 
    setJointPosition ('jRightFlexCarp_RFA',jRightFlexCarp_RFA_z,'Z',robot) 
    setJointPosition ('jRightFlexCarp_RH',jRightFlexCarp_RH_x,'X',robot) 
    setJointPosition ('jRightFlexCarp_RH',jRightFlexCarp_RH_y,'Y',robot) 
    setJointPosition ('jRightFlexCarp_RH',jRightFlexCarp_RH_z,'Z',robot) 
    setJointPosition ('jLeftFlexCarp_LFA',jLeftFlexCarp_LFA_x,'X',robot) 
    setJointPosition ('jLeftFlexCarp_LFA',jLeftFlexCarp_LFA_z,'Z',robot) 
    setJointPosition ('jLeftFlexCarp_LH',jLeftFlexCarp_LH_x,'X',robot) 
    setJointPosition ('jLeftFlexCarp_LH',jLeftFlexCarp_LH_y,'Y',robot) 
    setJointPosition ('jLeftFlexCarp_LH',jLeftFlexCarp_LH_z,'Z',robot) 

    # Extensor carpi radialis
    setJointPosition ('jRightExtCarp_RFA',jRightExtCarp_RFA_x,'X',robot) 
    setJointPosition ('jRightExtCarp_RFA',jRightExtCarp_RFA_z,'Z',robot) 
    setJointPosition ('jRightExtCarp_RH',jRightExtCarp_RH_x,'X',robot) 
    setJointPosition ('jRightExtCarp_RH',jRightExtCarp_RH_y,'Y',robot) 
    setJointPosition ('jRightExtCarp_RH',jRightExtCarp_RH_z,'Z',robot) 
    setJointPosition ('jLeftExtCarp_LFA',jLeftExtCarp_LFA_x,'X',robot) 
    setJointPosition ('jLeftExtCarp_LFA',jLeftExtCarp_LFA_z,'Z',robot) 
    setJointPosition ('jLeftExtCarp_LH',jLeftExtCarp_LH_x,'X',robot) 
    setJointPosition ('jLeftExtCarp_LH',jLeftExtCarp_LH_y,'Y',robot) 
    setJointPosition ('jLeftExtCarp_LH',jLeftExtCarp_LH_z,'Z',robot) 

    # Erector spinae longissimus
    setJointPosition ('jRightErSpin_RUT',jRightErSpin_RUT_x,'X',robot) 
    setJointPosition ('jRightErSpin_RUT',jRightErSpin_RUT_y,'Y',robot) 
    setJointPosition ('jRightErSpin_RUT',jRightErSpin_RUT_z,'Z',robot) 
    setJointPosition ('jRightErSpin_RP',jRightErSpin_RP_x,'X',robot) 
    setJointPosition ('jLeftErSpin_LUT',jLeftErSpin_LUT_x,'X',robot) 
    setJointPosition ('jLeftErSpin_LUT',jLeftErSpin_LUT_y,'Y',robot) 
    setJointPosition ('jLeftErSpin_LUT',jLeftErSpin_LUT_z,'Z',robot) 
    setJointPosition ('jLeftErSpin_LP',jLeftErSpin_LP_x,'X',robot) 

    # Rectus abdominis
    setJointPosition ('jRightRecAbd_RUT',jRightRecAbd_RUT_x,'X',robot) 
    setJointPosition ('jRightRecAbd_RUT',jRightRecAbd_RUT_y,'Y',robot) 
    setJointPosition ('jRightRecAbd_RP',jRightRecAbd_RP_x,'X',robot)
    setJointPosition ('jLeftRecAbd_LUT',jLeftRecAbd_LUT_x,'X',robot) 
    setJointPosition ('jLeftRecAbd_LUT',jLeftRecAbd_LUT_y,'Y',robot) 
    setJointPosition ('jLeftRecAbd_LP',jLeftRecAbd_LP_x,'X',robot)

    # Biceps femoris
    setJointPosition ('jRightBicFem_RUL',jRightBicFem_RUL_x,'X',robot) 
    setJointPosition ('jRightBicFem_RUL',jRightBicFem_RUL_y,'Y',robot) 
    setJointPosition ('jRightBicFem_RLL',jRightBicFem_RLL_x,'X',robot)
    setJointPosition ('jRightBicFem_RLL',jRightBicFem_RLL_y,'Y',robot)
    setJointPosition ('jLeftBicFem_LUL',jLeftBicFem_LUL_x,'X',robot) 
    setJointPosition ('jLeftBicFem_LUL',jLeftBicFem_LUL_y,'Y',robot) 
    setJointPosition ('jLeftBicFem_LLL',jLeftBicFem_LLL_x,'X',robot)
    setJointPosition ('jLeftBicFem_LLL',jLeftBicFem_LLL_y,'Y',robot) 

    # Rectus femoris
    setJointPosition ('jRightRecFem_RP',jRightRecFem_RP_x,'X',robot) 
    setJointPosition ('jRightRecFem_RP',jRightRecFem_RP_y,'Y',robot) 
    setJointPosition ('jRightRecFem_RP',jRightRecFem_RP_z,'Z',robot)
    setJointPosition ('jRightRecFem_RLL',jRightRecFem_RLL_x,'X',robot)
    setJointPosition ('jRightRecFem_RLL',jRightRecFem_RLL_y,'Y',robot) 
    setJointPosition ('jLeftRecFem_LP',jLeftRecFem_LP_x,'X',robot) 
    setJointPosition ('jLeftRecFem_LP',jLeftRecFem_LP_y,'Y',robot) 
    setJointPosition ('jLeftRecFem_LP',jLeftRecFem_LP_z,'Z',robot)
    setJointPosition ('jLeftRecFem_LLL',jLeftRecFem_LLL_x,'X',robot)
    setJointPosition ('jLeftRecFem_LLL',jLeftRecFem_LLL_y,'Y',robot)

    # Tibialis anterior
    setJointPosition ('jRightTibAnt_RLL',jRightTibAnt_RLL_x,'X',robot) 
    setJointPosition ('jRightTibAnt_RLL',jRightTibAnt_RLL_y,'Y',robot) 
    setJointPosition ('jRightTibAnt_RF',jRightTibAnt_RF_x,'X',robot)
    setJointPosition ('jRightTibAnt_RF',jRightTibAnt_RF_y,'Y',robot)
    setJointPosition ('jLeftTibAnt_LLL',jLeftTibAnt_LLL_x,'X',robot) 
    setJointPosition ('jLeftTibAnt_LLL',jLeftTibAnt_LLL_y,'Y',robot) 
    setJointPosition ('jLeftTibAnt_LF',jLeftTibAnt_LF_x,'X',robot)
    setJointPosition ('jLeftTibAnt_LF',jLeftTibAnt_LF_y,'Y',robot)

    # Gastrocnemius medialis
    setJointPosition ('jRightGasMed_RUL',jRightGasMed_RUL_x,'X',robot) 
    setJointPosition ('jRightGasMed_RUL',jRightGasMed_RUL_y,'Y',robot) 
    setJointPosition ('jRightGasMed_RUL',jRightGasMed_RUL_z,'Z',robot)
    setJointPosition ('jRightGasMed_RF',jRightGasMed_RF_z,'Z',robot)
    setJointPosition ('jLeftGasMed_LUL',jLeftGasMed_LUL_x,'X',robot) 
    setJointPosition ('jLeftGasMed_LUL',jLeftGasMed_LUL_y,'Y',robot) 
    setJointPosition ('jLeftGasMed_LUL',jLeftGasMed_LUL_z,'Z',robot)
    setJointPosition ('jLeftGasMed_LF',jLeftGasMed_LF_z,'Z',robot)

    # Gastrocnemius lateralis
    setJointPosition ('jRightGasLat_RUL',jRightGasLat_RUL_x,'X',robot) 
    setJointPosition ('jRightGasLat_RUL',jRightGasLat_RUL_y,'Y',robot) 
    setJointPosition ('jRightGasLat_RUL',jRightGasLat_RUL_z,'Z',robot)
    setJointPosition ('jRightGasLat_RF',jRightGasLat_RF_z,'Z',robot)
    setJointPosition ('jLeftGasLat_LUL',jLeftGasLat_LUL_x,'X',robot) 
    setJointPosition ('jLeftGasLat_LUL',jLeftGasLat_LUL_y,'Y',robot) 
    setJointPosition ('jLeftGasLat_LUL',jLeftGasLat_LUL_z,'Z',robot)
    setJointPosition ('jLeftGasLat_LF',jLeftGasLat_LF_z,'Z',robot)

    # Write URDF to a new file, also adding back the previously removed <gazebo> tags                
    utils.write_urdf_to_file(robot, output_file, gazebo_plugin_text)

    if Control == "On":
        print("")
        print("")
        print("|====================|" + "====================|" )
        print("|               " + FileName )
        print("|--------------------|" + "--------------------|" )
        print("|Total body mass     |" + "       " +  str(round(Head_mass + Neck_mass + UpperTrunk_mass + Shoulder_mass +Shoulder_mass + LowerTrunk_mass + Pelvis_mass + (UpperArm_mass*2) + (ForeArm_mass*2) + (Hand_mass*2) + (UpperLeg_mass*2) + (LowerLeg_mass*2) + (Foot_mass*2),2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Total height        |" + "       " +  str(H) + " m")
        print("|--------------------|" + "--------------------|" )
        print("|Head                |" + " height: " +  str(round(Head_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(Head_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Neck                |" + " height: " +  str(round(Neck_z,2)) + " m")
        print("|                    |" + " width:  " +  str(round(Neck_x,2) ) + " m")
        print("|                    |" + " mass:   " +  str(round(Neck_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Upper trunk         |" + " height: " +  str(round(UpperTrunk_z,2)) + " m")
        print("|                    |" + " width:  " +  str(round(UpperTrunk_y + (Shoulder_y*2),2)) + " m")
        print("|                    |" + " depth:  " +  str(round(UpperTrunk_x,2)) + " m")       
        print("|                    |" + " mass:   " +  str(round(UpperTrunk_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Lower trunk         |" + " height: " +  str(round(LowerTrunk_z,2)) + " m")
        print("|                    |" + " width:  " +  str(round(LowerTrunk_y,2)) + " m")
        print("|                    |" + " depth:  " +  str(round(LowerTrunk_x,2)) + " m")           
        print("|                    |" + " mass:   " +  str(round(LowerTrunk_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Pelvis              |" + " height: " +  str(round(Pelvis_z,2)) + " m")
        print("|                    |" + " width:  " +  str(round(Pelvis_y,2)) + " m")
        print("|                    |" + " depth:  " +  str(round(Pelvis_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(Pelvis_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Upper arm           |" + " length: " +  str(round(UpperArm_y,2)) + " m")
        print("|                    |" + " width:  " +  str(round(UpperArm_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(UpperArm_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Fore arm            |" + " length: " +  str(round(ForeArm_y,2)) + " m")
        print("|                    |" + " width:  " +  str(round(ForeArm_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(ForeArm_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Hand                |" + " height: " +  str(round(Hand_z,2)) + " m")
        print("|                    |" + " length: " +  str(round(Hand_y,2)) + " m")
        print("|                    |" + " width:  " +  str(round(Hand_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(Hand_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Upper leg           |" + " length: " +  str(round(UpperLeg_z,2)) + " m")
        print("|                    |" + " width:  " +  str(round(UpperLeg_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(UpperLeg_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Lower leg           |" + " length: " +  str(round(LowerLeg_z,2)) + " m")
        print("|                    |" + " width:  " +  str(round(LowerLeg_x,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(LowerLeg_mass,2)) + " Kg")
        print("|--------------------|" + "--------------------|" )
        print("|Foot                |" + " height: " +  str(round(Foot_z,2)) + " m")
        print("|                    |" + " length: " +  str(round(Foot_x,2)) + " m")
        print("|                    |" + " width:  " +  str(round(Foot_y,2)) + " m")
        print("|                    |" + " mass:   " +  str(round(Foot_mass,2)) + " Kg")
        print("|====================|" + "====================|" )
        print("")
        print("")

