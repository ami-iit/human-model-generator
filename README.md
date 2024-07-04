# Human Model Generator (HMG) [![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) 

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
- Install `urdf-modifiers`
```
git clone https://github.com/icub-tech-iit/urdf-modifiers.git
cd urdf-modifiers
pip install .
```
- Install `idyntree` following [this instructions](https://github.com/robotology/idyntree?tab=readme-ov-file#conda-recommended) 

## Usage
```
git clone https://github.com/ami-iit/human-model-generator.git
cd human-model-generator
```
- Open the file `config.py` with a text editor
- Manually modify the parameters according to the human subject anthropometric measurements (see [this file](https://github.com/ami-iit/human-model-generator/blob/ReorganizeCode/code/src/INFO.md))
- Generate the model by running `python main.py` 
- A URDF model called `FileName.urdf` will be saved in the folder `models/humanModel`
  
## Maintainers
|[Lorenzo Fiori](https://www.iit.it/it/web/guest/people-details/-/people/lorenzo-fiori)|[Claudia Latella](https://www.iit.it/it/web/guest/people-details/-/people/claudia-latella)|          
|:-------------------------------------------------------:|:-------------------------------------------------------:| 
|<img src="https://avatars.githubusercontent.com/u/118193358?v=4" width="180">|<img src="https://avatars.githubusercontent.com/u/10923418?v=4" width="180">|
