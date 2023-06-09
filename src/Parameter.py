import math

def ScalingAnthroPar (H,Model,Geometry):

    #Empirically based constants on Lorenzo Flowers

    Neck_W = 0.04
    Upper_Arm_W = 0.05
    Fore_Arm_W = 0.03
    Thigh_W = 0.07
    LowerLimb_W = 0.04

    Neck_D = 0.04
    Upper_Arm_D = 0.05
    Fore_Arm_D = 0.03
    Thigh_D = 0.07
    LowerLimb_D = 0.04

    # Links' length and width modification

    Head_L = (0.13*H)
    Neck_L = 0.052*H    

    match Model:
        
        case 'Dumas':
            #Dumas, et. al 2007 & Dumas, et. al 2015 correction
            UpperTrunk_L = 0.167*H
            UpperTrunk_W = (0.259*H)/3
            match Geometry:
                case "Cylinder":
                    RightShoulder_L = Upper_Arm_W
                    LeftShoulder_L = Upper_Arm_W
                case "Box":
                    RightShoulder_L = 0.167*H    
                    LeftShoulder_L = 0.167*H


            RightShoulder_W = (0.259*H)/3
            LeftShoulder_W = (0.259*H)/3
            LowerTrunk_L = 0.067*H
            LowerTrunk_W = (0.174*H)
            Pelvi_L = 0.05*H # _L = length
            Pelvi_W = (0.191*H) # _W = width

        case 'DeLeva':
            ##De Leva, et. al 1996 correction   
            UpperTrunk_L = 0.11*H
            UpperTrunk_W = (0.259*H)/3
            match Geometry:
                case "Cylinder":
                    RightShoulder_L = Upper_Arm_W
                    LeftShoulder_L = Upper_Arm_W
                case "Box":
                    RightShoulder_L = 0.11*H
                    LeftShoulder_L = 0.11*H

            RightShoulder_W = (0.259*H)/3
            LeftShoulder_W = (0.259*H)/3
            LowerTrunk_L = 0.1*H
            LowerTrunk_W = (0.174*H)
            Pelvi_L = 0.078*H
            Pelvi_W = (0.191*H)
            


    Upper_Arm_L = 0.186*H
    Fore_Arm_L = 0.146*H
    Hand_L = 0.108*H

    Thigh_L = 0.245*H
    LowerLimb_L = 0.246*H
    Foot_H = 0.039*H
    Foot_W = 0.055*H
    Foot_L = 0.152*H 



    return Head_L,Neck_L,Neck_W,Neck_D,UpperTrunk_L,UpperTrunk_W,RightShoulder_L,RightShoulder_W,\
    LeftShoulder_L,LeftShoulder_W,LowerTrunk_L,LowerTrunk_W,Pelvi_L,Pelvi_W,\
    Upper_Arm_L,Upper_Arm_W,Upper_Arm_D,Fore_Arm_L,Fore_Arm_W,Fore_Arm_D,Hand_L,\
    Thigh_L,Thigh_W,Thigh_D,LowerLimb_L,LowerLimb_W,LowerLimb_D,Foot_H,Foot_W,Foot_L

