## URDF Models

The Human Model Generator (HMG) models the human musculoskeletal system as a rigid multi-body system with 23 links connected by 22 joints and 22 muscles, 11 bilaterally, using their points of origin and insertion in the body. The modeling is done using simple geometric shapes like parallelepipeds, cylinders, and spheres, which are automatically scaled based on anthropometric parameters like total height, total mass, and specific circumferences. Additional meshes have been added to model the spinal cord from the pelvis to the neck. A total of 67 meshes for links, muscles, and bones are added to the body to represent the structure more accurately.

To provide a clearer view of the model created, below are two images.
The first image highlights the meshes of the links and muscles, showing the general structure of the musculoskeletal system: 
![Progetto senza titolo (1)](https://github.com/user-attachments/assets/41c92839-3f1c-4390-a721-5de80bca9496)

The second image emphasizes the meshes of the spinal cord, from the pelvis to the neck, with a transparency effect applied to better distinguish this component within the model:
![Progetto senza titolo (2)](https://github.com/user-attachments/assets/498d9e4d-b485-4102-82d2-5e5220c84696)


 ## References
* De Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. Journal of biomechanics, 29(9), 1223-1230. [link](https://doi.org/10.1016/0021-9290(95)00178-6)
* Winter, D. A. (2009). Biomechanics and motor control of human movement. John wiley & sons. [link](https://books.google.it/books?hl=it&lr=&id=_bFHL08IWfwC&oi=fnd&pg=PR13&dq=Winter,+D.+A.+(2009).+Biomechanics+and+motor+control+of+human+movement.+John+wiley+%26+sons&ots=Jnprer8eP5&sig=wOJ3iIC8niVM8NxsKUsUAbgaTW8&redir_esc=y#v=onepage&q=Winter%2C%20D.%20A.%20(2009).%20Biomechanics%20and%20motor%20control%20of%20human%20movement.%20John%20wiley%20%26%20sons&f=false)
* Frostell, A., Hakim, R., Thelin, E. P., Mattsson, P., & Svensson, M. (2016). A review of the segmental diameter of the healthy human spinal cord. Frontiers in neurology, 7, 238. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC5179522/pdf/fneur-07-00238.pdf)
