from AutomaticScaling import*
from Parameter import*
from SetPath import*

Model = 'Dumas'
Geometry = "Box"#Cylinder
H=1.8
m=105

urdf_path, output_file ,dummy_file = SetPathLoadAndSave (Geometry)

Head_L,Neck_L,Neck_W,UpperTrunk_Middle_L,UpperTrunk_Middle_W,UpperTrunk_Right_L,UpperTrunk_Right_W,\
    UpperTrunk_Left_L,UpperTrunk_Left_W,MiddleTrunk_L,MiddleTrunk_W,Pelvi_L,Pelvi_W,\
    Upper_Arm_L,Upper_Arm_W,Fore_Arm_L,Fore_Arm_W,Hand_L,\
    Thigh_L,Thigh_W,LowerLimb_L,LowerLimb_W,Foot_H,Foot_W,Foot_L,J_Pelvi_MiddleTrunk_Z,J_MiddleTrunk_UpperTrunk_Middle_Z,\
    J_UpperTrunk_Middle_UpperTrunk_Right_Y,J_UpperTrunk_Middle_UpperTrunk_Right_Z,J_UpperTrunk_Middle_UpperTrunk_Left_Y,J_UpperTrunk_Middle_UpperTrunk_Left_Z,\
    J_UpperTrunk_Middle_Neck,J_Neck_Head,J_Right_Shoulder_Y,J_Right_Shoulder_Z,J_Right_Elbow_Y,J_Right_Wrist_Y,\
    J_Left_Shoulder_Y,J_Left_Shoulder_Z,J_Left_Elbow_Y,J_Left_Wrist_Y,J_Right_Hip_Y,J_Right_Knee_Z,J_Right_Ankle_Z,J_Left_Hip_Y,\
    J_Left_Knee_Z,J_Left_Ankle_Z = ScalingAnthroPar ( H , Model , Geometry ) 


Head_m,Neck_m,UpperTrunk_Middle_m,UpperTrunk_Right_m,UpperTrunk_Left_m,MiddleTrunk_m,\
    Pelvi_m,Upper_Arm_m,Fore_Arm_m,Hand_m,Thigh_m,LowerLimb_m,Foot_m = ScalingMassPar ( m , Model )

# Extract the <gazebo> tags from the urdf, as they collide with the library
robot, gazebo_plugin_text = utils.load_robot_and_gazebo_plugins(urdf_path,dummy_file)

##############################################################################################
# LINK
##############################################################################################

##PELVI
Scaling_lenght ('Pelvis',Pelvi_L,None,Pelvi_L/2,"Z",'BOX',robot) #length
Scaling_lenght ('Pelvis',Pelvi_W,None,None,"Y",'BOX',robot) #width
Scaling_Percentage_Mass ('Pelvis',Pelvi_m,'Z',robot)

##MIDDLETRUNK
Scaling_lenght ('MiddleTrunk',MiddleTrunk_L,None,MiddleTrunk_L/2,"Z",'BOX',robot) #length
Scaling_lenght ('MiddleTrunk',MiddleTrunk_W,None,None,"Y",'BOX',robot) #width
Scaling_Percentage_Mass ('MiddleTrunk',MiddleTrunk_m,'Z',robot)

##UPPERTRUNK_MIDDLE
Scaling_lenght ('UpperTrunk_Middle',UpperTrunk_Middle_L,None,UpperTrunk_Middle_L/2,"Z",'BOX',robot) #length
Scaling_lenght ('UpperTrunk_Middle',UpperTrunk_Middle_W,None,None,"Y",'BOX',robot) #width
Scaling_Percentage_Mass ('UpperTrunk_Middle',UpperTrunk_Middle_m,'Z',robot)

