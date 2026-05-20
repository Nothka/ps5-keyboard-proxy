# Setup Guide

## Requirements

- Raspberry Pi Zero 2 W
- microSD card
- USB OTG cable
- Bluetooth keyboard
- Raspberry Pi OS Lite

---

## Clone repository

```bash
git clone https://github.com/Nothka/ps5-keyboard-proxy.git
cd ps5-keyboard-proxy
```

---

## Install dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-evdev bluetooth bluez
```

---

## Enable USB HID gadget mode

Edit:

```bash
sudo nano /boot/firmware/config.txt
```

Add at the bottom:

```txt
dtoverlay=dwc2
```

---

Edit:

```bash
sudo nano /boot/firmware/cmdline.txt
```

Add after `rootwait`:

```txt
modules-load=dwc2,libcomposite
```

Do NOT create a new line.

---

## Reboot

```bash
sudo reboot
```

---

## Clone project on Raspberry Pi

```bash
git clone https://github.com/Nothka/ps5-keyboard-proxy.git
cd ps5-keyboard-proxy
```

---

## Run installer

```bash
chmod +x install.sh
sudo ./install.sh
```

---

## Pair Bluetooth keyboard

```bash
bluetoothctl
```

Inside bluetoothctl:

```txt
scan on
pair YOUR_KEYBOARD_MAC
trust YOUR_KEYBOARD_MAC
connect YOUR_KEYBOARD_MAC
```

---

## Reboot Raspberry Pi

```bash
sudo reboot
```

---

## Verify services

```bash
sudo systemctl status kbpassthrough.service
sudo systemctl status btautoconnect.service
```

---

## Done

Your Bluetooth keyboard should now work on PS5 through the Raspberry Pi Zero 2 W USB connection.
