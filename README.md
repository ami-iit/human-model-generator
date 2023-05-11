# human-model-generator
Software tool for generating and scaling human models.

# Dependencies
- [`python3`](https://wiki.python.org/moin/BeginnersGuide)
- [`urdf-modifiers`](https://github.com/icub-tech-iit/urdf-modifiers)

# Usage
#### Configuration ####

 Into `GenerateModel.py` you can modify the following parameters:

- Model:
	- `Dumas` see [Dumas, et. al 2007](https://www.sciencedirect.com/science/article/pii/S0021929006000728?via%3Dihub) (default)
	- `DeLeva` see [De Leva, et. al 1996](https://www.sciencedirect.com/science/article/pii/0021929095001786)

- Geometry:
	- `Box`(default)
	- `Cylinder`

- Height:
	- `H` (1.8 m default)

- Mass:
	- `m` (105 Kg default)

#### Model Generator ####

In order to generate the model launch:

`Python src/GenerateModel.py`

The generated template is named `humanModelGenerated.urdf` and saved in the folder `models/humanModelTemplate`.

# Maintainers

* Lorenzo Fiori ([@LorenzoFiori](https://github.com/LorenzoFiori))
* Lorenzo Rapetti ([@lrapetti](https://github.com/lrapetti))
