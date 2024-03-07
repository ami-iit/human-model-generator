   
Manually modify the following parameters:

| Parameter    | Description                                                                                                                                 |  
|:------------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Model        | type of model to be used based on different theoretical approaches: `DeLeva` (see De Leva, et. al 1996) or `Dumas` (see Dumas, et. al 2007) |
| FileName     | name of the file with which the .urdf model will be saved.                                                                                  |
| Control      | generates a table with estimated anthropometric measurements for each body segment: `On` or `Off`.                                          |
| H            | total height of the subject to be modelled [m].                                                                                             |
| m            | total body mass of the subject to be modelled [Kg].                                                                                         |
| Neck_x       | Width of the Neck                                                                                                                           |
| UpperTrunk_x | Depth of the upper trunk                                                                                                                    |
| LowerTrunk_x | Depth of the lower trunk                                                                                                                    |
| Pelvis_x     | Depth of the pelvis                                                                                                                         |
| Shoulder_x   | Width of the shoulder                                                                                                                       |
| UpperArm_x   | Width of the upper arm                                                                                                                      |
| ForeArm_x    | Width of the fore arm                                                                                                                       |
| Hand_z       | Height of the hand                                                                                                                          |
| Hand_x       | Width of the hand                                                                                                                           |
| UpperLeg_x   | Width of the upper leg                                                                                                                      |
| LowerLeg_x   | Width of the lower leg                                                                                                                      |



   Please consider that the default configuration is the following

   ```
  Model    = 'DeLeva'
  FileName = 'FileNames'
  Control  = "On"

  ''' ANTHROPOMETRIC MEASUREMENTS''' 

  H            = 1.70
  m            = 100

  # some neck dimensions
  Neck_x       = 0.13

  # some trunk dimensions
  UpperTrunk_x = 0.25
  LowerTrunk_x = 0.25
  Pelvis_x     = 0.25

  # some arm dimensions
  Shoulder_x   = 0.115
  UpperArm_x   = 0.115
  ForeArm_x    = 0.085
  Hand_z       = 0.03
  Hand_x       = 0.08

  # some leg dimensions
  UpperLeg_x   = 0.16
  LowerLeg_x   = 0.11

   ```