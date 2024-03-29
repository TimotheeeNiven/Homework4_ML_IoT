# -*- coding: utf-8 -*-
"""eval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKeLZ7oHshfk9osY-b26JeHXa3_UslcS
"""

import numpy as np
from tensorflow.keras.models import load_model
# Google Collab Format for Loading File
data = np.load("/content/preprocess.npz")

# Extract dataset and labels
dataset = data['dataset']
labels = data['labels']

# Load the saved model
model = load_model("Homework4_ImageModel.h5")

# Evaluate the model
loss, accuracy = model.evaluate(dataset, labels)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)