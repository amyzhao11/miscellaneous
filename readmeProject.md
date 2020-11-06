# DCGAN on OASIS data
I have implemented a DCGAN on OASIS brain MRI images.

Amy Zhao

43571806

## Introduction:
An important field within computer vision is medical imaging. However, it is often difficult to obtain a large sample of training images. Limitations to obtaining brain MRIs include: the low availability of participants, the time it takes to obtain and process high resolution MRI brain images, as well as the fact that participants have to stay still for long periods of time (whichkes it difficult to obtain a good image). Therefore it is useful to implement a generative adversarial network (GAN) that can be trained on existing brain MRIs and then if trained successfully, it can generate an infinite number of plausible brain MRIs. This would aid the training of computer vision techniques such as brain segmentation which would require much more expansive datasets that may otherwise not exist without many man-hours of medical imaging. 

In particular, I have implemented a deep convolutional generative adversarial network (DCGAN) with reference DCGAN specifications in the paper written by Radford, Metz and Chintala [1]. In the DCGAN, the use of convolutional layers allows higher quality feature mapping and recognition relative to the traditional GAN only connected by dense layers. In my GAN implementation, I followed specifications such as:
* using LeakyReLU in the discriminator
* using strided convolutions in the discriminator and fractional-strided convolutions in the generator
* using batchnorm in both the generator and discriminator
* remove fully connected hidden layers
* scaling training image pixel values from -1 to 1
* in LeakyReLU, the slope of the leak was set to 0.2
* using an Adam optimiser with learning rate of 0.0002 for both generator and discriminator (I used 0.0002 for the generator and 0.0001 for the discriminator)
* no pooling layers

I also did not follow several specifications as I found they either did not work or produced lower quality results:
* They suggested the use of a ReLU activation function in the generator, however, I found LeakyReLU worked better as I used noise inputs generated with mean=0, sd=1. They also suggested the use of a Tanh activation function in the final layer of the generator, however, I found my model worked better without any activation functions in the generator and discriminator.
* Instead of using a batch size of 128, I used a batch size of 10 (i.e. 10 real and 10 fake images in each batch). I found larger batch sizes would overload the GPU.
* The paper suggested the use of beta_1=0.5 for the Adam optimiser, however I found that using the default beta_1=0.9 worked fine.
* I decided to use a latent space of 256 instead of 100 for no real reason and this worked quite well
* For the Conv2DTranspose layers, when using the depicted kernel size of (5,5) with stride (2,2) (Figure 1 in [1]) I got very aliased generator images with grid artifacts. This was remedied by using a kernel size of (4,4) with stride (2,2)
* Also in reference to Figure 1 in [1], I tried using four fractionally-strided convolutions (Conv2DTranspose) layers with one convolutional layer after and ended up with mode collapse. My model was working and produced very high quality brain images (SSIM>0.6) however, my generator would only produce the same images regardless of the noise input. I later fixed this by using three Conv2DTranspose layers and two convolutional layers instead.
* I used dropout layers in my discriminator to make my discriminator learn more slowly. I did not try running the GAN without dropout layers so I'm not sure if this had any real effect, but the current model is quite effective.

## Data:
Data consists of all the non-segmented OASIS data (9664 training images, 544 test images, 1120 validation images). The size of these images are 256x256 and are greyscale.

## Model script
The model script contains 2 functions

### Generator
The generator generates 256 x 256 images and is designed to take an input noise vector with latent space of size 256. Batchnorm is used after every convolutional layer except the last one.

### Discriminator
The discriminator takes an input image size of 256 x 256 and returns one output value. Its main objective is to classify the input images as real or fake by trying to minimise its loss. Batchnorm is used after every convolutional layer except the last one. I also used dropout layers with a dropout of 0.4.

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
Here, I install all the relevant packages which include tensorflow and keras which are involved in the creation of the GAN model. I also installed numpy, PIL, glob and os to help with loading the training images into an array from a specific directory. Matplotlib was used for image visualisation and sys was used to check whether a GPU was available as GAN training requires a lot of computational power and I had a lot of trouble with GPU availability on the lab computers. I also call my generator and discriminator functions from modelscript.py.

