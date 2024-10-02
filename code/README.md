   
## Configuration Parameters

Below are the parameters that can be manually modified to configure the model. These parameters allow you to set up the anthropometric characteristics and control options for the URDF model:

| Parameter        | Description                                                                                                                                 |  
|:----------------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| H                | Total height of the subject to be modelled [m].                                                                                             |
| m                | Total body mass of the subject to be modelled [Kg].                                                                                         |
| Neck [X]         | Diameter of the neck.                                                                                                                       |
| UpperTrunk [X]   | Depth of the upper trunk.                                                                                                                   |
| LowerTrunk [X]   | Depth of the lower trunk.                                                                                                                   |
| Pelvis [X]       | Depth of the pelvis.                                                                                                                        |
| Shoulder [X, Z]  | Width of the shoulder.                                                                                                                      |
| UpperArm [X, Z]  | Diameter of the upper arm.                                                                                                                  |
| ForeArm [X, Z]   | Diameter of the fore arm.                                                                                                                   |
| Hand [Z]         | Height of the hand.                                                                                                                         |
| Hand [X]         | Width of the hand.                                                                                                                          |
| UpperLeg [X, Y]  | Diameter of the upper leg.                                                                                                                  |
| LowerLegm [X, Y] | Diameter of the lower leg.                                                                                                                  |


## Additional Options

These options provide further customization for the model's consistency check, movement type, and visualization settings:

| Option                              | Value               | Description                                                  |
|:-----------------------------------:|:-------------------:|:-------------------------------------------------------------|
| OPT_CHECK_CONSISTENCY_MODEL         | `True` or `False`   | Check the consistency of the model.                          |
| OPT_VISUALIZZATION_MOVEMENT         | `True` or `False`   | Visualize the movement.                                      |
| OPT_VISUALIZZATION_MEASUREOFCONTROL | `True` or `False`   | Visualize the measure of control.                            |
| OPT_COLOR_LINK_MESH                 | `[R, G, B, alpha]`  | Defines the RGBA color of the link mesh for visualization.   |
| OPT_COLOR_MUSCLE_MESH               | `[R, G, B, alpha]`  | Defines the RGBA color of the muscle mesh for visualization. |


