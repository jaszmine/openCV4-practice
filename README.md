# openCV4-practice <img src="https://i.imgur.com/0W1gjfx.png" alt="opencvLogo" style="float:right;width:70px;"/>
Image and video classification practice with OpenCV.  
<br>
**Frameworks**: DNN, Caffe, Darknet  
**Libraries/Modules**: cmake, numpy, OpenCV's config, and dlib  
**Algorithms**: YOLOv3  
<br>
> Note: still in the process of adding yolov3 weights and caffe model

<br>
<div id="btt"></div>

## Contents
* [Concepts Overview](#concepts)
* [Deep Learning Applications](#dlApps)
* [OpenCV Overview](#ocvOverview)
* [OpenCV's DNN](#ocvDNN)
* [DNN Process](#dnnProcess)
* [Setup/Installation](#setup)
* [File descriptions, commands, & outputs](#files)
* [Resources](#resources)

<br>
<div id="concepts"></div>

### Concepts
* AI vs. ML vs. DL
* Training Networks
   * Hidden Layers
   * Weights
   * Loss Function
   * Back Propogation
* Pre-trained Networks

[Back to top](#btt)

<br>
<div id="dlApps"></div>

### Deep Learning Applications
* Image Classification
* Self-driving cars
* Handwriting transcription
* Speech recognition
* Language translation

[Back to top](#btt)

<br>
<div id="ocvOverview"></div>

### OpenCV Overview
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

[Back to top](#btt)

<br>
<div id="ocvDNN"></div>

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

[Back to top](#btt)

<br>
<div id="dnnProcess"></div>
   
### DNN Process
* Load pre-trained models from other DL frameworks
* Pre-process images using blobFromImages()
* Pass blobs through loaded pre-trained model to get output predictions (blob -> model -> inference)
* Read the Model
   * `cv2.dnn.readNetFromCaffe(protext, caffeModel)`
   * loads models and weights
* Create a Four-Dimensional Blob
   * `blob = cv2.dnn.blobFromImage(image, [scalefactor], [size], [mean], [swapRB], [crop], [ddepth])`
* Input the Blob into the Network
   * `net.setInput(blob)`
* Forward pass throught the Network
   * `outp = net.forward()`
   * produces an output prediction after a forward pass
* Summary of steps
1.  images
2.  blobFromImage()
3.  Blob
4.  Trained Model
5.  Inference
   * Returns: 4D Tensor(NCHW) - # of images, # of channels, height, width
   
|blobFromImage() Parameter| Description |
|:-:|:--|
|image| Input image (1, 3, or 4 channels) |
|scalefactor| Multiplier for image values |
|size| Spatial size for output image |
|mean| Scalar with mean values that are subtracted from BGR channels |
|swapRB| Flag that swaps channels (from RGB to BGR) |
|crop| Flag to crop image after resize |
|ddepth| Depth of ouput blob (CV_32F or CV_8U) |

[Back to top](#btt)

<br>
<div id="setup"></div>

### Setup/Installation

* Install Python and Anaconda
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
* Deep Learning Frameworks used
   * OpenCV
   * Caffe
   * Darknet

[Back to top](#btt)

<br>
<div id="files"></div>
  
### File description, commands, & outputs

Descripts
* 02_01: Displays the 'devon.jpg' image & 3 intensity/grayscale channels
* 02_02: Displays the 'devon.jpg' image
* 02_03: Runs the 'shore.mov' video
* 04_01: Returns first few entries of 'synset_words.txt' file
* 04_02: Classification & Probability in an image
* 04_03: Classification & Probability in a video
* 04_04: Classification for an image & video using YOLOv3 w/ confThreshold=0.5
* 04_05: Classification for an image & video using YOLOv3 w/ confThreshold=0.4

#### 04_01
* command: `python image.py`
* output:
<img src="https://i.imgur.com/fh6QbCc.png" alt="04_05 fruitOutput" style="width:500px;"/>

#### 04_02
* command: `python image.py`
* output:
<img src="https://i.imgur.com/27uPelU.png" alt="04_05 fruitOutput" style="width:500px;"/>

#### 04_03
* using dnn module as an inference engine for a video file
* command: `python video.py`
* output:
<img src="https://media.giphy.com/media/D3mv7Mo9wT62lkQxz8/giphy-downsized.gif" alt="04_03 shoreVideo" width="500px"/>

#### 04_04 and 04_05 - images
* passing an image through the network using YOLOv3 (an object detection algorithm) w/ confidence threshold's =0.5 and =0.4
* command: `python yolo.py --image ../images/fruit.jpg`
* 04_04 output:
<img src="https://i.imgur.com/zKztq4C.png" alt="04_05 fruitOutput" style="width:500px;"/>
* 04_05 output: 
<img src="https://i.imgur.com/VceE9YS.png" alt="04_05 fruitOutput" style="width:500px;"/>

#### 04_05 - video
* passing a video through the network using YOLOv3 w/ confidence threshold = 0.4
* command: `python yolo.py --video ../images/restaurant.mov`
* output:
<img src="https://media.giphy.com/media/QzKa7KRSNToJSoQM2q/giphy.gif" width="500px" />

[Back to top](#btt)

<br>
<div id="resources"></div>

### Resources
* [OpenCV DNN module docs](https://docs.opencv.org/4.x/d2/d58/tutorial_table_of_content_dnn.html)
* [Deep Learning in OpenCV's GitHub Wiki](https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV)
* [Conda dlib docs](https://anaconda.org/conda-forge/dlib)
* [Caffe docs](http://caffe.berkeleyvision.org/)
* [Darknet docs](https://pjreddie.com/darknet/)
   
