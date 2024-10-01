# Human Model Generator (HMG) [![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) 

The Human Model Generator is a Python-based tool designed to generate anthropometric human whole-body models in the Unified Robot Description Format (URDF) standard, suitable in robotics for motion analysis and simulation applications.

## Introduction
The movement of the human body is made possible through the synergistic action of the nervous, muscular, and skeletal systems. The nervous system sends signals to the muscles, causing them to contract and exert forces on the skeletal system. This intricate interaction between these systems enables complex and coordinated motions.
Musculoskeletal models offer a valuable approximation of the human anatomy and they are used extensively in fields like biomechanics, robotics, and computer simulations to study and mimic human movement. Muscle modeling is essential for a comprehensive understanding of human movement. This involves the simulation of the behavior of muscles, including their activation patterns, force production, and interaction with the skeletal system. Accurate muscle models can predict how whole-body movement and performance are affected by changes in muscle strength, coordination, and fatigue. However, for a more accurate representation, additional data is required to customize models for different subjects, such as inertial parameters of body segments and anthropometric measurements.
Therefore, the goal of the HMG is to develop an advanced human model that integrates both skeletal and muscular information. This model not only includes detailed anatomical and inertial data, but it is also scalable to accommodate the specific features of each human subject. The HMG also incorporates meshes for both the links and muscles, which are modeled to enhance the visual and physical representation of the human body.

<br>

<p align="center">
<img src= https://github.com/ami-iit/human-model-generator/assets/118193358/095c6a28-5dd8-4a73-a1ab-d2d5446c2e39 width ="650" height="500">
</p>

</br>

## Dependencies 
This library requires the following dependencies:

- [``idyntree``](https://github.com/robotology/idyntree)
- [``urdf-modifiers``](https://github.com/icub-tech-iit/urdf-modifiers)
- [``urchin``](https://github.com/fishbotics/urchin.git)

## Installation with [conda](https://docs.conda.io/en/latest/) (recommended)

- Create and activate a brand new enviroment
```
conda create -n human_model_env
conda activate human_model_env
```
- Install `idyntree` following [these instructions](https://github.com/robotology/idyntree?tab=readme-ov-file#conda-recommended) 
- Install `urdf-modifiers`
```
git clone https://github.com/icub-tech-iit/urdf-modifiers.git
cd urdf-modifiers
pip install .
```
- Install `urchin`
```
git clone https://github.com/fishbotics/urchin.git
cd urchin
git checkout traversaro-patch-1
pip install .
```

## Usage
```
git clone https://github.com/ami-iit/human-model-generator.git
cd human-model-generator/code
```
- Open the file `config.py` with a text editor
- Manually modify the parameters according to the human subject anthropometric measurements (see [this file](https://github.com/ami-iit/human-model-generator/blob/ReorganizeCode/code/README.md))
- Generate the model by running `python main.py` 
- The URDF model will be saved in the folder `models/humanModels`
  
## Maintainers
|[Lorenzo Fiori](https://www.iit.it/it/web/guest/people-details/-/people/lorenzo-fiori)|[Claudia Latella](https://www.iit.it/it/web/guest/people-details/-/people/claudia-latella)|          
|:-------------------------------------------------------:|:-------------------------------------------------------:| 
|<img src="https://avatars.githubusercontent.com/u/118193358?v=4" width="100">|<img src="https://avatars.githubusercontent.com/u/10923418?v=4" width="100">|

## License
The meshes for the links are derived from the [Blendswap model](https://blendswap.com/blend/11604) under the [CC-BY license](https://creativecommons.org/share-your-work/cclicenses/), whereas the meshes for the muscles are derived from [BodyParts3D](https://lifesciencedb.jp/bp3d/?lng=en) and [Blendswap](https://blendswap.com/blend/26915), both under the [CC-BY-SA license](https://creativecommons.org/licenses/by-sa/2.0/deed.en).
All the meshes were trimmed, morphed, and totally or partially reconstructed to achieve the desired shape and topology.
