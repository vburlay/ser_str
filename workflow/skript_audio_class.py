"""
Created on Sat Feb 03 21:41:46 2023

@author: Vladimir
"""
import os
import pandas as pd
import tensorflow as tf
import torch
import numpy as np
from torchvision import datasets, transforms
from pathlib import Path
from torch.utils.data import Dataset
import shutil


def check_wav(path):
    PATH_TO_FILE = Path.cwd() / path
    files = os.listdir(PATH_TO_FILE)
    newpath = PATH_TO_FILE / 'temp'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for file_name in files:
        full_file_name = os.path.join(PATH_TO_FILE, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, newpath)

    class_names = ['neutral', 'happy', 'sad', 'angry', 'fear', 'surprise']
    classification = []
    percentages_0 = []
    percentages_1 = []
    percentages_2 = []
    percentages_3 = []
    percentages_4 = []
    percentages_5 = []

    # load model
    model = torch.load('models/audio_model.pth')
    device = "cpu"

    image_transformed = transforms.Compose([transforms.Resize(255),
                                            transforms.CenterCrop(224),
                                            transforms.ToTensor(),
                                            transforms.Normalize([0.485, 0.456, 0.406],
                                                                 [0.229, 0.224, 0.225])])

    images = datasets.ImageFolder(PATH_TO_FILE, transform=image_transformed)
    image_loader = torch.utils.data.DataLoader(images, batch_size=1000)
    model.eval()
    images, labels = next(iter(image_loader))
    images, labels, model = images.to(device), labels.to(device), model.to(device)

    ps = torch.exp(model(images))
    top_p, top_class = ps.topk(1, dim=1)
    equals = top_class == labels.view(*top_class.shape)
    for i in range(0, len(top_class.tolist())):
        # classification.extend([str(top_class.tolist()[i][0])])

        score = tf.nn.softmax(ps.tolist()[i])
        classification.extend([class_names[np.argmax(score.numpy())]])
        percentages_0.extend([str(round(score.numpy()[0], 3))])
        percentages_1.extend([str(round(score.numpy()[1], 3))])
        percentages_2.extend([str(round(score.numpy()[2], 3))])
        percentages_3.extend([str(round(score.numpy()[3], 3))])
        percentages_4.extend([str(round(score.numpy()[4], 3))])
        percentages_5.extend([str(round(score.numpy()[5], 3))])

    for f in os.listdir(newpath):
        os.remove(os.path.join(newpath, f))
    os.rmdir(newpath)
    data = {'file': files, 'classification': classification, 'neutral': percentages_0,
            'happy': percentages_1, 'sad': percentages_2, 'angry': percentages_3,
            'fear': percentages_4, 'surprise': percentages_5}
    df_results = pd.DataFrame(data=data)
    return df_results



