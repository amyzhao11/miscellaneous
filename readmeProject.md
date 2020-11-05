# DCGAN on OASIS data
I have decided to implement a DCGAN on OASIS brain MRI images.

Amy Zhao

43571806

## Introduction:
An important field within computer vision is medical imaging. However, it is often difficult to obtain a large sample of training images. Limitations to obtaining brain MRIs include: the low availability of participants, the time it takes to obtain and process high resolution MRI brain images, as well as the fact that participants have to stay still for long periods of time (whichkes it difficult to obtain a good image). Therefore it is useful to implement a generative adversarial network (GAN) that can be trained on existing brain MRIs and then if trained successfully, it can generate an infinite number of plausible brain MRIs. This would aid the training of computer vision techniques such as brain segmentation which would require much more expansive datasets that may otherwise not exist without many man-hours of medical imaging. 

In particular, I have implemented a deep convolutional generative adversarial network (DCGAN) with reference DCGAN specifications in the paper written by Radford, Metz and Chintala [1]. In the DCGAN, the use of convolutional layers allows higher quality feature mapping and recognition relative to the traditional GAN only connected by dense layers. In my GAN implementation, I followed specifications such as:
* using LeakyReLU in the discriminator
* using strided convolutions in the discriminator and fractional-strided convolutions in the generator
* using batchnorm in both the generator and discriminator
* remove fully connected hidden layers
* scaling training images from [-1,1]
* in LeakyReLU, the slope of the leak was set to 0.2
* using an Adam optimiser with learning rate of 0.0002 (I used 0.0002 for the generator and 0.0001 for the discriminator)

I also did not follow several specifications as I found they either did not work or produced lower quality results:
* They suggested the use of a ReLU activation function in the generator, however, I found LeakyReLU worked better as I used noise inputs generated with mean=0, sd=1. They also suggested the use of a Tanh activation function in the final layer of the generator, however, I found my model worked better without any activation functions in the generator and discriminator.
* Instead of using a batch size of 128, I used a batch size of 10 (i.e. 10 real and 10 fake images in each batch). I found larger batch sizes would overload the GPU.





## Data:
Data consists of all the non-segmented OASIS data (9664 training images, 544 test images, 1120 validation images). The size of these images are 256x256 and are greyscale.

## Driver script
### Dependencies
My driver script requires the following packages to be installed in the environment
* tensorflow-gpu (version 2.1)
* keras
* python (version 3.7)
* jupyter notebook
* scikit-image
* matplotlib

### Package installation
Here, I install all the relevant packages which include tensorflow and keras which are involved in the creation of the GAN model. I also installed numpy, PIL, glob and os to help with loading the training images from a specific directory. Matplotlib was used for image visualisation and sys was used to check whether a GPU was available as GAN training requires a lot of computational power and I would have trouble with GPU availability on the lab computers. I also call my generator and discriminator functions form modelscript.py.

### Loading the data
The OASIS dataset contains 6 folders, however, only 3 of those folders are relevant to this project as they contain non-segmented brain MRI images. These are:
⋅⋅*/keras_png_slices_train
⋅⋅*/keras_png_slices_test
⋅⋅*/keras_png_slices_validate

### Preprocessing the data

### Training the model

### SSIM

## Model script
The model script contains 3 functions

### Generator

### Discriminator

### GAN
1. The read me file should contain a title, a description of the algorithm and the problem that it solves
(approximately a paragraph), how it works in a paragraph and a figure/visualisation.
2. It should also list any dependencies required
3. provide example outputs and plots of your algorithm code
4. The read me file should be properly formatted using GitHub markdown
5. describe and justify your training, validation and testing split of the data.
Marking Criteria
1. description and explanation of the working principles of the algorithm implemented and the problem it
solves (5 Marks)
2. description of usage and comments throughout scripts (3 Marks)
3. proper formatting using GitHub markdown (2 Mark)



## Note
I have been committing for the past 2 weeks, however, on 05/11 I changed the title of my folder from "Project" to "GAN Project" since I thought it was too vague. I did not realise at the time that having a space in the name of my folder would make me unable to access the folder through the terminal, so I changed it back to "Project". Upon doing so, I have found that I am unable to see any commits I have made prior to this day but you can check with Wei that I have been committing during the in-person pracs. In addition to this, I tried pushing my folder to my repo but I kept getting errors saying that one of my files was too big. I deleted that file but I have continued to get that error since it is still saved in my commit history. 

[1] A. Radford, L. Metz, and S. Chintala, “Unsupervised Representation Learning with Deep Convolutional
Generative Adversarial Networks,” arXiv:1511.06434 [cs], Jan. 2016, arXiv: 1511.06434. [Online]. Available:
http://arxiv.org/abs/1511.06434
