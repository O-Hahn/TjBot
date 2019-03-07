# Install the IBM TjBot Visual-Recognition Environment

## Create Dog Model

1. Goto Tab - Train-Dogs

    - download all image files (zip files) to local computer (images directory)
    - [Create custom classifier](https://console.bluemix.net/docs/services/visual-recognition/tutorial-custom-classifier.html#creating-a-custom-model)
    - copy all zip files to raspberry
        - scp *.zip pi@tjbot-xx:/home/pi/Downloads/.
    - Start the inital flow (setup classifier)
    - Enhance the classifier (after model has been trained)

2. Train Service for face-recognition - Train-Fotos

    - create at least 3 librariers with different fotos (should contain 30 different pictures each)
    - call them xx.zip where xx is the name (short)
    - edit the setup of this tab to the right names and xx
    - start the creation flow on the tab
    - enhance with local pictures or with the cam on the node-red/ui