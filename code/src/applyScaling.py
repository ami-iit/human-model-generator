# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from urdfModifiers.core.linkModifier import LinkModifier
from urdfModifiers.core.jointModifier import JointModifier
from urdfModifiers.core.modification import Modification
from urdfModifiers.utils import *
from urdfModifiers.geometry import *


def setLinkLength(linkName, newLength, newRadius, newPosition, axis, geometries, robot):
    """
    Modifies the length, radius, position, and axis of a link in the URDF model.

    Args:
        linkName (str): Name of the link to be modified.
        newLength (float): New length of the link.
        newRadius (float): New radius of the link.
        newPosition (tuple): New position of the link in (x, y, z) format.
        axis (str): Axis along which to modify the link ('X', 'Y', or 'Z').
        geometries (str): Type of geometry associated with the link ('BOX', 'CYLINDER', or 'SPHERE').
        robot (Robot): Instance of the Robot object representing the URDF model.

    Returns:
        None
    """

    match axis:

        case "X":

            axis = geometry.Side.X

        case "Y":

            axis = geometry.Side.Y

        case "Z":

            axis = geometry.Side.Z

    Link_modifier = LinkModifier.from_name(linkName, robot, axis)
    Link_modifications = Modification()

    # Verify the geometry type
    match geometries:

        case "BOX":

            Link_modifications.add_dimension(newLength, absolute=True)

        case "CYLINDER":

            if newLength != None:

                Link_modifications.add_dimension(newLength, absolute=True)

            if newRadius != None:

                Link_modifications.add_radius(newRadius, absolute=True)

        case "SPHERE":

            Link_modifications.add_radius(newRadius, absolute=True)

    if newPosition != None:

        Link_modifications.add_position(newPosition, absolute=True)

    Link_modifier.modify(Link_modifications)


def setJointPosition(jointName, newJointPosition, axis, robot):
    """
    Modifies the position of a joint in the URDF model.

    Args:
        jointName (str): Name of the joint to be modified.
        newJointPosition (float): New position of the joint.
        axis (str): Axis along which to modify the joint ('X', 'Y', or 'Z').
        robot (Robot): Instance of the Robot object representing the URDF model.

    Returns:
        None
    """

    match axis:

        case "X":

            axis = geometry.Side.X

        case "Y":

            axis = geometry.Side.Y

        case "Z":

            axis = geometry.Side.Z

    joint_modifier = JointModifier.from_name(jointName, robot, axis)
    joint_modifications = Modification()
    joint_modifications.add_position(newJointPosition, absolute=True)
    joint_modifier.modify(joint_modifications)


def setMassPercentage(linkName, newMass, axis, robot):
    """
    Modifies the mass of a link in the URDF model.

    Args:
        linkName (str): Name of the link to be modified.
        newMass (float): New mass of the link.
        axis (str): Axis along which to modify the mass ('X', 'Y', or 'Z').
        robot (Robot): Instance of the Robot object representing the URDF model.

    Returns:
        None
    """
    match axis:

        case "X":

            axis = geometry.Side.X

        case "Y":

            axis = geometry.Side.Y

        case "Z":

            axis = geometry.Side.Z

    Link_modifier = LinkModifier.from_name(linkName, robot, axis)
    Link_modifications = Modification()
    Link_modifications.add_mass(newMass, absolute=True)
    Link_modifier.modify(Link_modifications)
