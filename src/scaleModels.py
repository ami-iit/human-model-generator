
# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

import math

def scaleLink (H,UpperArm_x,Model):

    """
    Modifies the length and width of links based on anthropometric parameters.

    Args:
        H (float): Height of the subject.
        UpperArm_x (float): Width of the upper arm.
        Model (str): Model type for anthropometric corrections ('Dumas' or 'DeLeva').

    Returns:
        tuple: Modified dimensions of various body parts.
    """

    # Links' length and width modification
    Head_x = (0.13*H)
    Neck_z = 0.052*H    

    match Model:
        
        case 'Dumas':

            #Dumas, et. al 2007 & Dumas, et. al 2015 correction
            UpperTrunk_z = 0.167*H
            UpperTrunk_y = (0.259*H)/3

            Shoulder_x = UpperArm_x
            Shoulder_y = (0.259*H)/3

            LowerTrunk_z    = 0.067*H
            LowerTrunk_y    = (0.174*H)

            Pelvis_z         = 0.05*H # _L = length
            Pelvis_y         = (0.191*H) # _W = width

        case 'DeLeva':

            ##De Leva, et. al 1996 correction   
            UpperTrunk_z = 0.11*H
            UpperTrunk_y = (0.259*H)/3

            Shoulder_x = UpperArm_x
            Shoulder_y = (0.259*H)/3

            LowerTrunk_z    = 0.1*H
            LowerTrunk_y    = (0.174*H)

            Pelvis_z         = 0.078*H
            Pelvis_y         = (0.191*H)

    UpperArm_y = 0.186*H

    ForeArm_y  = 0.146*H

    Hand_y      = 0.108*H

    UpperLeg_z  = 0.245*H
    LowerLeg_z  = 0.246*H

    Foot_z      = 0.039*H
    Foot_y      = 0.055*H
    Foot_x      = 0.152*H 

    return     Head_x,Neck_z,UpperTrunk_z,UpperTrunk_y,Shoulder_x,Shoulder_y,\
               LowerTrunk_z,LowerTrunk_y,Pelvis_z,Pelvis_y,UpperArm_y,ForeArm_y,Hand_y,UpperLeg_z,LowerLeg_z,\
               Foot_z,Foot_y,Foot_x

