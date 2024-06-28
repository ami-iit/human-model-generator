import os
import numpy as np


def genSynthPhysMov(JOINTLIST, ndofs):

    # Flex-Ext right shoulder
    indexPosRightShoulder = JOINTLIST.index("jRightShoulder_rotx")
    indexMovRightShoulder = JOINTLIST.index("jRightShoulder_rotz")
    posAnglesRightShoulder = [0, 90]
    movAnglesRightShoulder = [[0, 90], [90, -50], [-50, 0]]
    posbackAnglesRightShoulder = [90, 0]

    sMovRightShoulder = generateComplexMov(
        ndofs,
        indexPosRightShoulder,
        indexMovRightShoulder,
        posAnglesRightShoulder,
        movAnglesRightShoulder,
        posbackAnglesRightShoulder,
    )

    # Flex-Ext left shoulder
    indexPosLeftShoulder = JOINTLIST.index("jLeftShoulder_rotx")
    indexMovLeftShoulder = JOINTLIST.index("jLeftShoulder_rotz")
    posAnglesLeftShoulder = [0, -90]
    movAnglesLeftShoulder = [[0, -90], [-90, 50], [50, 0]]
    posbackAnglesLeftShoulder = [-90, 0]

    sMovLeftShoulder = generateComplexMov(
        ndofs,
        indexPosLeftShoulder,
        indexMovLeftShoulder,
        posAnglesLeftShoulder,
        movAnglesLeftShoulder,
        posbackAnglesLeftShoulder,
    )

    # Flex-Ext right wrist
    indexPosRightWrist = JOINTLIST.index("jRightShoulder_rotz")
    indexMovRightWrist = JOINTLIST.index("jRightWrist_rotx")
    posAnglesRightWrist = [0, 90]
    movAnglesRightWrist = [[0, 60], [60, -60], [-60, 0]]
    posbackAnglesRightWrist = [90, 0]

    sMovRightWrist = generateComplexMov(
        ndofs,
        indexPosRightWrist,
        indexMovRightWrist,
        posAnglesRightWrist,
        movAnglesRightWrist,
        posbackAnglesRightWrist,
    )

    # Flex-Ext left wrist
    indexPosLeftWrist = JOINTLIST.index("jLeftShoulder_rotz")
    indexMovLeftWrist = JOINTLIST.index("jLeftWrist_rotx")
    posAnglesLeftWrist = [0, -90]
    movAnglesLeftWrist = [[0, -60], [-60, 60], [60, 0]]
    posbackAnglesLeftWrist = [-90, 0]

    sMovLeftWrist = generateComplexMov(
        ndofs,
        indexPosLeftWrist,
        indexMovLeftWrist,
        posAnglesLeftWrist,
        movAnglesLeftWrist,
        posbackAnglesLeftWrist,
    )

    # Flex-Ext trunk
    indexPosTrunk = [
        JOINTLIST.index("jRightShoulder_rotx"),
        JOINTLIST.index("jLeftShoulder_rotx"),
    ]
    indexMovTrunk = JOINTLIST.index("jL5S1_roty")
    posAnglesTrunk = [0, 90, 0, -90]
    movAnglesTrunk = [[0, 60], [60, -60], [-60, 0]]
    posbackAnglesTrunk = [90, 0, -90, 0]

    sMovTrunk = generateComplexMov(
        ndofs,
        indexPosTrunk,
        indexMovTrunk,
        posAnglesTrunk,
        movAnglesTrunk,
        posbackAnglesTrunk,
    )

    # Flex-Ext lowerLimb
    indexPosLowerLimb = [
        JOINTLIST.index("jRightHip_roty"),
        JOINTLIST.index("jRightKnee_roty"),
    ]
    indexMovLowerLimb = JOINTLIST.index("jRightAnkle_roty")
    posAnglesLowerLimb = [0, -90, 0, 90]
    movAnglesLowerLimb = [[0, -20], [-20, 50], [50, 0]]
    posbackAnglesLowerLimb = [-90, 0, 90, 0]

    sMovLowerLimb = generateComplexMov(
        ndofs,
        indexPosLowerLimb,
        indexMovLowerLimb,
        posAnglesLowerLimb,
        movAnglesLowerLimb,
        posbackAnglesLowerLimb,
    )

    # Combine right and left shoulder movements
    sMovShoulder = sMovRightShoulder + sMovLeftShoulder
    # Combine right and left wrist movements
    sMovWrist = sMovRightWrist + sMovLeftWrist
    Movment = np.hstack((sMovShoulder, sMovWrist, sMovTrunk, sMovLowerLimb))

    return Movment


