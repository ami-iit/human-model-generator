import os

def SetPathLoadAndSave (Geometry,NameFile):


    match Geometry:
        case "Cylinder":
            urdf_path ="./models/humanModelTemplate/humanModelTemplate_shoulder_Cylinder.urdf"
        case "Box":
            urdf_path ="./models/humanModelTemplate/humanModelTemplate_shoulder_Box.urdf"
    
    dirPathSave = "./models/humanModels/"
    os.makedirs(dirPathSave,exist_ok=True)    
    output_file = dirPathSave + NameFile + '_humanModel.urdf'
    dummy_file = 'no_gazebo_plugins.urdf'

    return urdf_path, output_file ,dummy_file
