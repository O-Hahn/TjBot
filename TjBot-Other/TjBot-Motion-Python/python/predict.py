#!/usr/bin/python3.5

from keras.models import load_model
from sense_hat import SenseHat
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from numpy import argmax
import sys
import pickle
import numpy as np
import pandas as pd
from keras.utils import np_utils


encoder = pickle.load(open('/home/pi/TJBot-python/encoder.pkl', 'rb'))

sense = SenseHat()

model = load_model('/home/pi/TJBot-python/model.h5')

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