match Geometry:
        
    case 'Box':
        #Box
        ##UPPERTRUNK_RIGHT
        Scaling_lenght ('UpperTrunk_Right',UpperTrunk_Right_L,None,None,"Z",'BOX',robot) #length
        Scaling_lenght ('UpperTrunk_Right',UpperTrunk_Right_W,None,-UpperTrunk_Right_W/2,"Y",'BOX',robot) #width
        Scaling_Percentage_Mass ('UpperTrunk_Right',UpperTrunk_Right_m,'Z',robot)
        ##UPPERTRUNK_LEFT
        Scaling_lenght ('UpperTrunk_Left',UpperTrunk_Left_L,None,None,"Z",'BOX',robot) #length
        Scaling_lenght ('UpperTrunk_Left',UpperTrunk_Left_W,None,UpperTrunk_Left_W/2,"Y",'BOX',robot) #width
        Scaling_Percentage_Mass ('UpperTrunk_Left',UpperTrunk_Left_m,'Z',robot)
    case 'Cylinder':
        #Cylinder
        ##UPPERTRUNK_RIGHT
        Scaling_lenght ('UpperTrunk_Right',None,UpperTrunk_Right_L,None,"Z",'CYLINDER',robot) #length
        Scaling_lenght ('UpperTrunk_Right',UpperTrunk_Right_W,None,-UpperTrunk_Right_W/2,"Y",'CYLINDER',robot) #width
        Scaling_Percentage_Mass ('UpperTrunk_Left',UpperTrunk_Left_m,'Z',robot)
        ##UPPERTRUNK_LEFT
        Scaling_lenght ('UpperTrunk_Left',None,UpperTrunk_Left_L,None,"Z",'CYLINDER',robot) #length
        Scaling_lenght ('UpperTrunk_Left',UpperTrunk_Left_W,None,UpperTrunk_Left_W/2,"Y",'CYLINDER',robot) #width
        Scaling_Percentage_Mass ('UpperTrunk_Left',UpperTrunk_Left_m,'Z',robot)
        





##NECK
Scaling_lenght ('Neck',Neck_L,Neck_W,Neck_L/2,"Z",'CYLINDER',robot) 
Scaling_Percentage_Mass ('Neck',Neck_m,'Z',robot)
##HEAD
Scaling_lenght ('Head',None,Head_L/2,Head_L/2,"Z",'SPHERE',robot) #length
Scaling_Percentage_Mass ('Head',Head_m,'Z',robot)


