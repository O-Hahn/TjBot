#!/usr/bin/python3.5

from sense_hat import SenseHat
from subprocess import call
import os
import time
import math
import sys

call(["/home/pi/TJBot-python/kill-last.sh", str(os.getpid())])

sense = SenseHat()
sense.set_rotation(270)

g = 9.81  # m/s

ball = {
    'x': 5,
    'y': 5,
    'w': 12,
    'vx': 12,
    'vy': -12,
    'ax': 0,
    'ay': 0
}

last = []

lastms = time.time() * 1000.0

mult = 48/64
mult2 = 63/64

while True:
    gyro = sense.get_gyroscope()
    pitch = gyro['pitch']
    roll = gyro['roll']
    yaw = gyro['yaw']
    ms = time.time() * 1000.0
    dt = (ms - lastms) / 1000

    sys.stdout.write("\x1B[2K\rP {:6.2f}, R {:6.2f}, Y {:6.2f}".format(pitch, roll, yaw))

    deg = yaw
    rad = deg / 360 * 2 * math.pi
    axm = math.sin(rad)
    aym = math.cos(rad)

    ball['x'] += ball['vx'] * dt
    ball['y'] += ball['vy'] * dt

    ball['vx'] += ball['ax'] * dt
    ball['vy'] += ball['ay'] * dt

    ball['ax'] = ball['w'] * g * axm
    ball['ay'] = ball['w'] * g * aym

    if ball['x'] > 7:
        ball['x'] = 7
        ball['vx'] = -ball['vx'] * mult
        ball['vy'] *= mult2
    elif ball['x'] < 0:
        ball['x'] = 0
        ball['vx'] = -ball['vx'] * mult
        ball['vy'] *= mult2
    if ball['y'] > 7:
        ball['y'] = 7
        ball['vy'] = -ball['vy'] * mult
        ball['vx'] *= mult2
    elif ball['y'] < 0:
        ball['y'] = 0
        ball['vy'] = -ball['vy'] * mult
        ball['vx'] *= mult2

    pixels = [(0, 0, 255)] * 64

    num = 16
    same = True
    for obj in last[-16:-1]:
        num -= 1
        val = int(256 - num * 16)
        if val > 255:
            val = 255
        pixels[obj[0] + obj[1] * 8] = (val, val, 255 - val)
        if obj[0] != int(ball['x']) or obj[1] != int(ball['y']):
            same = False
        if num == 16:
            break
    pixels[int(ball['x']) + int(ball['y']) * 8] = (255, 0, 0)
    sense.set_pixels(pixels)
    last += [[int(ball['x']), int(ball['y'])]]
    lastms = ms
    time.sleep(1/50)

