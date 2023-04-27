
def SetPathLoadAndSave (Geometry):


    match Geometry:
        case "Cylinder":
            urdf_path ="./models/humanModelTemplate/humanModelTemplate_shoulder_Cylinder.urdf"
        case "Box":
            urdf_path ="./models/humanModelTemplate/humanModelTemplate_shoulder_Box.urdf"
    
    output_file = "./models/humanModelTemplate/humanModel_test1.urdf"
    dummy_file = 'no_gazebo_plugins.urdf'

    return urdf_path, output_file ,dummy_file