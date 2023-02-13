# **Speach emotion recognition** 
 
> A study of the customer database for the purpose of finding and analyzing the potential customers

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


## Technologies Used
- Python - version 3.8.0
- Jupyter notebook - version 1.0


## Features
- Deep Learning (CNN)

## Screenshots

| Architecture    |Accuracy of Training data   |Accuracy of Test data  |
|-----------|:-----:| -----:|
|Convolutional neural network (CNN) |  0,94     |   0,94    |


* **CNN (Architecture)**

![image3](https://github.com/vburlay/anw_feld_ba/raw/main/images/model.PNG ) 

* **CNN (Evaluation)**

![image4](https://github.com/vburlay/anw_feld_ba/raw/main/images/evaluation.PNG ) 


## Setup
You can install the package as follows:
```r
import pandas as pd
import numpy as np
import os
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
np.random.seed(42)
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_curve
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import  cross_val_score,cross_val_predict
#CNN
from keras.models import Sequential
import keras
from keras.layers import Dense
from keras.layers import Input, Flatten, Dropout, Activation
from keras.layers import Conv1D, MaxPooling1D, AveragePooling1D
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D,SpatialDropout1D
from keras.models import Model
```


## Usage
The result 0.94025 - 94 % is good but with preprocessing by clustering the accuracy can be improved. Clustering (K-Means) can be an efficient approach for dimensionality reduction but for this a pipeline has to be created that divides the training data into clusters 34 and replaces the data by their distances to this cluster 34 to apply a logistic regression model afterwards:
```r
pipeline = Pipeline([
    ("kmeans", KMeans(n_clusters = d)),
    ("log_reg", LogisticRegression(multi_class = 'ovr',
             class_weight = None, 
             solver= 'saga', 
             max_iter = 10000)),
])
```


## Project Status
Project is: _complete_ 


## Room for Improvement

- The data implemented in the analysis has a relatively small volume. This should be improved by the new measurements of the characteristics.
- It is also conceivable that the further number of new customer groups will be included in the analysis. In this way, the new characteristics of customers can make the results more meaningful.



## Contact
Created by [Vladimir Burlay](wladimir.burlay@gmail.com) - feel free to contact me!