def genSynthRandMov(ndofs, lowrange, highrange, time, frequency):

    Movement = np.zeros((ndofs, time * frequency))

    for indxDoF in range(ndofs):
        init = 0
        end = frequency
        deg_start = 0
        deg_end = round(np.random.uniform(lowrange, highrange))
        for _ in range(time):

            Movement[indxDoF, init:end] = generateRangOfMotion(
                deg_start, deg_end, frequency
            )
            deg_start = deg_end

            if _ == time - 2:
                deg_end = 0
            else:
                deg_end = round(np.random.uniform(lowrange, highrange))

            init = end
            end += frequency

    return Movement


def generateComplexMov(ndofs, indexPos, indexMov, posAngles, movAngles, posbackAngles):
    # Convert `indexPos` to a list if it is not already
    if isinstance(indexPos, int):
        indexPos = [indexPos]

    # Initialising the motion matrix
    nsamples = 0
    sMov = None

    # If `indexPos` has two values, and `posAngles` and `posbackAngles` have four values
    if len(indexPos) == 2 and len(posAngles) == 4 and len(posbackAngles) == 4:
        pos1 = generateSimpleMov(posAngles[:2])
        pos2 = generateSimpleMov(posAngles[2:])
        mov = generateSimpleMov(*movAngles)
        posback1 = generateSimpleMov(posbackAngles[:2])
        posback2 = generateSimpleMov(posbackAngles[2:])

        nsamples = pos1.size + mov.size + posback1.size
        sMov = np.zeros((ndofs, nsamples))

        sMov[indexPos[0], : pos1.size] = pos1
        offset = pos1.size
        sMov[indexPos[0], offset : offset + mov.size] = pos1[-1]
        offset += mov.size
        sMov[indexPos[0], offset : offset + posback1.size] = posback1
        offset += posback1.size

        sMov[indexPos[1], : pos1.size] = pos2
        offset = pos2.size
        sMov[indexPos[1], offset : offset + mov.size] = pos2[-1]
        offset += mov.size
        sMov[indexPos[1], offset : offset + posback2.size] = posback2
        offset += posback2.size

        # complex movement
        sMov[indexMov, pos1.size : pos1.size + mov.size] = mov

    else:
        pos = generateSimpleMov(posAngles)
        mov = generateSimpleMov(*movAngles)
        posback = generateSimpleMov(posbackAngles)

        nsamples = pos.size + mov.size + posback.size
        sMov = np.zeros((ndofs, nsamples))

        sMov[indexPos[0], : pos.size] = pos
        sMov[indexPos[0], pos.size : nsamples - posback.size] = pos[-1]
        sMov[indexPos[0], nsamples - posback.size : nsamples] = posback
        sMov[indexMov, pos.size : pos.size + mov.size] = mov

    return sMov


def generateSimpleMov(*phases):
    movments = []

    for phase in phases:

        dim_phase = np.abs(np.diff(phase))
        mov_phase = generateRangOfMotion(phase[0], phase[1], abs(dim_phase))
        movments.append(mov_phase)

    # Concatenare tutti i movimenti lungo l'asse orizzontale
    Movement = np.concatenate(movments)

    return Movement


def generateRangOfMotion(deg_start, deg_end, num_points):
    # Conversion from degrees to radians
    rad_start = np.deg2rad(deg_start)
    rad_end = np.deg2rad(deg_end)

    if isinstance(num_points, (int, float)):
        num_points = [num_points]

    # Generation of the half-sine vector
    t = np.linspace(0, np.pi, num_points[0])
    RangeofMovement = rad_start + (rad_end - rad_start) * (1 - np.cos(t)) / 2

    return RangeofMovement


def saveMov(Movement):
    # Create directory for saving Movement if it doesn't exist
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PATH_SAVE = os.path.join(PROJECT_PATH, "syntheticData")
    os.makedirs(PATH_SAVE, exist_ok=True)

    # Save data to file
    PATH_SAVE_FILE = os.path.join(PATH_SAVE, "syntheticData.npy")
    np.save(PATH_SAVE_FILE, Movement)

    print(
        "\n [INFO] The synthetic dataset was successfully saved\n",
    )