def ScalingJoint (Neck_L,UpperTrunk_L,UpperTrunk_W,RightShoulder_L,RightShoulder_W,\
    LeftShoulder_L,LeftShoulder_W,LowerTrunk_L,Pelvi_L,Pelvi_W,\
    Upper_Arm_L,Upper_Arm_W,Fore_Arm_L,Hand_L, Thigh_L,Thigh_W,LowerLimb_L,LowerLimb_W,Foot_H,Foot_L, Geometry ):

        # Joints' position modification

    J_Pelvi_LowerTrunk_Z = Pelvi_L

    J_LowerTrunk_UpperTrunk_Z = LowerTrunk_L 

    J_UpperTrunk_RightShoulder_Y = -UpperTrunk_W/2 

    match Geometry:

        case "Cylinder":
            J_UpperTrunk_RightShoulder_Z = UpperTrunk_L-RightShoulder_L
        case "Box":
            J_UpperTrunk_RightShoulder_Z = RightShoulder_L/2

    

    J_UpperTrunk_LeftShoulder_Y = UpperTrunk_W/2 

    match Geometry:
        case "Cylinder":
            J_UpperTrunk_LeftShoulder_Z = UpperTrunk_L-LeftShoulder_L
        case "Box":
            J_UpperTrunk_LeftShoulder_Z = LeftShoulder_L/2




    J_UpperTrunk_Neck = UpperTrunk_L
    J_Neck_Head = Neck_L

    J_Right_Shoulder_Y = -RightShoulder_W

    match Geometry:
        case "Cylinder":
            J_Right_Shoulder_Z = None
        case "Box":
            J_Right_Shoulder_Z = (RightShoulder_L/2)-Upper_Arm_W
    J_Right_Elbow_Y = -Upper_Arm_L
    J_Right_Wrist_Y = -Fore_Arm_L

    J_Left_Shoulder_Y = LeftShoulder_W

    match Geometry:
        case "Cylinder":
            J_Left_Shoulder_Z = None
        case "Box":
            J_Left_Shoulder_Z = (LeftShoulder_L/2)-Upper_Arm_W
    J_Left_Elbow_Y = Upper_Arm_L
    J_Left_Wrist_Y = Fore_Arm_L

    j_Right_HandCOM_Y = -Hand_L/2
    j_Left_HandCOM_Y = Hand_L/2

    J_Right_Hip_Y = -((Pelvi_W/2)-Thigh_W) 
    J_Right_Knee_Z = -Thigh_L 
    J_Right_Ankle_Z = -LowerLimb_L 
    J_Right_Ankle_X = -LowerLimb_W 
    j_Right_BallFoot_X= Foot_L
    j_Right_BallFoot_Z= -Foot_H

    J_Left_Hip_Y = ((Pelvi_W/2)-Thigh_W) 
    J_Left_Knee_Z = -Thigh_L 
    J_Left_Ankle_Z = - LowerLimb_L 
    J_Left_Ankle_X = - LowerLimb_W
    j_Left_BallFoot_X = Foot_L
    j_Left_BallFoot_Z= -Foot_H


    return J_UpperTrunk_RightShoulder_Y,J_UpperTrunk_RightShoulder_Z,J_UpperTrunk_LeftShoulder_Y,J_UpperTrunk_LeftShoulder_Z,\
    J_UpperTrunk_Neck,J_Neck_Head,J_Right_Shoulder_Y,J_Right_Shoulder_Z,J_Right_Elbow_Y,J_Right_Wrist_Y,\
    J_Left_Shoulder_Y,J_Left_Shoulder_Z,J_Left_Elbow_Y,J_Left_Wrist_Y,j_Right_HandCOM_Y,j_Left_HandCOM_Y,J_Right_Hip_Y,J_Right_Knee_Z,J_Right_Ankle_Z,J_Left_Hip_Y,\
    J_Left_Knee_Z,J_Left_Ankle_Z,J_Pelvi_LowerTrunk_Z,J_LowerTrunk_UpperTrunk_Z,J_Right_Ankle_X,J_Left_Ankle_X,j_Right_BallFoot_X,\
    j_Right_BallFoot_Z,j_Left_BallFoot_X,j_Left_BallFoot_Z

def ScalingMassPar (m,Model):
    
    # Links' mass modification

    match Model:
        
        case "Dumas":
            #Dumas, et. al 2007 & Dumas, et. al 2015 correction
            Head_m = 0.0479*m
            Neck_m = 0.0191*m
            UpperTrunk_m = 0.0945*m
            RightShoulder_m= 0.0945*m
            LeftShoulder_m = 0.0945*m
            LowerTrunk_m = 0.035*m
            Pelvi_m = 0.1435*m
            Upper_Arm_m = 0.023*m
            Fore_Arm_m = 0.015*m
            Hand_m = 0.0055*m
            Thigh_m = 0.1345*m
            LowerLimb_m = 0.0465*m
            Foot_m = 0.011*m


        case "DeLeva":
            ##De Leva, et. al 1996 correction   
            Head_m = 0.0487*m
            Neck_m = 0.0194*m
            UpperTrunk_m = 0.0523*m
            RightShoulder_m= 0.0523*m
            LeftShoulder_m = 0.0523*m
            LowerTrunk_m = 0.1549*m
            Pelvi_m = 0.1183*m
            Upper_Arm_m = 0.0263*m
            Fore_Arm_m = 0.015*m
            Hand_m = 0.0059*m
            Thigh_m = 0.1447*m
            LowerLimb_m = 0.0457*m
            Foot_m = 0.0133*m

    
    return Head_m,Neck_m,UpperTrunk_m,RightShoulder_m,LeftShoulder_m,LowerTrunk_m,\
    Pelvi_m,Upper_Arm_m,Fore_Arm_m,Hand_m,Thigh_m,LowerLimb_m,Foot_m