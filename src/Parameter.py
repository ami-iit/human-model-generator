import math

def ScalingAnthroPar (H,Model,Geometry):

    #Empirically based constants on Lorenzo Flowers
    '''
    '''

    #Constants
    Neck_W = 0.08
    Upper_Arm_W = 0.1
    Fore_Arm_W = 0.06
    Thigh_W = 0.14
    LowerLimb_W = 0.08
    Hand_W = 0.1

    Neck_D = 0.08
    UpperTrunk_D = 0.15
    Upper_Arm_D = 0.1
    Fore_Arm_D = 0.06
    Thigh_D = 0.14
    LowerLimb_D = 0.08
    Pelvi_D = 0.15


    Hand_H = 0.03

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



    return Head_L,Neck_L,Neck_W,Neck_D,UpperTrunk_L,UpperTrunk_W,UpperTrunk_D,RightShoulder_L,RightShoulder_W,\
    LeftShoulder_L,LeftShoulder_W,LowerTrunk_L,LowerTrunk_W,Pelvi_L,Pelvi_W,Pelvi_D,\
    Upper_Arm_L,Upper_Arm_W,Upper_Arm_D,Fore_Arm_L,Fore_Arm_W,Fore_Arm_D,Hand_L,Hand_W,Hand_H,\
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

