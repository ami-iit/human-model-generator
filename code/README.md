   
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

![DSC06733-Enhanced-NR](https://github.com/user-attachments/assets/462c778c-62e2-423c-a258-e70337086599)
To measure the neck diameter, first measure the neck circumference at the base of the neck using a measuring tape. Then, calculate the diameter using the formula:

$d = \frac{\text{circumference}}{3.14}$

### Trunk Depth
![DSC06762-Enhanced-NR](https://github.com/user-attachments/assets/46ca71b0-409a-4279-a8f5-2e8e66544773)
To measure the depth of the trunk links, first measure the trunk depth at the level of the mesosternum. Then, perform the following operation:
$X = \frac{0.6 \times \text{depth}}{0.19}$

### Pelvis
![DSC06769-Enhanced-NR](https://github.com/user-attachments/assets/a9af5a2a-f6b5-4f4f-93b6-fa03a7ec48cc)
You can refer to the image for guidance on how to measure the pelvis depth. To do so, measure it at the height of the hip.

### Shoulder Height
To determine the shoulder height, position yourself in a T-pose and measure the distance as shown in the figure:
![DSC06756-Enhanced-NR](https://github.com/user-attachments/assets/c352de44-5d55-4d0b-9ce6-c49a2368474b)


### Upper Arm and Forearm 
![DSC06750-Enhanced-NR](https://github.com/user-attachments/assets/4502fff4-948d-4b0e-8547-cd14a8d4e6cd)
![DSC06753-Enhanced-NR](https://github.com/user-attachments/assets/175b7286-d4e3-44ad-b1a0-5e343a70213c)
Measure the circumference of the upper arm and forearm. Then, calculate the diameter using:

$d = \frac{\text{circumference}}{3.14}$

### Hand 
Refer to the image to see how to measure hand width and height.
![DSC06784-Enhanced-NR](https://github.com/user-attachments/assets/9f9dc0c3-941d-44cf-b2b7-41a428d54aa8)
![DSC06778-Enhanced-NR](https://github.com/user-attachments/assets/cfa03a50-a5d5-4a78-9136-43bdddaedb8d)


### Upper Leg and Lower Leg
![DSC06789-Enhanced-NR](https://github.com/user-attachments/assets/4bb6365b-5f1c-4c9a-be70-114835850823)
![DSC06801-Enhanced-NR](https://github.com/user-attachments/assets/eae2b492-dcbd-43c2-9ae4-0c7a64c47d70)

Measure the circumference of the upper leg and lower leg. For the upper leg, measure the circumference at mid-thigh. For the lower leg, measure the circumference at mid-calf. Then, compute the diameter as:

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


