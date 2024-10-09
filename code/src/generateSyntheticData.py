import os
import numpy as np


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