def ScalingMuscleJoint (Upper_Arm_D,Upper_Arm_W,Fore_Arm_D,Fore_Arm_W,Hand_L,Hand_W,Hand_H,UpperTrunk_L,UpperTrunk_W,UpperTrunk_D,Pelvi_D,\
                        Pelvi_W,Pelvi_L,Thigh_L,Thigh_D,Thigh_W,LowerLimb_D,LowerLimb_W,Foot_H,Foot_L,Foot_W):
    pi = math.pi

    # Biceps
    j_Right_BicBrac_RUA_X = (-1)*(Upper_Arm_D/2)*math.cos((pi/2)) 
    j_Right_BicBrac_RUA_Z = (Upper_Arm_W/2) * math.sin((pi/2)) 
    j_Right_BicBrac_RFA_X = (-1)*(Fore_Arm_D/2) * math.cos((pi))
    j_Right_BicBrac_RFA_Z = (Fore_Arm_W/2) * math.sin((pi/2)) 
    j_Left_BicBrac_LUA_X  = (Upper_Arm_D/2) * math.cos((pi/2)) 
    j_Left_BicBrac_LUA_Z  = (Upper_Arm_W/2) * math.sin((pi/2)) 
    j_Left_BicBrac_LFA_X  = (Fore_Arm_D/2) * math.cos((0))
    j_Left_BicBrac_LFA_Z  = (Fore_Arm_W/2) * math.sin((0)) 

    # Triceps
    j_Right_TricBrac_RUA_X = (-1)*(Upper_Arm_D/2)* math.cos((0))
    j_Right_TricBrac_RUA_Z = (Upper_Arm_W/2) * math.sin((0)) 
    j_Right_TricBrac_RFA_X = (-1)*(Fore_Arm_D/2) * math.cos((0))
    j_Right_TricBrac_RFA_Z = (Fore_Arm_W/2) * math.sin((0)) 
    j_Left_TricBrac_LUA_X = (-1)*(Upper_Arm_D/2)* math.cos((pi))
    j_Left_TricBrac_LUA_Z = (Upper_Arm_W/2) * math.sin((pi)) 
    j_Left_TricBrac_LFA_X = (-1)*(Fore_Arm_D/2) * math.cos((pi))
    j_Left_TricBrac_LFA_Z = (Fore_Arm_W/2) * math.sin((pi)) 
    
    # Flexor carpi radialis
    j_Right_FlexCarp_RFA_X = (-1)*(Fore_Arm_D/2) * math.cos((0))
    j_Right_FlexCarp_RFA_Z = (Fore_Arm_W/2) * math.sin((0)) 
    j_Right_FlexCarp_RH_X =  Hand_W/5
    j_Right_FlexCarp_RH_Y = -Hand_L/2
    j_Right_FlexCarp_RH_Z =  Hand_H/2
    j_Left_FlexCarp_LFA_X = (Fore_Arm_D/2) * math.cos((pi))
    j_Left_FlexCarp_LFA_Z = (Fore_Arm_W/2) * math.sin((pi)) 
    j_Left_FlexCarp_LH_X =  Hand_W/5
    j_Left_FlexCarp_LH_Y =  Hand_L/2
    j_Left_FlexCarp_LH_Z =  Hand_H/2

    # Extensor carpi radialis
    j_Right_ExtCarp_RFA_X = (-1)*(Fore_Arm_D/2) * math.cos((pi))
    j_Right_ExtCarp_RFA_Z = (Fore_Arm_W/2) * math.sin((pi)) 
    j_Right_ExtCarp_RH_X =  Hand_W/5
    j_Right_ExtCarp_RH_Y = -Hand_L/2
    j_Right_ExtCarp_RH_Z = -Hand_H/2
    j_Left_ExtCarp_LFA_X = (Fore_Arm_D/2) * math.cos((pi))
    j_Left_ExtCarp_LFA_Z = (Fore_Arm_W/2) * math.sin((pi)) 
    j_Left_ExtCarp_LH_X =  Hand_W/5
    j_Left_ExtCarp_LH_Y =  Hand_L/2
    j_Left_ExtCarp_LH_Z = -Hand_H/2

    # Erector spinae longissimus
    j_Right_ErSpin_RUT_X = -UpperTrunk_D/2
    j_Right_ErSpin_RUT_Y = -UpperTrunk_W/2
    j_Right_ErSpin_RUT_Z =  UpperTrunk_L
    j_Right_ErSpin_RP_X =  -Pelvi_D/2
    j_Left_ErSpin_LUT_X = -UpperTrunk_D/2
    j_Left_ErSpin_LUT_Y =  UpperTrunk_W/2
    j_Left_ErSpin_LUT_Z = UpperTrunk_L
    j_Left_ErSpin_LP_X = -Pelvi_D/2

    # Rectus abdominis
    j_Right_RecAbd_RUT_X = UpperTrunk_D/2
    j_Right_RecAbd_RUT_Y = -UpperTrunk_W/2
    j_Right_RecAbd_RP_X = Pelvi_D/2
    j_Left_RecAbd_LUT_X = UpperTrunk_D/2
    j_Left_RecAbd_LUT_Y = UpperTrunk_W/2
    j_Left_RecAbd_LP_X = Pelvi_D/2

    # Biceps femoris
    j_Right_BicFem_RUL_X = (Thigh_D/2) * math.sin((3/2*pi))
    j_Right_BicFem_RUL_Y = (-1)*(Thigh_W/2) * math.cos((3/2*pi))
    j_Right_BicFem_RLL_X = (LowerLimb_D/2) * math.sin(0)
    j_Right_BicFem_RLL_Y = (-1)*(LowerLimb_W/2) * math.cos(0)
    j_Left_BicFem_LUL_X =  (Thigh_D/2) * math.sin((3/2*pi))
    j_Left_BicFem_LUL_Y = (-1)*(Thigh_W/2) * math.cos((3/2*pi))
    j_Left_BicFem_LLL_X = (LowerLimb_D/2) * math.sin(pi)
    j_Left_BicFem_LLL_Y = (-1)*(LowerLimb_W/2) * math.cos(pi)

    # Rectus femoris
    j_Right_RecFem_RP_X = Pelvi_D/2
    j_Right_RecFem_RP_Y =  -Pelvi_W/3
    j_Right_RecFem_RP_Z = Pelvi_L/2
    j_Right_RecFem_RLL_X = (LowerLimb_D/2) * math.sin((pi/2))
    j_Right_RecFem_RLL_Y =  (-1)*(LowerLimb_W/2) * math.cos((pi/2))
    j_Left_RecFem_LP_X = Pelvi_D/2
    j_Left_RecFem_LP_Y =  Pelvi_W/3
    j_Left_RecFem_LP_Z = Pelvi_L/2
    j_Left_RecFem_LLL_X = (LowerLimb_D/2) * math.sin((pi/2))
    j_Left_RecFem_LLL_Y =  (-1)*(LowerLimb_W/2) * math.cos((pi/2))

    # Tibialis anterior
    j_Right_TibAnt_RLL_X = (LowerLimb_D/2) * math.sin((pi/2))
    j_Right_TibAnt_RLL_Y = (-1)*(LowerLimb_W/2) * math.cos((pi/2))
    j_Right_TibAnt_RF_X = Foot_L/2
    j_Right_TibAnt_RF_Y = Foot_W/2
    j_Left_TibAnt_LLL_X = (LowerLimb_D/2) * math.sin((pi/2))
    j_Left_TibAnt_LLL_Y = (-1)*(LowerLimb_W/2) * math.cos((pi/2))
    j_Left_TibAnt_LF_X = Foot_L/2
    j_Left_TibAnt_LF_Y = -Foot_W/2

    # Gastrocnemius medialis
    j_Right_GasMed_RUL_X = (Thigh_D/2) * math.sin((4/3*pi))
    j_Right_GasMed_RUL_Y = (-1)*(Thigh_W/2) * math.cos((4/3*pi))
    j_Right_GasMed_RUL_Z = -Thigh_L
    j_Right_GasMed_RF_Z = -Foot_H/2
    j_Left_GasMed_LUL_X = (Thigh_D/2) * math.sin((5/3*pi))
    j_Left_GasMed_LUL_Y = (-1)*(Thigh_W/2) * math.cos((5/3*pi))
    j_Left_GasMed_LUL_Z = -Thigh_L
    j_Left_GasMed_LF_Z = -Foot_H/2

    # Gastrocnemius lateralis
    j_Right_GasLat_RUL_X = (Thigh_D/2) * math.sin((5/3*pi))
    j_Right_GasLat_RUL_Y = (-1)*(Thigh_W/2) * math.cos((5/3*pi))
    j_Right_GasLat_RUL_Z = -Thigh_L
    j_Right_GasLat_RF_Z = -Foot_H/2
    j_Left_GasLat_LUL_X = (Thigh_D/2) * math.sin((4/3*pi))
    j_Left_GasLat_LUL_Y = (-1)*(Thigh_W/2) * math.cos((4/3*pi))
    j_Left_GasLat_LUL_Z = -Thigh_L
    j_Left_GasLat_LF_Z = -Foot_H/2

    return j_Right_BicBrac_RUA_X, j_Right_BicBrac_RUA_Z, j_Right_BicBrac_RFA_X,j_Right_BicBrac_RFA_Z,\
    j_Left_BicBrac_LUA_X, j_Left_BicBrac_LUA_Z, j_Left_BicBrac_LFA_X,j_Left_BicBrac_LFA_Z,\
    j_Right_TricBrac_RUA_X,j_Right_TricBrac_RUA_Z, j_Right_TricBrac_RFA_X, j_Right_TricBrac_RFA_Z,\
    j_Left_TricBrac_LUA_X,j_Left_TricBrac_LUA_Z, j_Left_TricBrac_LFA_X,j_Left_TricBrac_LFA_Z,\
    j_Right_FlexCarp_RFA_X,j_Right_FlexCarp_RFA_Z,j_Right_FlexCarp_RH_X,j_Right_FlexCarp_RH_Y,j_Right_FlexCarp_RH_Z,\
    j_Left_FlexCarp_LFA_X,j_Left_FlexCarp_LFA_Z,j_Left_FlexCarp_LH_X,j_Left_FlexCarp_LH_Y,j_Left_FlexCarp_LH_Z,\
    j_Right_ExtCarp_RFA_X,j_Right_ExtCarp_RFA_Z,j_Right_ExtCarp_RH_X,j_Right_ExtCarp_RH_Y,j_Right_ExtCarp_RH_Z,\
    j_Left_ExtCarp_LFA_X,j_Left_ExtCarp_LFA_Z,j_Left_ExtCarp_LH_X,j_Left_ExtCarp_LH_Y,j_Left_ExtCarp_LH_Z,\
    j_Right_ErSpin_RUT_X, j_Right_ErSpin_RUT_Y,j_Right_ErSpin_RUT_Z,j_Right_ErSpin_RP_X,j_Left_ErSpin_LUT_X,\
    j_Left_ErSpin_LUT_Y,j_Left_ErSpin_LUT_Z,j_Left_ErSpin_LP_X,\
    j_Right_RecAbd_RUT_X,j_Right_RecAbd_RUT_Y,j_Right_RecAbd_RP_X,j_Left_RecAbd_LUT_X,j_Left_RecAbd_LUT_Y,j_Left_RecAbd_LP_X,\
    j_Right_BicFem_RUL_X, j_Right_BicFem_RUL_Y, j_Right_BicFem_RLL_X, j_Right_BicFem_RLL_Y, j_Left_BicFem_LUL_X, j_Left_BicFem_LUL_Y,\
    j_Left_BicFem_LLL_X,j_Left_BicFem_LLL_Y,j_Right_RecFem_RP_X,j_Right_RecFem_RP_Y,j_Right_RecFem_RP_Z,j_Right_RecFem_RLL_X,\
    j_Right_RecFem_RLL_Y,j_Left_RecFem_LP_X,j_Left_RecFem_LP_Y,j_Left_RecFem_LP_Z,j_Left_RecFem_LLL_X,j_Left_RecFem_LLL_Y,\
    j_Right_TibAnt_RLL_X,j_Right_TibAnt_RLL_Y,j_Right_TibAnt_RF_X,j_Right_TibAnt_RF_Y,j_Left_TibAnt_LLL_X,j_Left_TibAnt_LLL_Y,j_Left_TibAnt_LF_X,\
    j_Left_TibAnt_LF_Y,j_Right_GasMed_RUL_X,j_Right_GasMed_RUL_Y,j_Right_GasMed_RUL_Z,j_Right_GasMed_RF_Z,j_Left_GasMed_LUL_X,j_Left_GasMed_LUL_Y,\
    j_Left_GasMed_LUL_Z,j_Left_GasMed_LF_Z,j_Right_GasLat_RUL_X,j_Right_GasLat_RUL_Y,j_Right_GasLat_RUL_Z,j_Right_GasLat_RF_Z,j_Left_GasLat_LUL_X,\
    j_Left_GasLat_LUL_Y,j_Left_GasLat_LUL_Z,j_Left_GasLat_LF_Z
    

    
    

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