##RIGHT UPPERARM
Scaling_lenght ('RightUpperArm',Upper_Arm_L,Upper_Arm_W,-Upper_Arm_L/2,"Y",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('RightUpperArm',Upper_Arm_m,'Z',robot)
##RIGHT FOREARM
Scaling_lenght ('RightForeArm',Fore_Arm_L,Fore_Arm_W,-Fore_Arm_L/2,"Y",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('RightForeArm',Fore_Arm_m,'Z',robot)
##RIGHT HAND
Scaling_lenght ('RightHand',Hand_L,None,-Hand_L/2,"Y",'BOX',robot) #length
Scaling_Percentage_Mass ('RightHand',Hand_m,'Z',robot)

##LEFT UPPERARM
Scaling_lenght ('LeftUpperArm',Upper_Arm_L,Upper_Arm_W,Upper_Arm_L/2,"Y",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('LeftUpperArm',Upper_Arm_m,'Z',robot)
##LEFT FOREARM
Scaling_lenght ('LeftForeArm',Fore_Arm_L,Fore_Arm_W,Fore_Arm_L/2,"Y",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('LeftForeArm',Fore_Arm_m,'Z',robot)
##LEFT HAND
Scaling_lenght ('LeftHand',Hand_L,None,Hand_L/2,"Y",'BOX',robot) #length
Scaling_Percentage_Mass ('LeftHand',Hand_m,'Z',robot)

##RIGHT THIGH
Scaling_lenght ('RightUpperLeg',Thigh_L,Thigh_W,-Thigh_L/2,"Z",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('RightUpperLeg',Thigh_m,'Z',robot)
##RIGHT LOWERLEG
Scaling_lenght ('RightLowerLeg',LowerLimb_L,LowerLimb_W,-LowerLimb_L/2,"Z",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('RightLowerLeg',LowerLimb_m,'Z',robot)
##RIGHT FOOT
Scaling_lenght ('RightFoot',Foot_H,None,-Foot_H/2,"Z",'BOX',robot) #length
Scaling_lenght ('RightFoot',Foot_W,None,None,"Y",'BOX',robot) #width
Scaling_lenght ('RightFoot',Foot_L,None,Foot_L/3,"X",'BOX',robot) #deep
Scaling_Percentage_Mass ('RightFoot',Foot_m,'Z',robot)

##LEFT THIGH
Scaling_lenght ('LeftUpperLeg',Thigh_L,Thigh_W,-Thigh_L/2,"Z",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('LeftUpperLeg',Thigh_m,'Z',robot)
##LEFT LOWERLEG
Scaling_lenght ('LeftLowerLeg',LowerLimb_L,LowerLimb_W,-LowerLimb_L/2,"Z",'CYLINDER',robot) #length
Scaling_Percentage_Mass ('LeftLowerLeg',Thigh_m,'Z',robot)
##LEFT FOOT
Scaling_lenght ('LeftFoot',Foot_H,None,-Foot_H/2,"Z",'BOX',robot) #length
Scaling_lenght ('LeftFoot',Foot_W,None,None,"Y",'BOX',robot) #width
Scaling_lenght ('LeftFoot',Foot_L,None,Foot_L/3,"X",'BOX',robot) #deep
Scaling_Percentage_Mass ('LeftFoot',Foot_m,'Z',robot)


##############################################################################################
# JOINT
##############################################################################################

## JOINT PELVI-MIDDLETRUNK
Scaling_Joint_Position ('jL5S1_rotx',J_Pelvi_MiddleTrunk_Z,'Z',robot) 


## JOINT MIDDLETRUNK-UPPERTRUNK_MIDDLE
Scaling_Joint_Position ('jL4L3_rotx',J_MiddleTrunk_UpperTrunk_Middle_Z,'Z',robot) 
## JOINT UPPERTRUNK_MIDDLE-UPPERTRUNK_RIGHT
Scaling_Joint_Position ('jT1C7_Right_rotx',J_UpperTrunk_Middle_UpperTrunk_Right_Z,'Z',robot) 
Scaling_Joint_Position ('jT1C7_Right_rotx',J_UpperTrunk_Middle_UpperTrunk_Right_Y,'Y',robot)
## JOINT UPPERTRUNK_MIDDLE-UPPERTRUNK_LEFT
Scaling_Joint_Position ('jT1C7_Left_rotx',J_UpperTrunk_Middle_UpperTrunk_Left_Z,'Z',robot) 
Scaling_Joint_Position ('jT1C7_Left_rotx',J_UpperTrunk_Middle_UpperTrunk_Left_Y,'Y',robot) 



## JOINT UPPERTRUNK - NECK
Scaling_Joint_Position ('jT1C7_rotx',J_UpperTrunk_Middle_Neck,'Z',robot) #height
## JOINT NECK - HEAD
Scaling_Joint_Position ('jC1Head_rotx',J_Neck_Head,'Z',robot) #height

## JOINT RIGHT SHOULDER
if Geometry == "Box":
    Scaling_Joint_Position ('jRightC7Shoulder_rotx',J_Right_Shoulder_Z,'Z',robot) #height
Scaling_Joint_Position ('jRightC7Shoulder_rotx',J_Right_Shoulder_Y,'Y',robot) #lateral
## JOINT RIGHT ELBOW
Scaling_Joint_Position ('jRightElbow_rotx',J_Right_Elbow_Y,'Y',robot) #lateral
## JOINT RIGHT WRIST
Scaling_Joint_Position ('jRightWrist_rotx',J_Right_Wrist_Y,'Y',robot) #lateral

## JOINT LEFT SHOULDER
if Geometry == "Box":
    Scaling_Joint_Position ('jLeftC7Shoulder_rotx',J_Left_Shoulder_Z,'Z',robot) #height
Scaling_Joint_Position ('jLeftC7Shoulder_rotx',J_Left_Shoulder_Y,'Y',robot) #lateral
## JOINT LEFT ELBOW
Scaling_Joint_Position ('jLeftElbow_rotx',J_Left_Elbow_Y,'Y',robot) #lateral
## JOINT LEFT WRIST
Scaling_Joint_Position ('jLeftWrist_rotx',J_Left_Wrist_Y,'Y',robot) #lateral

## JOINT RIGHT HIP
Scaling_Joint_Position ('jRightHip_rotx',J_Right_Hip_Y,'Y',robot) #lateral
## JOINT RIGHT KNEE
Scaling_Joint_Position ('jRightKnee_rotx',J_Right_Knee_Z,'Z',robot) #height
## JOINT RIGHT ANKLE
Scaling_Joint_Position ('jRightAnkle_rotx',J_Right_Ankle_Z,'Z',robot) #height

## JOINT LEFT HIP
Scaling_Joint_Position ('jLeftHip_rotx',J_Left_Hip_Y,'Y',robot) #lateral
## JOINT LEFT KNEE
Scaling_Joint_Position ('jLeftKnee_rotx',J_Left_Knee_Z,'Z',robot) #height
## JOINT LEFT ANKLE
Scaling_Joint_Position ('jLeftAnkle_rotx',J_Left_Ankle_Z,'Z',robot) #height


# Write URDF to a new file, also adding back the previously removed <gazebo> tags                
utils.write_urdf_to_file(robot, output_file, gazebo_plugin_text)


