import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import keras

from keras.layers import Dense, Dropout, Input, Conv2D,MaxPooling2D, Flatten
from keras.models import Model,Sequential

input_shape= (28,28,1)
num_classes = 2

model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()
