import os
import numpy as np


def linkPhysicallyConsistence(dynComp):
    Links = {}
    indxLinks = 1
    for indx in range(dynComp.model().getNrOfLinks()):
        if dynComp.model().getLink(indx).getInertia().isPhysicallyConsistent():
            Links[indxLinks] = dynComp.model().getLinkName(indx)
            # Links.append(dynComp.model().getLinkName(indx))
            indxLinks += 1

    return Links


def isPositiveDefinite(mass_mx):

    mass_mxNumpy = mass_mx.toNumPy()

    # Calculate the eigenvalues of the matrix
    # Checks whether all eigenvalues are positive
    eigvals = np.linalg.eigvals(mass_mxNumpy)
    eig = np.all(eigvals)
    if np.all(eig > 0):
        positivity = True
    else:
        positivity = False
        # print(np.linalg.eigvals(mass_mxNumpy))

    return positivity, mass_mxNumpy, eigvals
