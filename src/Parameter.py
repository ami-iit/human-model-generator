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
            UpperTrunk_Middle_L = 0.167*H
            UpperTrunk_Middle_W = (0.259*H)/3
            match Geometry:
                case "Cylinder":
                    UpperTrunk_Right_L = Upper_Arm_W
                    UpperTrunk_Left_L = Upper_Arm_W
                case "Box":
                    UpperTrunk_Right_L = 0.167*H    
                    UpperTrunk_Left_L = 0.167*H


            UpperTrunk_Right_W = (0.259*H)/3
            UpperTrunk_Left_W = (0.259*H)/3
            MiddleTrunk_L = 0.067*H
            MiddleTrunk_W = (0.174*H)
            Pelvi_L = 0.05*H # _L = length
            Pelvi_W = (0.191*H) # _W = width

        case 'DeLeva':
            ##De Leva, et. al 1996 correction   
            UpperTrunk_Middle_L = 0.11*H
            UpperTrunk_Middle_W = (0.259*H)/3
            match Geometry:
                case "Cylinder":
                    UpperTrunk_Right_L = Upper_Arm_W
                    UpperTrunk_Left_L = Upper_Arm_W
                case "Box":
                    UpperTrunk_Right_L = 0.11*H
                    UpperTrunk_Left_L = 0.11*H

            UpperTrunk_Right_W = (0.259*H)/3
            UpperTrunk_Left_W = (0.259*H)/3
            MiddleTrunk_L = 0.1*H
            MiddleTrunk_W = (0.174*H)
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



    return Head_L,Neck_L,Neck_W,Neck_D,UpperTrunk_Middle_L,UpperTrunk_Middle_W,UpperTrunk_Right_L,UpperTrunk_Right_W,\
    UpperTrunk_Left_L,UpperTrunk_Left_W,MiddleTrunk_L,MiddleTrunk_W,Pelvi_L,Pelvi_W,\
    Upper_Arm_L,Upper_Arm_W,Upper_Arm_D,Fore_Arm_L,Fore_Arm_W,Fore_Arm_D,Hand_L,\
    Thigh_L,Thigh_W,Thigh_D,LowerLimb_L,LowerLimb_W,LowerLimb_D,Foot_H,Foot_W,Foot_L

def ScalingJoint (Neck_L,UpperTrunk_Middle_L,UpperTrunk_Middle_W,UpperTrunk_Right_L,UpperTrunk_Right_W,\
    UpperTrunk_Left_L,UpperTrunk_Left_W,MiddleTrunk_L,Pelvi_L,Pelvi_W,\
    Upper_Arm_L,Upper_Arm_W,Fore_Arm_L, Thigh_L,Thigh_W,LowerLimb_L,LowerLimb_W, Geometry ):

        # Joints' position modification

    J_Pelvi_MiddleTrunk_Z = Pelvi_L

    J_MiddleTrunk_UpperTrunk_Middle_Z = MiddleTrunk_L 

    J_UpperTrunk_Middle_UpperTrunk_Right_Y = -UpperTrunk_Middle_W/2 

    match Geometry:

        case "Cylinder":
            J_UpperTrunk_Middle_UpperTrunk_Right_Z = UpperTrunk_Middle_L-UpperTrunk_Right_L
        case "Box":
            J_UpperTrunk_Middle_UpperTrunk_Right_Z = UpperTrunk_Right_L/2

    

    J_UpperTrunk_Middle_UpperTrunk_Left_Y = UpperTrunk_Middle_W/2 

    match Geometry:
        case "Cylinder":
            J_UpperTrunk_Middle_UpperTrunk_Left_Z = UpperTrunk_Middle_L-UpperTrunk_Left_L
        case "Box":
            J_UpperTrunk_Middle_UpperTrunk_Left_Z = UpperTrunk_Left_L/2




    J_UpperTrunk_Middle_Neck = UpperTrunk_Middle_L
    J_Neck_Head = Neck_L

    J_Right_Shoulder_Y = -UpperTrunk_Right_W

    match Geometry:
        case "Cylinder":
            J_Right_Shoulder_Z = None
        case "Box":
            J_Right_Shoulder_Z = (UpperTrunk_Right_L/2)-Upper_Arm_W
    J_Right_Elbow_Y = -Upper_Arm_L
    J_Right_Wrist_Y = -Fore_Arm_L

    J_Left_Shoulder_Y = UpperTrunk_Left_W

    match Geometry:
        case "Cylinder":
            J_Left_Shoulder_Z = None
        case "Box":
            J_Left_Shoulder_Z = (UpperTrunk_Left_L/2)-Upper_Arm_W
    J_Left_Elbow_Y = Upper_Arm_L
    J_Left_Wrist_Y = Fore_Arm_L

    J_Right_Hip_Y = -((Pelvi_W/2)-Thigh_W) 
    J_Right_Knee_Z = - Thigh_L 
    J_Right_Ankle_Z = - LowerLimb_L 
    J_Right_Ankle_X = -LowerLimb_W 

    J_Left_Hip_Y = ((Pelvi_W/2)-Thigh_W) 
    J_Left_Knee_Z = - Thigh_L 
    J_Left_Ankle_Z = - LowerLimb_L 
    J_Left_Ankle_X =  -LowerLimb_W


    return J_UpperTrunk_Middle_UpperTrunk_Right_Y,J_UpperTrunk_Middle_UpperTrunk_Right_Z,J_UpperTrunk_Middle_UpperTrunk_Left_Y,J_UpperTrunk_Middle_UpperTrunk_Left_Z,\
    J_UpperTrunk_Middle_Neck,J_Neck_Head,J_Right_Shoulder_Y,J_Right_Shoulder_Z,J_Right_Elbow_Y,J_Right_Wrist_Y,\
    J_Left_Shoulder_Y,J_Left_Shoulder_Z,J_Left_Elbow_Y,J_Left_Wrist_Y,J_Right_Hip_Y,J_Right_Knee_Z,J_Right_Ankle_Z,J_Left_Hip_Y,\
    J_Left_Knee_Z,J_Left_Ankle_Z,J_Pelvi_MiddleTrunk_Z,J_MiddleTrunk_UpperTrunk_Middle_Z,J_Right_Ankle_X,J_Left_Ankle_X

def ScalingMassPar (m,Model):
    
    # Links' mass modification

    match Model:

        case "Dumas":
            #Dumas, et. al 2007 & Dumas, et. al 2015 correction
            Head_m = 0.0479*m
            Neck_m = 0.0191*m
            UpperTrunk_Middle_m = 0.0945*m
            UpperTrunk_Right_m= 0.0945*m
            UpperTrunk_Left_m = 0.0945*m
            MiddleTrunk_m = 0.035*m
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
            UpperTrunk_Middle_m = 0.0523*m
            UpperTrunk_Right_m= 0.0523*m
            UpperTrunk_Left_m = 0.0523*m
            MiddleTrunk_m = 0.1549*m
            Pelvi_m = 0.1183*m
            Upper_Arm_m = 0.0263*m
            Fore_Arm_m = 0.015*m
            Hand_m = 0.0059*m
            Thigh_m = 0.1447*m
            LowerLimb_m = 0.0457*m
            Foot_m = 0.0133*m

    
    return Head_m,Neck_m,UpperTrunk_Middle_m,UpperTrunk_Right_m,UpperTrunk_Left_m,MiddleTrunk_m,\
    Pelvi_m,Upper_Arm_m,Fore_Arm_m,Hand_m,Thigh_m,LowerLimb_m,Foot_m

