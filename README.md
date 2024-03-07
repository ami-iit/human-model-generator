# human-model-generator

Dynamics is a significant aspect in the study of human movement. The generation of movement is possible due to the synergetic action of the nervous system and muscles, which is then implemented through the connection of the skeletal system with the muscles. The skeletal models used to date, such as the URDF model, are a good approximation of real human models; however, the inertial parameters of the body segment, as well as other anthropometric data required for customizing the model to individual subjects, and muscle modeling must be added to these. As a result, our goal is to generate a human model that includes skeletal and muscular informations and is scalable to each subject.

<p align="center">
<img src= https://github.com/ami-iit/human-model-generator/assets/116801366/ffb6bbd9-632a-4201-b7ee-dcb99a23fda2 width ="600" height="500">
</p>


## Dependencies
- [`python3`](https://wiki.python.org/moin/BeginnersGuide)
- [`urdf-modifiers`](https://github.com/icub-tech-iit/urdf-modifiers)

## Usage
- Clone this repository
  ```
  git clone https://github.com/ami-iit/human-model-generator.git
  cd human-model-generator
  ```
- Open the file `src/generateModels.py` with a text editor.
- Manually modify the parameters.
- Generate the model by running on the terminal `Python src/generateModels.py`.
- A template called `FileName` + `.urdf` will be saved in the folder `models/humanModel`.

## Maintainers

* Lorenzo Fiori ([@LorenzoFiori](https://github.com/LorenzoFiori))
* Claudia Latella ([@claudia-lat](https://github.com/claudia-lat/claudia-lat))

## References

* De Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. Journal of biomechanics, 29(9), 1223-1230. [link](https://doi.org/10.1016/0021-9290(95)00178-6)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Adjustments to McConville et al. and Young et al. body segment inertial parameters. Journal of biomechanics, 40(3), 543-553. [link](https://doi.org/10.1016/j.jbiomech.2006.02.013)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Corrigendum to “Adjustments to McConville et al. and Young et al. body segment inertial parameters”[J. Biomech. 40 (2007) 543–553]. Journal of Biomechanics, 40(7), 1651-1652. [link](http://bibtexbib.free.fr/bibliographie_net/Dumas_2007_Corrigendum.pdf)
* Winter, D. A. (2009). Biomechanics and motor control of human movement. John wiley & sons. [link](https://books.google.it/books?hl=it&lr=&id=_bFHL08IWfwC&oi=fnd&pg=PR13&dq=Winter,+D.+A.+(2009).+Biomechanics+and+motor+control+of+human+movement.+John+wiley+%26+sons&ots=Jnprer8eP5&sig=wOJ3iIC8niVM8NxsKUsUAbgaTW8&redir_esc=y#v=onepage&q=Winter%2C%20D.%20A.%20(2009).%20Biomechanics%20and%20motor%20control%20of%20human%20movement.%20John%20wiley%20%26%20sons&f=false)
* Dumas, R., & Wojtusch, J. (2018). Estimation of the Body Segment Inertial Parameters for the Rigid Body Biomechanical Models Used in Motion Analysis. In: Müller B., Wolf S.(eds) Handbook of Human Motion. [link](https://hal.science/hal-02266177/)
