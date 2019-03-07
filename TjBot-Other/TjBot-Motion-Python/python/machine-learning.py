#!/usr/bin/python3.5

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras import backend as K
from sense_hat import SenseHat
from keras.utils import np_utils
from numpy import argmax
import sys
import pickle

sense = SenseHat()

#data = pd.read_csv('C:\\Users\\LORENZStechauner\\Desktop\\data.csv', sep=';', header=None).values
data = pd.read_csv('/home/pi/data.csv', sep=';', header=None).values

model = Sequential()
model.add(Dense(50))
model.add(Dense(25))
model.add(Dense(10))
model.add(Dense(2))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

X = data[:, 1:].astype(float)
y = data[:, 0]

encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)
pickle.dump(encoder, open('/home/pi/TJBot-python/encoder.pkl', 'wb'))
dummy_y = np_utils.to_categorical(encoded_y)

model.fit(X, dummy_y, epochs=20, verbose=0)

model.save('/home/pi/TJBot-python/model.h5')

X_sens = []

while True:
    X_sens.append([])
    for i in range(0, 25):
        data = sense.get_accelerometer_raw()
        X_sens[-1].append(data['x'])
        X_sens[-1].append(data['y'])
        X_sens[-1].append(data['z'])

    y_pred = model.predict(np.array([X_sens[-1]]), batch_size=5)
    #print(y_pred)
    #print(argmax(y_pred))
    status = encoder.inverse_transform(argmax(y_pred[0, :]))
    #print(status)
    sys.stdout.write(status)
    sys.stdout.flush()
    #sys.stdout.write('\x1B[2K\r' + str(pred) + " " + str(y_pred2))


#8A4D9BB880968356

