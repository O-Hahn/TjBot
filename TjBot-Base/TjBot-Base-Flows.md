# The IBM TjBot Base Flows

Inport all the Tabs you on your Node-Red on the Raspberry pi. Because the necessary credentials could not automatically resolved, you have to configure each of the IBM Cloud services with the necessary credetials of your environment.

The Base Fows for the TjBot give you following possibilities:

## Tab1: Startup

Gets the IP adress from the Raspi and shows it to the SenseHAT during Startup.
It also saves into globals the necessary parameters (ip, appurl, ..) and also stores the faces for the senseHAT.

## Tab2: SenseHAT

The senseHAT tab gets all sensor data (Environment like temp & hum) and pushes them to the dashboard.
It also contols the output of the SenseHAT like faces with emotions, eye simulation, bulb, ..

The eye simulation could be triggered via HTTP endpoint (tjbot-xxx:1880/eye?eye=up) - with start, stop, up, down, left, right as messages. After the start - ther will be automatically a blinking eye.

## Tab3: ReceiveIoTF

With this tab you can get commands from the cloud via IoTF and influence the behavior of the TjBot.

## Tab4: Image

Demonstration of the standard visual recognition service. Here you can catch up a foto from the raspicam, which is displayed on the dashboard. The vrs will then detect a face and gives back the age,, the gender and a probability - which also will be shown.

## Tab5: Speak

This is the demo of the translation and text to speech service. With the dialog on the dashboard you can enter a sentance and this will be translated and also spoken on the attached raspberry pi speaker.
The service will also use the approperiate language when the text is spoken.

Not all possible translations (from, to) are implemented.

Although there is a trival sentiment analyse on the given sentence. As if there is a good or bad shape - the senseHAT display will give a smily, frusty or a nutreal face.

## Tab6: Weather

This is the demonstration of the weather service from the IBM Cloud. You can enter a city from the dropbox - which will be translated into long/lat and than depending on the language you will get the forcast spoken on the speaker and also textual in the dashboard.