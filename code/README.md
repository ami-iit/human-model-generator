   
## Configuration Parameters

Below are the parameters that can be manually modified to configure the model. These parameters allow you to set up the anthropometric characteristics and control options for the URDF model:
<div align="center">
   
| Parameter        | Description                                                                                                                                 |  
|:----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| H                | Total height [m]                                                                                             |
| m                | Total body mass [Kg]                                                                                         |
| Neck [X, Y]         | Diameter of the neck [m]                                                                                                                        |
| T8 [X] = T12 [X] =  L3 [X] =  L5 [X] | Depth of the trunk [m]                                                                                                                  |
| Pelvis [X]       | Depth of the pelvis [m]                                                                                                                      |
| Shoulder [Z]  | Width of the shoulder [m]                                                                                                                       |
| UpperArm [X, Z]  | Diameter of the upper arm [m]                                                                                                                   |
| ForeArm [X, Z]   | Diameter of the fore arm [m]                                                                                                                 |
| Hand [Z]         | Height of the hand [m]                                                                                                                          |
| Hand [X]         | Width of the hand [m]                                                                                                                         |
| UpperLeg [X, Y]  | Diameter of the upper leg [m]                                                                                                                 |
| LowerLeg  [X, Y] | Diameter of the lower leg [m]                                                                                                                 |

</div>


## How to measure:
Ensure to follow these guidelines carefully to obtain accurate measurements for configuring the model correctly.

![Neck](https://github.com/user-attachments/assets/956a0e95-e0f5-4947-ac4b-a1a08a11a04a)

![Neck (1)](https://github.com/user-attachments/assets/988fc378-c929-4dcb-9eaa-a4e9381f1a01)

![Neck (2)](https://github.com/user-attachments/assets/5a194839-7902-42c8-a628-4299d0b95dc6)

![Neck (3)](https://github.com/user-attachments/assets/8eb5ecf9-917d-4331-8104-c55cfc1e2157)

![Neck (4)](https://github.com/user-attachments/assets/017c068d-af08-4e0c-8685-84332ceeb6d0)

![Neck (5)](https://github.com/user-attachments/assets/7f3d53d7-2503-4159-8808-07521d563ea4)

![Neck (6)](https://github.com/user-attachments/assets/34fd78ca-86b8-4ea3-99f6-c8fe10d2827d)




## Additional Options

These options provide further customization for the model's consistency check, movement type, and visualization settings:
<div align="center">
   
| Option                              | Value               | Description                                                  |
|:-----------------------------------:|:-------------------:|:-------------------------------------------------------------|
| OPT_CHECK_CONSISTENCY_MODEL         | `True` or `False`   | Check the consistency of the model                         |
| OPT_VISUALIZZATION_MODEL            | `True` or `False`   | Visualize the movement                                      |
| OPT_VISUALIZZATION_MEASUREOFCONTROL | `True` or `False`   | Visualize the measure of control                           |
| OPT_VISUALIZATION_MESH | `True` or `False`   | Visualize the meshes of the model                           |
| OPT_VISUALIZATION_MUSCLES | `True` or `False`   | Visualize the muscles meshes of the model                           |
| OPT_VISUALIZATION_SPINALCORD | `True` or `False`   | Visualize the spinal cord meshes of the model                           |
| OPT_COLOR_LINK_MESH                 | `[R, G, B, alpha]`  | Defines the RGBA color of the link mesh for visualization, with alpha transparency factor   |
| OPT_COLOR_MUSCLE_MESH               | `[R, G, B, alpha]`  | Defines the RGBA color of the muscle mesh for visualization, with alpha transparency factor  |
| OPT_COLOR_SPINALCORD_MESH               | `[R, G, B, alpha]`  | Defines the RGBA color of the spinal cord mesh for visualization, with alpha transparency factor  |



</div>