def scaleJoint (Neck_z,UpperTrunk_z,UpperTrunk_y,Shoulder_y,Shoulder_x,LowerTrunk_z,Pelvis_z,Pelvis_y,\
    UpperArm_y,ForeArm_y,Hand_y, UpperLeg_z,UpperLeg_x,LowerLeg_z,LowerLeg_x,Foot_z,Foot_x):

    """
    Modifies the position of joints based on anthropometric parameters.

    Args:
        Neck_z (float): Length of the neck.
        UpperTrunk_z (float): Length of the upper trunk.
        UpperTrunk_y (float): Width of the upper trunk.
        Shoulder_y (float): Width of the shoulders.
        Shoulder_x (float): Length of the shoulders.
        LowerTrunk_z (float): Length of the lower trunk.
        Pelvis_z (float): Length of the pelvis.
        Pelvis_y (float): Width of the pelvis.
        UpperArm_y (float): Length of the upper arm.
        ForeArm_y (float): Length of the forearm.
        Hand_y (float): Length of the hand.
        UpperLeg_z (float): Length of the upper leg.
        UpperLeg_x (float): Width of the upper leg.
        LowerLeg_z (float): Length of the lower leg.
        LowerLeg_x (float): Width of the lower leg.
        Foot_z (float): Length of the foot.
        Foot_x (float): Width of the foot.

    Returns:
        tuple: Modified positions of various joints.
    """
   
    # Joints' position modification

    # Pelvis - LowerTrunk
    jL5S1_z            =  Pelvis_z

    # LowerTrunk - UpperTrunk    
    jT9T8_z            =  LowerTrunk_z 

    # UpperTrunk - RightShoulder        
    jC7RightShoulder_y  = -UpperTrunk_y/2 
    jC7RightShoulder_z  =  UpperTrunk_z-Shoulder_x/2

    # UpperTrunk - LeftShoulder       
    jC7LeftShoulder_y   =  UpperTrunk_y/2 
    jC7LeftShoulder_z   =  UpperTrunk_z-Shoulder_x/2

    # UpperTrunk - Neck      
    jT1C7_z              =  UpperTrunk_z
    
    # UpperTrunk - Neck
    jC1Head_z            =  Neck_z


    jRightShoulder_y   = -UpperTrunk_y
    jRightShoulder_z   =  None
    jRightElbow_y      = -UpperArm_y
    jRightWrist_y      = -ForeArm_y
    jRightHandCOM_y    = -Hand_y/2

    jLeftShoulder_y    =  UpperTrunk_y
    jLeftShoulder_z    =  None
    jLeftElbow_y       =  UpperArm_y
    jLeftWrist_y       =  ForeArm_y
    jLeftHandCOM_y     =  Hand_y/2

    jRightHip_y        = -((Pelvis_y/2)-(UpperLeg_x/2)) 
    jRightKnee_z       = -UpperLeg_z 
    jRightAnkle_z      = -LowerLeg_z 
    jRightAnkle_x      = -LowerLeg_x/2 
    jRightBallFoot_x   = Foot_x
    jRightBallFoot_z   = -Foot_z
    jRightHeel_z       = -Foot_z

    jLeftHip_y        =  ((Pelvis_y/2)-(UpperLeg_x/2)) 
    jLeftKnee_z       = -UpperLeg_z 
    jLeftAnkle_z      = -LowerLeg_z 
    jLeftAnkle_x      = -LowerLeg_x/2
    jLeftBallFoot_x   =  Foot_x
    jLeftBallFoot_z   = -Foot_z
    jLeftHeel_z       = -Foot_z

    # Fixed joint position based on shoes dimension 
    jRightBirken_x    =  0.037  
    jRightBirken_z    = -0.055  
    jLeftBirken_x     =  0.037  
    jLeftBirken_z     = -0.055  

    return     jL5S1_z,jT9T8_z,jC7RightShoulder_y,jC7RightShoulder_z,jC7LeftShoulder_y,jC7LeftShoulder_z,jT1C7_z,jC1Head_z,\
               jRightShoulder_y,jRightShoulder_z,jRightElbow_y,jRightWrist_y,jRightHandCOM_y,jLeftShoulder_y,jLeftShoulder_z,\
               jLeftElbow_y,jLeftWrist_y,jLeftHandCOM_y,jRightHip_y,jRightKnee_z,jRightAnkle_z,jRightAnkle_x,jRightBallFoot_x,\
               jRightBallFoot_z,jRightHeel_z,jLeftHip_y,jLeftKnee_z,jLeftAnkle_z,jLeftAnkle_x,jLeftBallFoot_x,jLeftBallFoot_z,\
               jLeftHeel_z,jRightBirken_x,jRightBirken_z,jLeftBirken_x,jLeftBirken_z

