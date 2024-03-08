
# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

import os

def setPathLoadAndSave (NameFile):

    """
    Set the paths for loading and saving the URDF model.

    Parameters:
    NameFile (str): Name of the file for the URDF model.

    Returns:
    tuple: A tuple containing three elements:
           - The path to load the URDF template model.
           - The path to save the modified URDF model.
           - The name of the dummy file.
    """

    urdf_path = "./models/humanModelTemplate/humanModelTemplate.urdf"

  
    dirPathSave = "./models/humanModels/"

    os.makedirs(dirPathSave,exist_ok=True)    
    
    output_file = dirPathSave + NameFile + '.urdf'
    dummy_file  = 'no_gazebo_plugins.urdf'

    return urdf_path, output_file ,dummy_file


