# Human Model Generator (HMG) [![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) 

The Human Model Generator is a Python-based tool designed to generate anthropometric human whole-body models in the Unified Robot Description Format (URDF) standard, suitable in robotics for motion analysis and simulation applications.

## Introduction
The movement of the human body is made possible through the synergistic action of the nervous, muscular, and skeletal systems. The nervous system sends signals to the muscles, causing them to contract and exert forces on the skeletal system. This intricate interaction between these systems enables complex and coordinated motions.
Musculoskeletal models offer a valuable approximation of the human anatomy and they are used extensively in fields like biomechanics, robotics, and computer simulations to study and mimic human movement. Muscle modeling is essential for a comprehensive understanding of human movement. This involves the simulation of the behavior of muscles, including their activation patterns, force production, and interaction with the skeletal system. Accurate muscle models can predict how whole-body movement and performance are affected by changes in muscle strength, coordination, and fatigue. However, for a more accurate representation, additional data is required to customize models for different subjects, such as inertial parameters of body segments and anthropometric measurements.
Therefore, the goal of the HMG is to develop an advanced human model that integrates both skeletal and muscular information. This model not only includes detailed anatomical and inertial data, but it is also scalable to accommodate the specific features of each human subject. The HMG also incorporates meshes for both the links and muscles, which are modeled to enhance the visual and physical representation of the human body.

![22 links (1)](https://github.com/user-attachments/assets/13402460-d29d-4040-b83a-a9c25f058eff)


## Dependencies 
This library requires the following dependencies:

- [``numpy``](https://github.com/numpy/numpy)
- [``urchin``](https://github.com/fishbotics/urchin)
- [``idyntree``](https://github.com/robotology/idyntree)
- [``urdf-modifiers``](https://github.com/icub-tech-iit/urdf-modifiers)

## Installation with [conda](https://docs.conda.io/en/latest/) (recommended)

Create and activate a brand new enviroment with the required dependencies:
```
conda create -n hmgenv python numpy urchin idyntree urdf-modifiers
conda activate hmgenv
```

## Usage
```
git clone https://github.com/ami-iit/human-model-generator.git
cd human-model-generator/code
```
- Open the file `config.py` with a text editor
- Manually modify the parameters according to the human subject anthropometric measurements (see [this file](https://github.com/ami-iit/human-model-generator/tree/main/code#readme))
- Generate the model by running `python main.py` 
- The URDF model will be saved in the folder `models/humanModels`

## Citing this work
If you find this work useful, please use the following bibtex as a reference:

```
@inproceedings{HMGsiamoc,
	title = {An automatic anthropometric model generation tool for scalable human whole-body musculoskeletal modeling},
	url = {https://doi.org/10.6092/unibo/amsacta/7898},
	doi = {10.6092/unibo/amsacta/7898},
	series = {Proceedings {SIAMOC}},
	booktitle = {Proceedings {XXIV} Congresso {SIAMOC} 2024},
	author = {Fiori, Lorenzo and Latella, Claudia and Tatarelli, Antonella and Pucci, Daniele},
	date = {2024}
}
```

## License
The meshes for the links are derived from the [Blendswap model](https://blendswap.com/blend/11604) under the [CC-BY license](https://creativecommons.org/share-your-work/cclicenses/), whereas the meshes for the muscles are derived from [BodyParts3D](https://lifesciencedb.jp/bp3d/?lng=en) and [Blendswap](https://blendswap.com/blend/26915), both under the [CC-BY-SA license](https://creativecommons.org/licenses/by-sa/2.0/deed.en).
All the meshes were trimmed, morphed, and totally or partially reconstructed to achieve the desired shape and topology.
