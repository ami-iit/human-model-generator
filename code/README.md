   
## Configuration Parameters

Below are the parameters that can be manually modified to configure the model. These parameters allow you to set up the anthropometric characteristics and control options for the URDF model:

| Parameter    | Description                                                                                                                                 |  
|:------------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Model        | Type of model to be used based on different theoretical approaches: `DeLeva` (see De Leva, et. al 1996) or `Dumas` (see Dumas, et. al 2007) |
| H            | Total height of the subject to be modelled [m].                                                                                             |
| m            | Total body mass of the subject to be modelled [Kg].                                                                                         |
| Neck_x       | Diameter of the neck.                                                                                                                       |
| UpperTrunk_x | Depth of the upper trunk.                                                                                                                   |
| LowerTrunk_x | Depth of the lower trunk.                                                                                                                   |
| Pelvis_x     | Depth of the pelvis.                                                                                                                        |
| Shoulder_x   | Width of the shoulder.                                                                                                                      |
| UpperArm_x   | Diameter of the upper arm.                                                                                                                  |
| ForeArm_x    | Diameter of the fore arm.                                                                                                                   |
| Hand_z       | Height of the hand.                                                                                                                         |
| Hand_x       | Width of the hand.                                                                                                                          |
| UpperLeg_x   | Diameter of the upper leg.                                                                                                                  |
| LowerLeg_x   | Diameter of the lower leg.                                                                                                                  |
|:------------:|---------------------------------------------------------------------------------------------------------------------------------------------|

## Additional Options

These options provide further customization for the model's consistency check, movement type, and visualization settings:

| Option                                | Value               | Description                        |
|:-------------------------------------:|:-------------------:|:-----------------------------------|
| OPT_CHECK_CONSISTENCY_MODEL           | `True` or `False`   | Check the consistency of the model.|
| OPT_TYPE_MOVEMENT                     | `physio` or `random`| Type of movement for the model.    |
| OPT_VISUALIZZATION_MOVEMENT           | `True` or `False`   | Visualize the movement.            |
| OPT_VISUALIZZATION_MEASUREOFCONTROL   | `True` or `False`   | Visualize the measure of control.  |
|:-------------------------------------:|:-------------------:|:-----------------------------------|