def scaleMuscleJoint (UpperArm_x,ForeArm_x,Hand_y,Hand_x,Hand_z,UpperTrunk_z,UpperTrunk_y,UpperTrunk_x,Pelvis_x,\
                        Pelvis_y,Pelvis_z,UpperLeg_z,UpperLeg_x,LowerLeg_x,Foot_z,Foot_x,Foot_y):
    
    """
    Modifies the position of muscle attachment points based on anthropometric parameters.

    Args:
        UpperArm_x (float): Width of the upper arm.
        ForeArm_x (float): Width of the forearm.
        Hand_y (float): Length of the hand.
        Hand_x (float): Width of the hand.
        Hand_z (float): Height of the hand.
        UpperTrunk_z (float): Length of the upper trunk.
        UpperTrunk_y (float): Width of the upper trunk.
        UpperTrunk_x (float): Length of the upper trunk.
        Pelvis_x (float): Length of the pelvis.
        Pelvis_y (float): Width of the pelvis.
        Pelvis_z (float): Length of the pelvis.
        UpperLeg_z (float): Length of the upper leg.
        UpperLeg_x (float): Width of the upper leg.
        LowerLeg_x (float): Width of the lower leg.
        Foot_z (float): Length of the foot.
        Foot_x (float): Width of the foot.
        Foot_y (float): Height of the foot.

    Returns:
        tuple: Modified positions of various muscle attachment points.
    """
    
    pi = math.pi

    # Biceps
    jRightBicBrac_RUA_x  = (-1)*(UpperArm_x/2)  * math.cos((pi/2)) 
    jRightBicBrac_RUA_z  = (UpperArm_x/2)       * math.sin((pi/2)) 
    jRightBicBrac_RFA_x  = (-1)*(ForeArm_x/2)   * math.cos((pi))
    jRightBicBrac_RFA_z  = (ForeArm_x/2)        * math.sin((pi/2)) 
    jLeftBicBrac_LUA_x   = (UpperArm_x/2)       * math.cos((pi/2)) 
    jLeftBicBrac_LUA_z   = (UpperArm_x/2)       * math.sin((pi/2)) 
    jLeftBicBrac_LFA_x   = (ForeArm_x/2)        * math.cos((0))
    jLeftBicBrac_LFA_z   = (ForeArm_x/2)        * math.sin((0)) 

    # Triceps
    jRightTricBrac_RUA_x = (-1)*(UpperArm_x/2)  * math.cos((0))
    jRightTricBrac_RUA_z = (UpperArm_x/2)       * math.sin((0)) 
    jRightTricBrac_RFA_x = (ForeArm_x/2)        * math.cos((0)) 
    jRightTricBrac_RFA_z = (ForeArm_x/2)        * math.sin((0)) 
    jLeftTricBrac_LUA_x  = (-1)*(UpperArm_x/2)  * math.cos((pi))
    jLeftTricBrac_LUA_z  = (UpperArm_x/2)       * math.sin((pi)) 
    jLeftTricBrac_LFA_x  = (-1)*(ForeArm_x/2)   * math.cos((pi))
    jLeftTricBrac_LFA_z  = (ForeArm_x/2)        * math.sin((pi)) 
    
    # Flexor carpi radialis
    jRightFlexCarp_RFA_x = (-1)*(ForeArm_x/2)   * math.cos((0))
    jRightFlexCarp_RFA_z = (ForeArm_x/2)        * math.sin((0)) 
    jRightFlexCarp_RH_x  =  Hand_x/5
    jRightFlexCarp_RH_y  = -Hand_y/2
    jRightFlexCarp_RH_z  =  Hand_z/2
    jLeftFlexCarp_LFA_x  = (ForeArm_x/2)       * math.cos((pi))
    jLeftFlexCarp_LFA_z  = (ForeArm_x/2)       * math.sin((pi)) 
    jLeftFlexCarp_LH_x   =  Hand_x/5
    jLeftFlexCarp_LH_y   =  Hand_y/2
    jLeftFlexCarp_LH_z   =  Hand_z/2

    # Extensor carpi radialis
    jRightExtCarp_RFA_x  = (-1)*(ForeArm_x/2)  * math.cos((pi))
    jRightExtCarp_RFA_z  = (ForeArm_x/2)       * math.sin((pi)) 
    jRightExtCarp_RH_x   =  Hand_x/5
    jRightExtCarp_RH_y   = -Hand_y/2
    jRightExtCarp_RH_z   = -Hand_z/2
    jLeftExtCarp_LFA_x   = (ForeArm_x/2)       * math.cos((pi))
    jLeftExtCarp_LFA_z   = (ForeArm_x/2)       * math.sin((pi)) 
    jLeftExtCarp_LH_x    =  Hand_x/5
    jLeftExtCarp_LH_y    =  Hand_y/2
    jLeftExtCarp_LH_z    = -Hand_z/2

    # Erector spinae longissimus
    jRightErSpin_RUT_x   = -UpperTrunk_x/2
    jRightErSpin_RUT_y   = -UpperTrunk_y/2
    jRightErSpin_RUT_z   =  UpperTrunk_z
    jRightErSpin_RP_x    = -Pelvis_x/2
    jLeftErSpin_LUT_x    = -UpperTrunk_x/2
    jLeftErSpin_LUT_y    =  UpperTrunk_y/2
    jLeftErSpin_LUT_z    = UpperTrunk_z
    jLeftErSpin_LP_x     = -Pelvis_x/2

    # Rectus abdominis
    jRightRecAbd_RUT_x   = UpperTrunk_x/2
    jRightRecAbd_RUT_y   =-UpperTrunk_y/2
    jRightRecAbd_RP_x    = Pelvis_x/2
    jLeftRecAbd_LUT_x    = UpperTrunk_x/2
    jLeftRecAbd_LUT_y    = UpperTrunk_y/2
    jLeftRecAbd_LP_x     = Pelvis_x/2

    # Biceps femoris
    jRightBicFem_RUL_x   = (UpperLeg_x/2)       * math.sin((3/2*pi))
    jRightBicFem_RUL_y   = (-1)*(LowerLeg_x/2)  * math.cos((3/2*pi))
    jRightBicFem_RLL_x   = (LowerLeg_x/2)       * math.sin(0)
    jRightBicFem_RLL_y   = (-1)*(LowerLeg_x/2)  * math.cos(0)
    jLeftBicFem_LUL_x    = (UpperLeg_x/2)       * math.sin((3/2*pi))
    jLeftBicFem_LUL_y    = (-1)*(LowerLeg_x/2)  * math.cos((3/2*pi))
    jLeftBicFem_LLL_x    = (LowerLeg_x/2)       * math.sin(pi)
    jLeftBicFem_LLL_y    = (-1)*(LowerLeg_x/2)  * math.cos(pi)

    # Rectus femoris
    jRightRecFem_RP_x    = Pelvis_x/2
    jRightRecFem_RP_y    = -Pelvis_y/3
    jRightRecFem_RP_z    = Pelvis_z/2
    jRightRecFem_RLL_x   = (LowerLeg_x/2)      * math.sin((pi/2))
    jRightRecFem_RLL_y   = (-1)*(LowerLeg_x/2) * math.cos((pi/2))
    jLeftRecFem_LP_x     = Pelvis_x/2
    jLeftRecFem_LP_y     = Pelvis_y/3
    jLeftRecFem_LP_z     = Pelvis_z/2
    jLeftRecFem_LLL_x    = (LowerLeg_x/2)      * math.sin((pi/2))
    jLeftRecFem_LLL_y    = (-1)*(LowerLeg_x/2) * math.cos((pi/2))

    # Tibialis anterior
    jRightTibAntRLL_x    = (LowerLeg_x/2)      * math.sin((pi/2))
    jRightTibAntRLL_y    = (-1)*(LowerLeg_x/2) * math.cos((pi/2))
    jRightTibAntRF_x     = Foot_x/2
    jRightTibAntRF_y     = Foot_y/2
    jLeftTibAnt_LLL_x    = (LowerLeg_x/2)      * math.sin((pi/2))
    jLeftTibAnt_LLL_y    = (-1)*(LowerLeg_x/2) * math.cos((pi/2))
    jLeftTibAnt_LF_x     = Foot_x/2
    jLeftTibAnt_LF_y     = -Foot_y/2

    # Gastrocnemius medialis
    jRightGasMed_RUL_x   = (UpperLeg_x/2)       * math.sin((4/3*pi))
    jRightGasMed_RUL_y   = (-1)*(LowerLeg_x/2)  * math.cos((4/3*pi))
    jRightGasMed_RUL_z   = -UpperLeg_z
    jRightGasMed_RF_z    = -Foot_z/2
    jLeftGasMed_LUL_x    = (UpperLeg_x/2)       * math.sin((5/3*pi))
    jLeftGasMed_LUL_y    = (-1)*(LowerLeg_x/2)  * math.cos((5/3*pi))
    jLeftGasMed_LUL_z    = -UpperLeg_z
    jLeftGasMed_LF_z     = -Foot_z/2

    # Gastrocnemius lateralis  
    jRightGasLatRUL_x   = (UpperLeg_x/2)        * math.sin((5/3*pi))
    jRightGasLatRUL_y   = (-1)*(LowerLeg_x/2)   * math.cos((5/3*pi))
    jRightGasLatRUL_z   = -UpperLeg_z
    jRightGasLatRF_z    = -Foot_z/2
    jLeftGasLat_LUL_x    = (UpperLeg_x/2)       * math.sin((4/3*pi))
    jLeftGasLat_LUL_y    = (-1)*(LowerLeg_x/2)  * math.cos((4/3*pi))
    jLeftGasLat_LUL_z    = -UpperLeg_z
    jLeftGasLat_LF_z     = -Foot_z/2

    return     jRightBicBrac_RUA_x, jRightBicBrac_RUA_z, jRightBicBrac_RFA_x,jRightBicBrac_RFA_z,\
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
               jRightTibAntRLL_x,jRightTibAntRLL_y,jRightTibAntRF_x,jRightTibAntRF_y,jLeftTibAnt_LLL_x,jLeftTibAnt_LLL_y,jLeftTibAnt_LF_x,\
               jLeftTibAnt_LF_y,jRightGasMed_RUL_x,jRightGasMed_RUL_y,jRightGasMed_RUL_z,jRightGasMed_RF_z,jLeftGasMed_LUL_x,jLeftGasMed_LUL_y,\
               jLeftGasMed_LUL_z,jLeftGasMed_LF_z,jRightGasLatRUL_x,jRightGasLatRUL_y,jRightGasLatRUL_z,jRightGasLatRF_z,jLeftGasLat_LUL_x,\
               jLeftGasLat_LUL_y,jLeftGasLat_LUL_z,jLeftGasLat_LF_z

