## URDF Models

The Human Model Generator (HMG) model the human musculoskeletal system as a rigid multi-body system with 21 links connected by 18 joints and 22 muscles, 11 bilaterally, using their points of origin and insertion in the body. 
The modeling is done using simple geometric shapes like parallelepipeds, cylinders, and spheres or frames, which are automatically scaled based on anthropometric parameters like total height, total mass, and specific circumferences.

### Model types

There are two possible models that can be used in Human Model Generator, one is called `Dumas` and the other is `DeLeva` (see [here](https://github.com/ami-iit/human-model-generator/blob/ReorganizeCode/code/README.md) how to select them in the tool) . Each model has its own theoretical framework, a set of assumptions and techniques for handling the trunk's structure, as in example: 

 <img src="https://github.com/ami-iit/human-model-generator/assets/118193358/ec05cc8e-f8fc-4507-bd2c-ba5dfb4b3828" width="650" height="700">


 ## References
* De Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. Journal of biomechanics, 29(9), 1223-1230. [link](https://doi.org/10.1016/0021-9290(95)00178-6)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Adjustments to McConville et al. and Young et al. body segment inertial parameters. Journal of biomechanics, 40(3), 543-553. [link](https://doi.org/10.1016/j.jbiomech.2006.02.013)
* Dumas, R., Cheze, L., & Verriest, J. P. (2007). Corrigendum to “Adjustments to McConville et al. and Young et al. body segment inertial parameters”[J. Biomech. 40 (2007) 543–553]. Journal of Biomechanics, 40(7), 1651-1652. [link](http://bibtexbib.free.fr/bibliographie_net/Dumas_2007_Corrigendum.pdf)
* Winter, D. A. (2009). Biomechanics and motor control of human movement. John wiley & sons. [link](https://books.google.it/books?hl=it&lr=&id=_bFHL08IWfwC&oi=fnd&pg=PR13&dq=Winter,+D.+A.+(2009).+Biomechanics+and+motor+control+of+human+movement.+John+wiley+%26+sons&ots=Jnprer8eP5&sig=wOJ3iIC8niVM8NxsKUsUAbgaTW8&redir_esc=y#v=onepage&q=Winter%2C%20D.%20A.%20(2009).%20Biomechanics%20and%20motor%20control%20of%20human%20movement.%20John%20wiley%20%26%20sons&f=false)
* Dumas, R., & Wojtusch, J. (2018). Estimation of the Body Segment Inertial Parameters for the Rigid Body Biomechanical Models Used in Motion Analysis. In: Müller B., Wolf S.(eds) Handbook of Human Motion. [link](https://hal.science/hal-02266177/)
