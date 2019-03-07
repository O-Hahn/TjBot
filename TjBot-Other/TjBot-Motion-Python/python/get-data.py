#!/usr/bin/python3.5

from sense_hat import SenseHat
import time


sense = SenseHat()

file = open('/home/pi/data.csv', mode='a')

while True:
    mode = input("Please enter Mode (c/i): ")
    if mode == '':
        break
    for n in range(0, 100):
        file.write(mode)
        for i in range(0, 25):
            data = sense.get_accelerometer_raw()
            file.write(';' + str(data['x']) + ';' + str(data['y']) + ';' + str(data['z']))
            print("X: {:6.3f}, Y: {:6.3f}, Z: {:6.3f}".format(data['x'], data['y'], data['z']))
        file.write('\r\n')
        file.flush()

file.close()