def scaleMass (TotalMass,Model):
    
    """
    Modifies the mass of body segments based on anthropometric parameters.

    Args:
        TotalMass (float): Total mass of the subject.
        Model (str): Model type for anthropometric corrections ('Dumas' or 'DeLeva').

    Returns:
        tuple: Modified masses of various body segments.
    """
        
    # Links' mass modification
    match Model:
        
        case "Dumas":

            # Dumas, et. al 2007 & Dumas, et. al 2015 correction
            Head_mass         = 0.0479 * TotalMass
            Neck_mass         = 0.0191 * TotalMass
            UpperTrunk_mass   = 0.0945 * TotalMass
            LowerTrunk_mass   = 0.035  * TotalMass
            Shoulder_mass     = 0.0945 * TotalMass
            Pelvi_mass        = 0.1435 * TotalMass
            UpperArm_mass     = 0.023  * TotalMass
            ForeArm_mass      = 0.015  * TotalMass
            Hand_mass         = 0.0055 * TotalMass
            UpperLeg_mass     = 0.1345 * TotalMass
            LowerLeg_mass     = 0.0465 * TotalMass
            Foot_mass         = 0.011  * TotalMass

        case "DeLeva":

            # De Leva, et. al 1996 correction   
            Head_mass         = 0.0487 * TotalMass
            Neck_mass         = 0.0194 * TotalMass
            UpperTrunk_mass   = 0.0523 * TotalMass
            LowerTrunk_mass   = 0.1549 * TotalMass
            Shoulder_mass     = 0.0523 * TotalMass
            Pelvi_mass        = 0.1183 * TotalMass
            UpperArm_mass     = 0.0263 * TotalMass
            ForeArm_mass      = 0.015  * TotalMass
            Hand_mass         = 0.0059 * TotalMass
            UpperLeg_mass     = 0.1447 * TotalMass
            LowerLeg_mass     = 0.0457 * TotalMass
            Foot_mass         = 0.0133 * TotalMass
   
    return     Head_mass,Neck_mass,UpperTrunk_mass,Shoulder_mass,LowerTrunk_mass,\
               Pelvi_mass,UpperArm_mass,ForeArm_mass,Hand_mass,UpperLeg_mass,LowerLeg_mass,Foot_mass


