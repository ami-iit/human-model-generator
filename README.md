# Human Model Generator (HMG)

The Human Model Generator is a Python-based tool designed to generate anthropometric human whole-body models in the Unified Robot Description Format (URDF) standard, suitable in robotics for motion analysis and simulation applications.

## Introduction
Dynamics is a critical aspect in the study of human movement, encompassing the forces and torques that cause motion. The generation of movement is possible through the synergistic action of the nervous system and muscles. The nervous system sends signals to the muscles, which then contract and produce movement by exerting forces on the skeletal system. The intricate interaction between the skeletal system and muscles allows for complex and coordinated motions.
The musculoskeletal models offer a valuable approximation of the human anatomy and they are used extensively in fields like biomechanics, robotics, and computer simulations to study and mimic human movement. The muscle modeling is essential for a comprehensive understanding of the human movement. This involves the simulation of the behavior of muscles, including their activation patterns, force production, and interaction with the skeletal system. Accurate muscle models can predict how the whole-body movement and performance are affected by changes in muscle strength, coordination, and fatigue.  However, for a more accurate representation, additional data is required to customize models for different subjects, e.g., inertial parameters of body segments and anthropometric measurements.
Therefore, the goal of the HMG is to develop an advanced human model that integrates both skeletal and muscular information. This model does not only include detailed anatomical and inertial data but also it is scalable to accommodate the specific features of each human subject.

<p align="center">
<img src= https://github.com/ami-iit/human-model-generator/assets/116801366/ffb6bbd9-632a-4201-b7ee-dcb99a23fda2 width ="600" height="500">
</p>


## Dependencies 
This library requires the following dependencies:

- [``urdf-modifiers``](https://github.com/icub-tech-iit/urdf-modifiers)
- [``idyntree``](https://github.com/robotology/idyntree)

## Installation with [conda](https://docs.conda.io/en/latest/) (recommended)

- Create and activate a brand new enviroment
```
conda create -n human_model_env
conda activate human_model_env
```
- Install `urdf-modifiers` repository
```
git clone https://github.com/icub-tech-iit/urdf-modifiers.git
cd urdf-modifiers
pip install .
```
- Install idyntree following [this instructions](https://github.com/robotology/idyntree?tab=readme-ov-file#conda-recommended) 

## Usage
```
git clone https://github.com/ami-iit/human-model-generator.git
cd human-model-generator
```
- Open the file `config.py` with a text editor
- Manually modify the parameters according to the human subject anthropometric measurements (see file [INFO.md](INFO.md))
- Generate the model by running `python main.py` 
- A URDF model called `FileName.urdf` will be saved in the folder `models/humanModel`.
  
## Maintainers
* Lorenzo Fiori ([@LorenzoFiori](https://github.com/LorenzoFiori))
* Claudia Latella ([@claudia-lat](https://github.com/claudia-lat/claudia-lat))

## References
* De Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. Journal of biomechanics, 29(9), 1223-1230. [link](https://doi.org/10.1016/0021-9290(95)00178-6)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Adjustments to McConville et al. and Young et al. body segment inertial parameters. Journal of biomechanics, 40(3), 543-553. [link](https://doi.org/10.1016/j.jbiomech.2006.02.013)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Corrigendum to “Adjustments to McConville et al. and Young et al. body segment inertial parameters”[J. Biomech. 40 (2007) 543–553]. Journal of Biomechanics, 40(7), 1651-1652. [link](http://bibtexbib.free.fr/bibliographie_net/Dumas_2007_Corrigendum.pdf)
* Winter, D. A. (2009). Biomechanics and motor control of human movement. John wiley & sons. [link](https://books.google.it/books?hl=it&lr=&id=_bFHL08IWfwC&oi=fnd&pg=PR13&dq=Winter,+D.+A.+(2009).+Biomechanics+and+motor+control+of+human+movement.+John+wiley+%26+sons&ots=Jnprer8eP5&sig=wOJ3iIC8niVM8NxsKUsUAbgaTW8&redir_esc=y#v=onepage&q=Winter%2C%20D.%20A.%20(2009).%20Biomechanics%20and%20motor%20control%20of%20human%20movement.%20John%20wiley%20%26%20sons&f=false)
* Dumas, R., & Wojtusch, J. (2018). Estimation of the Body Segment Inertial Parameters for the Rigid Body Biomechanical Models Used in Motion Analysis. In: Müller B., Wolf S.(eds) Handbook of Human Motion. [link](https://hal.science/hal-02266177/)

