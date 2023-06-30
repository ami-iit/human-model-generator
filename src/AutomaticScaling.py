from urdfModifiers.core.linkModifier import LinkModifier
from urdfModifiers.core.jointModifier import JointModifier
from urdfModifiers.core.modification import Modification
from urdfModifiers.utils import *
from urdfModifiers.geometry import *

#robot, gazebo_plugin_text = utils.load_robot_and_gazebo_plugins(urdf_path,dummy_file)

def Scaling_lenght (link_name,newlength,newradius,newposition,axis,geometries,robot):


    match axis:
        case "X":
            axis = geometry.Side.X
        case "Y":
            axis = geometry.Side.Y
        case "Z":
            axis = geometry.Side.Z    

    Link_modifier = LinkModifier.from_name(link_name, robot, axis)
    Link_modifications = Modification()


    #Verify the geometry type
    match geometries:
         case 'BOX':
             Link_modifications.add_dimension(newlength, absolute=True)
         case 'CYLINDER':
             if  newlength != None: 
                 Link_modifications.add_dimension(newlength, absolute=True) 
             if newradius != None:
                 Link_modifications.add_radius(newradius, absolute=True)              
         case 'SPHERE':
             Link_modifications.add_radius(newradius, absolute=True)

   
    
    if  newposition != None:        
        Link_modifications.add_position(newposition, absolute=True)   

    Link_modifier.modify(Link_modifications)

def Scaling_Joint_Position (joint_name,newjointposition,axis,robot):
    match axis:
        case "X":
            axis=geometry.Side.X
        case "Y":
            axis=geometry.Side.Y
        case "Z":
            axis=geometry.Side.Z

    joint_modifier = JointModifier.from_name(joint_name, robot, axis)
    joint_modifications = Modification()
    joint_modifications.add_position(newjointposition, absolute=True) 
    joint_modifier.modify(joint_modifications)

def Scaling_Percentage_Mass (link_name,newmass,axis,robot):

    match axis:
        case "X":
            axis=geometry.Side.X
        case "Y":
            axis=geometry.Side.Y
        case "Z":
            axis=geometry.Side.Z


    Link_modifier = LinkModifier.from_name(link_name,robot,axis)
    Link_modifications = Modification()
    Link_modifications.add_mass(newmass, absolute=True)     
    Link_modifier.modify(Link_modifications)

