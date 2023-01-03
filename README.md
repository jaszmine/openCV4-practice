# openCV4-practice
> Notes from the LinkedIn Learning Course: Intro to Deep Learning w/ OpenCV

### Concepts
* AI vs. ML vs. DL
* Training Networks
   * Hidden Layers
   * Weights
   * Loss Function
   * Back Propogation
* Pre-trained Networks

### Deep Learning Applications
* Image Classification
* Self-driving cars
* Handwriting transcription
* Speech recognition
* Language translation

### OpenCV
* An open-source computer vision and machine learning software library
* Applications
   * Facial recognition
   * Object identification
   * Human action classification
   * Camera movement tracking
* Natively written in C++, can use wrappers for Python and Java
* No framework-specific limitations
* An internal representation of models - can optimize code easier
* Has its own deep learning implementation - minimum external dependencies
* Uses BGR color format (instead of RGB)

### OpenCV's DNN
* Deep Neural Network Module
* NOT an entire deep learning framework
* Inference: 
   * When only a forward pass occurs (no back propgation so no default learning)
   * Engine example: input -> pretrained model -> result
   * Makes coding easier - no training means no GPUs needed
* OpenCV 4's DNN module supports:
   * Caffe
   * TensorFlow
   * Darknet
   * ONNX format 

### Setup

* Installed Python and Anaconda
* Setup Virtual Environment
   (In Anaconda Terminal)
   * Create: `conda create --name ocv4 python--3.6`
   * Activate: `activate ocv4`
   * Install cmake: `pip install cmake`
   * Install numpy: `pip install numpy`
   * Install OpenCV contrib module: `pip install opencv-contrib--python=-4.0.1.24`
   * Install dlib: `conda install -c conda-forge dlib` or `pip install dlib`
* Check if everything installed properly
  * Switch to python: `python` (command line should now start with `>>>`)
  * `import numpy`
  * `import cv2`
  * If nothing returns then it was done right :)

### Resources
* [OpenCV DNN module docs](https://docs.opencv.org/4.x/d2/d58/tutorial_table_of_content_dnn.html)
* [GH Deep Learning in OpenCV docs](https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV)
   