### Loading the data
The OASIS dataset contains 6 folders, however, only 3 of those folders are relevant to this project as they contain non-segmented brain MRI images. These are:
⋅⋅*/keras_png_slices_train
⋅⋅*/keras_png_slices_test
⋅⋅*/keras_png_slices_validate
These images were loaded for each folder and then concatenated into a single variable containing all the images, there were a total of 11328 images.

### Preprocessing the data
As per the paper [1], I scaled the image pixel values so that they were between -1 and 1. 

### Loss functions and optimisers
The loss for the discriminator was defined as the sum of the binary crossentropy of classifying the real images and the binary crossentropy of classifying the fake images. The loss for the generator was defined as the binary crossentropy of fake images with real image labels. This means the loss for the generator is minimised if its generated images are classified as real.

I used the Adam optimiser with learning rate 0.0002 for the generator and a learning rate of 0.0001 for the discriminator as I found the generator loss was not growing as quickly as I would have liked when the discriminator learning rate was 0.0002.

### Training function
I defined a training function with gradient tape with help from the tensorflow website [2].

### Training the model
I used a batch size of 10 and ran my model for 200 epochs, this took about 6 hours. However, it would be sufficient to get decent images by running it for 20 or more epochs. The training data was shuffled and partitioned into 1133 batches (total number of images divided by batch size) using tf.data.Dataset.from_tensor_slices. 

I defined a training loop which feeds an image batch to the training function and also print the discriminator and generator loss at certain iterations as well as sample images from the generator so that the user can track its progress. 

#### Sample outputs
4th epoch:
![4th Epoch](https://github.com/amyzhao11/miscellaneous/blob/master/0411%20Epoch4%20batch0%20less%20g%20layers.png)

10th epoch:
![10th Epoch](https://github.com/amyzhao11/miscellaneous/blob/master/0411%20Epoch10%20batch0%20less%20g%20layers.png)

20th epoch:
![20th Epoch](https://github.com/amyzhao11/miscellaneous/blob/master/0411%20Epoch20%20batch0%20less%20g%20layers.png)

50th epoch:
![50th Epoch](https://github.com/amyzhao11/miscellaneous/blob/master/0411%20Epoch50%20batch0%20less%20g%20layers.png)

199th epoch:
![199th Epoch](https://github.com/amyzhao11/miscellaneous/blob/master/0411%20Epoch199%20batch700%20less%20g%20layers.png)

******insert images
### SSIM
After generating images from the trained generator, you can choose an image to calculate the SSIM for. This calculation involves iterating over the entire training set and calculating and storing the SSIM value. The maximum SSIM is then displayed along with the corresponding training image which is closest in structural similarity to the generated image. With 200 epochs, the SSIM should be above 0.64 with some images reaching 0.68.

******insert images

## Note
I have been committing for the past 2 weeks, however, on 05/11 I changed the title of my folder from "Project" to "GAN Project" since I thought it was too vague. I did not realise at the time that having a space in the name of my folder would make me unable to access the folder through the terminal, so I changed it back to "Project". Upon doing so, I have found that I am unable to see any commits I have made prior to this day but you can check with Wei that I have been committing during the in-person pracs. In addition to this, I tried pushing my folder to my repo but I kept getting errors saying that one of my files was too big. I deleted that file but I have continued to get that error since it is still saved in my commit history. 

[1] A. Radford, L. Metz, and S. Chintala, “Unsupervised Representation Learning with Deep Convolutional
Generative Adversarial Networks,” arXiv:1511.06434 [cs], Jan. 2016, arXiv: 1511.06434. [Online]. Available:
http://arxiv.org/abs/1511.06434

[2] TensorFlow, "Deep Convolutional Generative Adversarial Network", [Online]. Available: https://www.tensorflow.org/tutorials/generative/dcgan
