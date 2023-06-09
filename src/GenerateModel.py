from Modifier import*

''' 
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| PARAMETERS | THE FUNCTION OF PARAMETERS                                                                                                                  |  
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| H          | height of the subject to be modelled.                                                                                                       |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| m          | mass of the subject to be modelled.                                                                                                         |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Model      | type of model to be used based on different theoretical approaches: `DeLeva` (see De Leva, et. al 1996) or `Dumas` (see Dumas, et. al 2007) |   
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|   
| Geometry   | the type of geometry to model the shoulder: `Cylinder` or  `Box`.                                                                           | 
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| FileName   | name of the file with which the .urdf model will be saved.                                                                                  |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| Control    | generates a table with estimated anthropometric measurements for each body segment: `On` or `Off`.                                          |
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|

'''
H=1.70
m=105
Model = 'DeLeva'# or 'Dumas'
Geometry = "Cylinder" # or 'Box'
FileName='Subject_Name'
Control="On" # or "Off"

ModelModifier (H,m,Model,Geometry,FileName,Control)
