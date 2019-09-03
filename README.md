[![Build Status](https://travis-ci.org/aik7/image_structure.svg?branch=master)](https://travis-ci.org/aik7/image_structure)

# Description

This code computes the following:

(1) INPUTS: a gray scale image and parameters

(2) Compute the 2D Fourier transform of the image

(3) Compute the radial average of the Fourier magnitude

(4) Fit a Gaussian about the peak magnitude

(5) OUTPUTS:

1. A file "structured_vectors.dat" containing the parameters and its pair of numbers (mean, sigma) corresponding to the mean and standard deviation of the Gaussian fit (data will be accumulated.)

2. A Gaussian-fit figure in png format

Ai modified [Anthony's code](https://github.com/adegenna/image_structure)
to save structured vectors for multiple input images.
You can just write a script to call this inverse solver multiple times
for different images and parameters.

## How to run  

```
python ./code/driver.py -input=./data/2D_N100_T2000_sig0.25_m0.4_size8_gray.npy -m=.4 -sig=0.25
```
