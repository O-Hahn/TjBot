# Grove Pi as a possible Education Base

## Install toolkit when using GrovePi education board instead of SenseHat

1. install GrovePi+ Enhancements (if used as base)

[see](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/)

* cd ~
* mkdir Git
* cd Git
* git clone https://github.com/DexterInd/GrovePi
* cd GrovePi/Script
* sudo chmod +x install.sh
* sudo ./install.sh

2. Check grovepi+ board

* sudo i2cdetect -y 1
  * if brings 04 * means that grovepi+ board has been detected

3. test green light (plug into D4 the green light)

[see also](http://www.dexterindustries.com/GrovePi/engineering/python-library-documentation/)

* cd GrovePi/Software/Python
* python grove_led_blink.py

4. Additional Setup * Boot with LCD (placed on I2C-1) & IPAdresse on Display

* sudo apt-get install python-netifaces
* cd ~/Git
* git clone https://github.com/O-Hahn/RaspiTools.git

* Systemctl * Startup Script
  * sudo nano /lib/systemd/system/myinit.service

* Insert followin into the editor
	```
	[Unit]
	Description=My Startup Service
	After=multi-user.target

	[Service]
	Type=idle
	ExecStart=/usr/bin/python /home/pi/Git/RaspiTools/myinit.py

	[Install]
	WantedBy=multi-user.target
	```

* Make mystartup.py executable and insert into daemon
  * sudo chmod 644 /lib/systemd/system/myinit.service
  * sudo systemctl daemon-reload
  * sudo systemctl enable myinit.service

5. Install NPM Package on node-red-data

* cd ~/node-red-data
* npm install node-red-contrib-grovepi
