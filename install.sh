#!/bin/bash

sudo apt update
sudo apt install -y python3-evdev bluetooth bluez

sudo cp kb_passthrough.py /home/pi/
sudo cp ps5kbd.sh /home/pi/

sudo chmod +x /home/pi/ps5kbd.sh

sudo cp services/kbpassthrough.service /etc/systemd/system/
sudo cp services/btautoconnect.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable kbpassthrough.service
sudo systemctl enable btautoconnect.service

echo "Install complete"
