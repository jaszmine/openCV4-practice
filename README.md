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
* Deep Learning Frameworks used
   * Caffe
   * Darknet
  
### File commands & outputs

Descripts
* 02_01: 
* 02_02:
* 02_03:
* 04_01:
* 04_02:
* 04_03: Classification for a video
* 04_04:
* 04_05: Classification for an image & video using YOLOv3

#### 04_03
* using dnn module as an inference engine for a video file
* command: `python video.py`
* output:
<img src="https://media.giphy.com/media/D3mv7Mo9wT62lkQxz8/giphy.gif" alt="04_03 shoreVideo"	 style="width:500px;"/>

#### 04_05
* passing an image through the network using YOLOv3 (an object detection algorithm) w/ confidence threshold = 0.4
* command: `python yolo.py --image ../images/fruit.jpg`
* ouput: 
<img src="https://i.imgur.com/VceE9YS.png" alt="04_05 fruitOutput" style="width:500px;"/>

* passing a video through the network using YOLOv3 w/ confidence threshold = 0.4
* command: `python yolo.py --video ../images/restaurant.mov`
* output:
<img src="https://media.giphy.com/media/QzKa7KRSNToJSoQM2q/giphy.gif" width="500px" />

### Resources
* [OpenCV DNN module docs](https://docs.opencv.org/4.x/d2/d58/tutorial_table_of_content_dnn.html)
* [GH Deep Learning in OpenCV docs](https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV)
   
