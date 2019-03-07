# The IBM TjBot-FH-Education-Flows

This Asset is the base for a course on a university for applied science to cover the Sensor Events, IoTF for transmission, Watson Studio for getting insights and train Machine Learning modells, building virtual sensors and also utilizing models to predict.

Import all the Tabs you on your Node-Red on the Raspberry Pi. Because the necessary credentials could not automatically resolved, you have to configure each of the IBM Cloud services with the necessary credetials of your environment.

The Base Fows for the TjBot give you following possibilities:

## Tab1: Startup

Gets the IP adress from the Raspi and shows it to the SenseHAT during Startup.
It also saves into globals the necessary parameters (ip, appurl, ..) and also stores the faces for the senseHAT.

## Tab2: Eye simulation

The eye simulation could be triggered via HTTP endpoint (tjbot-xxx:1880/eye?eye=up) - with start, stop, up, down, left, right as messages. After the start - ther will be automatically a blinking eye.

## Tab3-Tab5: SenseHAT Demo

The senseHAT tab gets all sensor data (Environment like temp & hum), Motions, Joystick events and pushes them to the dashboard (if selected to be sent to Cloud). There is also a GUI representing the visualisation of the sensordata.

## Tab6: Motion-Detection

With this tab you can train or detect motions you are drawing in the air. In the train mode - you first select the digit (displayed on the senseHAT interface) by pushing up and down you can switch the digit. When ready you push the joystick and start the training of one digit. In the air draw the digit and at the end stop by pressing the joystick again. All the collected data points during the movement is sent via IoTF to the cloudant database for furter computation.

There is a corresponding Junyper Notebook for collecting, transforming and creation of an model based on these movements to detect the corresponding digit on each motionset.

When running in the detect mode- you will draw a digit in the air (movements) by starting and stopping with the joystick - and than the model will be called to do the right prediction of the detected motionset.

## Tab7: Image - Demo

Demonstration of the standard visual recognition service. Here you can catch up a foto from the raspicam, which is displayed on the dashboard. The vrs will then detect a face and gives back the age, the gender and a probability - which also will be shown. Also do some parts with local fotos to better training and progression.

## Tab8: Handwriting

The Handwriting demo takes a foto of written numbers and transform it into spoken digits by using the MNIST dataset for the training a ML model. The corresponding Junyper Notebook is also available.

# Education Links

[Educ](TjBot-FH-Education-Flows/Education-Links.md)