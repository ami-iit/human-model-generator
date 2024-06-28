# Human-Model-Generator (HMG)

## Introduction
Dynamics is a critical aspect in the study of human movement, encompassing the forces and torques that cause motion. The generation of movement is made possible through the synergistic action of the nervous system and muscles. The nervous system sends signals to the muscles, which then contract and produce movement by exerting force on the skeletal system. This intricate interaction between the skeletal system and muscles allows for complex and coordinated motions.

Current skeletal models, such as the Unified Robot Description Format (URDF) model, offer a valuable approximation of human anatomy. These models are used extensively in fields like biomechanics, robotics, and computer simulations to study and replicate human movement. However, for a more accurate representation, especially when customizing models for individual subjects, additional data is required. This includes inertial parameters of body segments, which describe how mass is distributed throughout the body, and various anthropometric measurements that capture the unique dimensions and proportions of an individual.

Moreover, muscle modeling is essential for a comprehensive understanding of human movement. This involves simulating the behavior of muscles, including their activation patterns, force production, and interaction with the skeletal system. Accurate muscle models can predict how changes in muscle strength, coordination, or fatigue affect overall movement and performance.

Therefore, our goal is to develop an advanced human model that integrates both skeletal and muscular information. This model will not only include detailed anatomical and inertial data but also be scalable to accommodate the specific characteristics of each individual. By achieving this, we can enhance the precision and applicability of simulations and analyses in various applications, from clinical assessments to the development of prosthetics and robotics.

<p align="center">
<img src= https://github.com/ami-iit/human-model-generator/assets/116801366/ffb6bbd9-632a-4201-b7ee-dcb99a23fda2 width ="600" height="500">
</p>


## Dependencies 
This library requires the following dependencies

- [``urdf-modifiers``](https://github.com/icub-tech-iit/urdf-modifiers)
- [``idyntree``](https://github.com/robotology/idyntree)


## Usage

- Clone this repository: 

  ```
  git clone https://github.com/ami-iit/human-model-generator.git
  ```
- Go to the repository folder: 
  ```
  cd human-model-generator
  ```
- Open the file `src/main.py` with a text editor.
- Manually modify the parameters (see file [INFO.md](src/INFO.md)).
- Generate the model by running on the terminal: 
    ```
    python src/main.py
    ```
- A template called `FileName.urdf` will be saved in the folder `models/humanModel`.
  
## Maintainers
* Lorenzo Fiori ([@LorenzoFiori](https://github.com/LorenzoFiori))
* Claudia Latella ([@claudia-lat](https://github.com/claudia-lat/claudia-lat))

## References
* De Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. Journal of biomechanics, 29(9), 1223-1230. [link](https://doi.org/10.1016/0021-9290(95)00178-6)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Adjustments to McConville et al. and Young et al. body segment inertial parameters. Journal of biomechanics, 40(3), 543-553. [link](https://doi.org/10.1016/j.jbiomech.2006.02.013)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Corrigendum to “Adjustments to McConville et al. and Young et al. body segment inertial parameters”[J. Biomech. 40 (2007) 543–553]. Journal of Biomechanics, 40(7), 1651-1652. [link](http://bibtexbib.free.fr/bibliographie_net/Dumas_2007_Corrigendum.pdf)
* Winter, D. A. (2009). Biomechanics and motor control of human movement. John wiley & sons. [link](https://books.google.it/books?hl=it&lr=&id=_bFHL08IWfwC&oi=fnd&pg=PR13&dq=Winter,+D.+A.+(2009).+Biomechanics+and+motor+control+of+human+movement.+John+wiley+%26+sons&ots=Jnprer8eP5&sig=wOJ3iIC8niVM8NxsKUsUAbgaTW8&redir_esc=y#v=onepage&q=Winter%2C%20D.%20A.%20(2009).%20Biomechanics%20and%20motor%20control%20of%20human%20movement.%20John%20wiley%20%26%20sons&f=false)
* Dumas, R., & Wojtusch, J. (2018). Estimation of the Body Segment Inertial Parameters for the Rigid Body Biomechanical Models Used in Motion Analysis. In: Müller B., Wolf S.(eds) Handbook of Human Motion. [link](https://hal.science/hal-02266177/)

