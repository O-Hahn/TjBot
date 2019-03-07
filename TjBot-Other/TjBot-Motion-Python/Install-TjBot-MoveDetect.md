
# TJBot Movement Detection
This is a short Readme for the TJBot. All files can be found in 
[this Box Folder](https://ibm.ent.box.com/folder/52956034129).

## Files

* ```python/```
  * ```predict.py``` - Loads model and writes state to ```stdout```
  * ```pong.py``` - Minigame with a ball and (basic) gravity
  * ```get-data.py``` - Collects data from SenseHat module and saves it
  * ```kill-last.sh``` - Kills all running ```pong.py``` processes
  * ```machine-learning.py``` - Trains and saves the model with collected data
* ```raspi.json``` - NodeRED Flow for Raspi
* ```cloud.json``` - NodeRED Flow for IBM Cloud

## Configuration

As Project Root I used ```/home/pi/TJBot-python/``` on the Raspi.
(Most file references in Python scripts are hardcoded -
change them if necessary) 

The Python scripts use following Python Libraries (and their dependencies):

* NumPy
* Pandas
* SenseHat
* SciKit Learn
* Keras
* TensorFlow

## NodeRED

The main NodeRED Flow is ```cloud.json```. It runs in the cloud and calls 
```raspi.json``` on the Raspi via the IBM Cloud Platform. The Raspi only
responses to these commands. The cloud-flow also hosts an UI Dashboard which 
displays the last taken photo. The main way for communication is the **Telegram API**.

Visual Recognition, Text to Speech,

## Interfaces

Refer to John's **Watson Assistant Workspace** to see, how Watson Assistant 
communicates with NodeRED.

The **Telegram API Key** should be easily changeable.

**IBM Cloud Platform** is needed to provide communication between the TJBot 
and the NodeRED flow in the cloud.
