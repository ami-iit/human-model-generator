   
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

### Neck
![Neck Measurement](path/to/neck_image.jpg)
To measure the neck diameter, first measure the neck circumference using a measuring tape. Then, calculate the diameter using the formula:

$d = \frac{\text{circumference}}{3.14}$

### Trunk Depth
![Trunk Measurement](path/to/trunk_image.jpg)
To measure the trunk depth, use the following formula:

$ X = \frac{0.6 \times \text{depth}}{0.19} $

### Pelvis
![Pelvis Measurement](path/to/pelvis_image.jpg)
Refer to the image to see how to measure the pelvis depth.

### Shoulder Width
![Shoulder Measurement](path/to/shoulder_image.jpg)
To determine the shoulder width, first measure the total trunk width. Then, compute the shoulder width using:

$ \text{Shoulder}[Z] = \frac{\text{trunk width}}{3} $

### Upper Arm and Forearm
![Upper Arm Measurement](path/to/upper_arm_image.jpg)
![Forearm Measurement](path/to/forearm_image.jpg)
Measure the circumference of the upper arm and forearm. Then, calculate the diameter using:

$d = \frac{\text{circumference}}{3.14}$

### Hand
Refer to the image to see how to measure hand width and height.
![Hand Measurement](path/to/hand_image.jpg)

### Upper Leg and Lower Leg
![Upper Leg Measurement](path/to/upper_leg_image.jpg)
![Lower Leg Measurement](path/to/lower_leg_image.jpg)
Measure the circumference of the upper leg and lower leg. Then, compute the diameter as:

$d = \frac{\text{circumference}}{3.14}$



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


