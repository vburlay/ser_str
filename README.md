# **Speach emotion recognition** 
 
![image1](https://github.com/vburlay/ser_str/raw/master/image/ser.PNG) 

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

Speach emotion recognition

## Technologies Used
- Python - version 3.8.0
- Jupyter notebook - version 1.0


## Features
- Deep Learning (Pytorch & Keras - ResNet34)
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


* **CNN (Evaluation)**

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
The result 0.94 (Pytorch)
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

- The data implemented in the analysis has a relatively small volume. This should be improved by the new measurements of the characteristics.
- It is also conceivable that the further number of new customer groups will be included in the analysis. In this way, the new characteristics of customers can make the results more meaningful.



## Contact
Created by [Vladimir Burlay](wladimir.burlay@gmail.com) - feel free to contact me!
