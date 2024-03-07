   
Manually modify the following parameters:

| Parameter    | Description                                                                                                                                 |  
|:------------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Model        | type of model to be used based on different theoretical approaches: `DeLeva` (see De Leva, et. al 1996) or `Dumas` (see Dumas, et. al 2007) |
| FileName     | name of the file with which the .urdf model will be saved.                                                                                  |
| Control      | generates a table with estimated anthropometric measurements for each body segment: `On` or `Off`.                                          |
| H            | total height of the subject to be modelled [m].                                                                                             |
| m            | total body mass of the subject to be modelled [Kg].                                                                                         |
| Neck_x       |                                                                                                                                             |
| UpperTrunk_x |                                                                                                                                             |
| LowerTrunk_x |                                                                                                                                             |
| Pelvis_x     |                                                                                                                                             |
| Shoulder_x   |                                                                                                                                             |
| UpperArm_x   |                                                                                                                                             |
| ForeArm_x    |                                                                                                                                             |
| Hand_z       |                                                                                                                                             |
| Hand_x       |                                                                                                                                             |
| UpperLeg_x   |                                                                                                                                             |
| LowerLeg_x   |                                                                                                                                             |                                                                                      


   Please consider that the default configuration is the following

   ```
  Model    = 'DeLeva'# or 'Dumas'
  FileName = 'FileNames'
  Control  = "On" # or "On"

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