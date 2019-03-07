# HowTo Install the TJBot-Base on Raspberry Pi

This short installation guide will support you to set up an Raspberry PI v2/v3 with raspbian (most current) as a base to build the TjBot based on NodeRed.
Also you will update the node-red environment (nodejs, node-red, nodes) to the most current supported version to suport this demo.

## HW base for the TJBot

You will need for this installation following components

* Raspberry Pi v2/3 (including microUSB cable and powersupply)
* SD Card (at least 16GB needed)
* SenseHat [here](https://www.raspberrypi.org/products/sense-hat/)
* Speaker (chinch or Blouthooth)
* Raspberry Pi Camera module
* USB Mini Microphone dongle or USB Sound Card (for raspi) + Mic
* A body for your bot which can be laser cut or 3D printed see [here](https://ibmtjbot.github.io/)

## TJBot Credentials

After installation of this asset you will have a Raspberry Pi setup with all necessary components to run all of the TjBot use cases. To log on - you will need only following informations:

Hostname: ```tjbot-xxx``` (```.local```)
Username: ```pi```
Password: ```IbmTjBot```

## Installation

### Install Raspian od SD Card

1. Download current raspbian and install on SD Card (use web tutorials from raspbian to install the base)

2. Configure Raspbian (use raspi-config or GUI) with
* camera on
* I2C on
* VNC enabled
* SSH enabled
* right locale (like de/vienna)
* right timezone (like at/vienna)
* right wlan (like at)
* set default hostname to (tjbot-xx) where xx is your short name
* leave pi as your username or create a new user and work with this user
* set new default password
* reboot

3. upgrade raspbian and firmware to most current version
* sudo apt-get update
* sudo apt-get install
* sudo apt-get upgrade
* sudo apt-get dist-upgrade
* sudo reboot
* sudo rpi-update

4. install common used tools and addons (if needed - good selection might be)
* sudo apt install -y tightvncserver
* sudo apt install -y xrdp
* sudo apt install -y samba
* sudo reboot

### Install Node-Red TJBot Environment

1. upgrade nodejs to most recent supported version (with node-red update script)
* bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
* update-nodejs-and-nodered

2. check if tools are most current (for micro, sound, camera, ..)
* sudo apt-get install git
* sudo apt-get install python-picamera
* sudo apt-get install python-dev python-rpi.gpio
* sudo apt-get install alsa-base alsa-utils
* sudo apt-get install libasound2-dev

3. Config NodeJS (and fix permission errors)
* mkdir ~/.npm-global
* npm config set prefix '~/.npm-global'
* nano ~/.profile
    * export PATH=~/.npm-global/bin:$PATH
* source ~/.profile

4. install Node-Red base Nodes for TJBot NodeRed environment
* node-red-start
* node-red-stop
* ln -s ~/.node-red ~/node-red-data
* cd ~/node-red-data
* npm install -g node-red-admin
* npm install node-red-contrib-speakerpi
* npm install node-red-contrib-micropi
* npm install node-red-contrib-camerapi
* npm install node-red-contrib-cos
* npm install node-red-contrib-ibm-watson-iot
* npm install node-red-node-watson
* npm install node-red-dashboard
* npm install node-red-node-base64
* npm install node-red-node-pi-sense-hat
* npm install node-red-contrib-browser-utils
* npm install node-red-contrib-telegrambot
* npm install node-red-bluemix-nodes
* npm install node-red-contrib-python3-function
* npm install node-red-contrib-watson-machine-learning

4. Install SenseHat
* Put the SenseHat board on the Raspberry Pi
* nothing additional to install if you use it with NodeRed

5. Configure autostart of node-red
* sudo systemctl enable nodered.service

6. Update to the most current versions of all packages
* npm install -g npm-check-updates
* ncu -u
* npm install

### Install Microphone

1. Microphone and Sound settings
* Plug in the USB Sound Card or USB Microphone
* Config with alsamixer
  * alsamixer
  * sudo alsactl store
* Test with
  * arecord -D plughw:1,0 -d 3.0 test.wav && aplay test.wav

### Install Pi Camera

1. Test camerapi
* raspistill -o cam.jpg

## Configure NodeRed

* import all flows from TjBot-Flows
* setup on all tabs the credentials and configure the services well
* deploy

## Optional Assets

### Install SSH Autologin

1. SSH Autologin implementation (run from base system not raspi)
* ssh-keygen -t rsa
* ssh pi@tjbot-xx mkdir -p .ssh
* cat .ssh/id_rsa.pub | ssh pi@tjbot-xx 'cat >> .ssh/authorized_keys'

### Install nodejs Http-Server for Development

* npm install -g browser-sync
* browser-sync start --server --files "css/*.css"

### Install Pyhthon Envirnoment

* sudo apt install python3-dev python3-pip
* sudo pip3 install -U virtualenv
* virtualenv --system-site-packages -p python3 ./ai-env

Activate:

* source ./ai-env/bin/activate

Deactivate:

* deactivate

### Install Tensorflow within environment

* sudo apt install libatlas-base-dev
* pip install --upgrade pip
* pip -V
* pip install --upgrade tensorflow

### Install Tensorflow on Base-System

* sudo apt install libatlas-base-dev
* pip3 install --user --upgrade tensorflow  
* python3 -c "import tensorflow as tf; print(tf.__version__)"

### Install Kensas

* sudo apt-get install python3-numpy
* sudo apt-get install libblas-dev
* sudo apt-get install liblapack-dev
* sudo apt-get install python3-dev
* sudo apt-get install libatlas-base-dev
* sudo apt-get install gfortran
* sudo apt-get install python3-setuptools
* sudo apt-get install python3-scipy
* sudo apt-get update
* sudo apt-get install python3-h5py
* sudo pip3 install keras

### Install Pandas

* python3 -m pip install --upgrade pandas

### Install SciKit-Learn

* pip3 install -U scikit-learn

### Optional - Install Jupyter Notebooks

* sudo apt-get install python3-matplotlib
* sudo apt-get install python3-scipy
* sudo pip3 install --upgrade pip
* sudo pip3 install jupyter

[see](https://www.instructables.com/id/Jupyter-Notebook-on-Raspberry-Pi/)

### Optional - Install OpenCV

[see](https://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/)

## VisualStudio Code Addons (if needed)

1. VisualStudio Code with remote Access configuration
* Install Remote VSCode Plugin to VS Code
* Start an SSH Session to the remote host (RASPI)
  * ssh -R 52698:localhost:52698 pi@xxx.xxx.xxx.xxx
  * ssh -R 52698:localhost:52698 pi@tjbot-xx
* Install rmate on the RASPI
  * sudo wget -O /usr/local/bin/rmate https://raw.github.com/aurora/rmate/master/rmate
  * sudo chmod a+x /usr/local/bin/rmate
* Create an alias on Raspi
  * sudo nano ~/.bashrc
  * Fill in at the end
    * alias code='rmate -p 52698'

2. VisualStudio Code on Raspberry Pi (if needed)
* wget https://packagecloud.io/headmelted/codebuilds/gpgkey -O - | sudo apt-key add -
* curl -L https://code.headmelted.com/installers/apt.sh | sudo bash
* Start node-red locally again with inspection (debuggin local)
    * node-red-pi --max-old-space-size=256 --inspect

3. VisualStudio Code with remote Debug
* Create a launch.json in the debug pane
{
    // Remote Debugging of NodeRed
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "attach",
            "name": "Attach to Remote NodeRed",
            "address": "localhost",
            "port": 9221,
            "remoteRoot": null,
            "localRoot": null
        }
    ]
}
* Stop the current running NodeRed instance
    * node-red-stop
* Start again manually with for debugging
    * node-red-pi --max-old-space-size=256 --inspect
* ssh -L 9221:localhost:9229 pi@tjbot-xx


## Use of Docker

1. Install Docker core
* curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
* sudo groupadd docker
* sudo gpasswd -a $USER docker
* docker run hello-world

2. Install Docker Compose as a Docker
* docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:/rootfs/$PWD" \
    -w="/rootfs/$PWD" \
    docker/compose:1.13.0 up
* echo alias docker-compose="'"'docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:/rootfs/$PWD" \
    -w="/rootfs/$PWD" \
    docker/compose:1.13.0'"'" >> ~/.bashrc
* source ~/.bashrc

[docker install](https://medium.freecodecamp.org/the-easy-way-to-set-up-docker-on-a-raspberry-pi-7d24ced073e)

## Secure Node-Red

Best is when your local Node-Red is secure and also https is enabled. See here:
[secure](http://www.steves-internet-guide.com/securing-node-red-ssl/)

## See also Additional Documentation

1. TJBot * Original base
* [see](https://github.com/victordibia/tjwave)

2. additional tutorials
* [see](http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi/)
* [see](http://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)
* [see](http://tutorials-raspberrypi.com/library-installation-for-multiline-m-x-n-max7219-led-matrices/)
* [see](http://tutorials-raspberrypi.de/led-dot-matrix-zusammenbau-und-installation/)
* [see](http://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/)
* [see](https://www.sunfounder.com/wiki/index.php?title=To_use_USB_mini_microphone_on_Raspbian)
* [see](https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/)
* [see](https://www.tensorflow.org/install/install_raspbian)
* [see](https://medium.com/@abhizcc/installing-latest-tensor-flow-and-keras-on-raspberry-pi-aac7dbf95f2)
