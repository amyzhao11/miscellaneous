# DCGAN on OASIS data
I have decided to implement a DCGAN on OASIS brain MRI images.

## Data:
Data consists of all the non-segmented OASIS data (9664 training images, 544 test images, 1120 validation images). The size of these images are 256x256 and are greyscale.

## Driver script
### Loading the data

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

## Dependencies
python=3.7 scikit-learn jupyter notebook tensorflow-gpu matplotlib keras scikit-image
