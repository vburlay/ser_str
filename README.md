# **Speach emotion recognition** 
 
![image1](https://github.com/vburlay/ser_str/raw/master/image/ser.PNG) 

> Emotion recognition from audio data using Deep Learning (Keras and Pytorch - ResNet34).
> Live demo [_here_](https://vburlay-ser-str-streamlit-demo-28yxvn.streamlit.app/).
## Table of Contents
* [Genelal Info](#general-nformation)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## General Information

> This project has two main objectives. One was to understand how to effectively speach emotion recognition based on deep learning, and the other was to determine a best approach to speach emotion recognition using deep learning. 
 > Data set: "Allstate Claim Prediction Challenge" comes from Kaggle [_here_](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio).

## Technologies Used
- Python - version 3.8.0
- Jupyter notebook - version 1.0
- Streamlit - version 1.18.0


## Features
- Deep Learning(Pytorch & Keras - ResNet34)
- Librosa(.wav -> .png)

## Screenshots
### Spectogram (.wav -> .png)

![image2](https://github.com/vburlay/ser_str/raw/master/image/spectogram.PNG)

| Architecture     | Accuracy of Training data | Accuracy of Test data |
|------------------|:-------------------------:|----------------------:|
| Pytorch ResNet34 |           0,98            |                  0,94 |
| Keras ResNet34   |           0,98            |                  0,84 |


* **ResNet23 (Keras)**

![image3](https://github.com/vburlay/ser_str/raw/master/image/model.PNG ) 

* **Learning rate**

![image4](https://github.com/vburlay/ser_str/raw/master/image/lernrate.PNG ) 


* **Pytorch Resnet34 (Evaluation)**

![image5](https://github.com/vburlay/ser_str/raw/master/image/matrix.PNG ) 


## Setup
You can install the package as follows:
```r
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import IPython.display as display
import numpy as np
import random
import librosa
import librosa.display
import tensorflow as tf
import torchvision
from torchvision import models, transforms
from pathlib import Path
from PIL import Image
from torch.utils.data import Dataset, DataLoader, TensorDataset
from sklearn.metrics import classification_report,confusion_matrix
import itertools
from sklearn.model_selection import StratifiedKFold
from google.colab import drive
import os
from torch.utils.tensorboard import SummaryWriter
from sklearn.model_selection import train_test_split
```


## Usage
The result 0.94 (Pytorch) but ResNet50 is better 
```r
    spec_resnet = models.resnet34(pretrained=True)

    for param in spec_resnet.parameters():
        param.requires_grad = False

        spec_resnet.fc = nn.Sequential(nn.Linear(spec_resnet.fc.in_features,500),
                               nn.ReLU(),
                               nn.Dropout(), nn.Linear(500,6))
        return spec_resnet
```


## Project Status
Project is: _complete_ 


## Room for Improvement

Training the models for the audio data posed various challenges. The customer neural network (Keras-Resnet34), which was initially created , achieved a relatively low and therefore unsatisfactory level of accuracy. By using transfer learning, an increase in accuracy could be achieved on the basis of the PyTorch-ResNet34, but the accuracy of the validation data set was still not satisfactory and the model had a strong tendency to overfitting. This phenomenon could be reduced by using image augmentation, but not yet eliminated.
Training the model for the audio data had to be done using Google Collab due to the heavy computational overhead, as a commercially available computer was no longer sufficient.


## Contact
Created by [Vladimir Burlay](wladimir.burlay@gmail.com) - feel free to contact me!
