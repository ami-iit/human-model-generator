# human-model-generator

Dynamics is a significant aspect in the study of human movement. The generation of movement is possible due to the synergetic action of the nervous system and muscles, which is then implemented through the connection of the skeletal system with the muscles. The skeletal models used to date, such as the URDF model, are a good approximation of real human models; however, the inertial parameters of the body segment, as well as other anthropometric data required for customizing the model to individual subjects, and muscle modeling must be added to these. As a result, our goal is to generate a human model that includes skeletal and muscular informations and is scalable to each subject.

#

<p align="center">
<img src= https://github.com/ami-iit/human-model-generator/assets/116801366/ffb6bbd9-632a-4201-b7ee-dcb99a23fda2 width ="600" height="500">
</p>

#

# Dependencies

- [`python3`](https://wiki.python.org/moin/BeginnersGuide)
- [`urdf-modifiers`](https://github.com/icub-tech-iit/urdf-modifiers)

# Usage

### Configuration ###

 Into `GenerateModel.py` you can modify the following parameters:
 
| Parameters | The function of the parameter                                                                                                               |  
|:----------:|---------------------------------------------------------------------------------------------------------------------------------------------|
| H          | height of the subject to be modelled.                                                                                                       |
| m          | mass of the subject to be modelled.                                                                                                         |
| Model      | type of model to be used based on different theoretical approaches: `DeLeva` (see De Leva, et. al 1996) or `Dumas` (see Dumas, et. al 2007) |      
| Geometry   | the type of geometry to model the shoulder: `Cylinder` or  `Box`.                                                                           | 
| FileName   | name of the file with which the .urdf model will be saved.                                                                                  |
| Control    | generates a table with estimated anthropometric measurements for each body segment: `On` or `Off`.                                          |


#### Default configuration: ####

```
H        = 1.70
m        = 105
Model    = 'DeLeva'
Geometry = "Cylinder"
FileName = 'Subject_Name'
Control  = "On"
```

### Model Generator ###

In order to generate the model launch:

`Python src/GenerateModel.py`

The generated template is named `Subject_Name.urdf` and saved in the folder `models/humanModel`.

# Maintainers

* Lorenzo Fiori ([@LorenzoFiori](https://github.com/LorenzoFiori))
* Lorenzo Rapetti ([@lrapetti](https://github.com/lrapetti))

# References

* De Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. Journal of biomechanics, 29(9), 1223-1230. [link](https://doi.org/10.1016/0021-9290(95)00178-6)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Adjustments to McConville et al. and Young et al. body segment inertial parameters. Journal of biomechanics, 40(3), 543-553. [link](https://doi.org/10.1016/j.jbiomech.2006.02.013)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Corrigendum to “Adjustments to McConville et al. and Young et al. body segment inertial parameters”[J. Biomech. 40 (2007) 543–553]. Journal of Biomechanics, 40(7), 1651-1652. [link](http://bibtexbib.free.fr/bibliographie_net/Dumas_2007_Corrigendum.pdf)
* Winter, D. A. (2009). Biomechanics and motor control of human movement. John wiley & sons. [link](https://books.google.it/books?hl=it&lr=&id=_bFHL08IWfwC&oi=fnd&pg=PR13&dq=Winter,+D.+A.+(2009).+Biomechanics+and+motor+control+of+human+movement.+John+wiley+%26+sons&ots=Jnprer8eP5&sig=wOJ3iIC8niVM8NxsKUsUAbgaTW8&redir_esc=y#v=onepage&q=Winter%2C%20D.%20A.%20(2009).%20Biomechanics%20and%20motor%20control%20of%20human%20movement.%20John%20wiley%20%26%20sons&f=false)
* Dumas, R., & Wojtusch, J. (2018). Estimation of the Body Segment Inertial Parameters for the Rigid Body Biomechanical Models Used in Motion Analysis. In: Müller B., Wolf S.(eds) Handbook of Human Motion. [link](https://hal.science/hal-02266177/)
