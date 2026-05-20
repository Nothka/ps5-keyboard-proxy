# PS5 Keyboard Proxy

Bluetooth keyboard to USB HID proxy for PS5 using Raspberry Pi Zero 2 W.

## Features

- Bluetooth keyboard passthrough
- USB HID gadget mode
- PS5 compatible
- Auto reconnect on boot
- Systemd services
- Automatic keyboard detection
- Low latency input

## Hardware

- Raspberry Pi Zero 2 W
- microSD card
- USB OTG cable
- Bluetooth keyboard

## Architecture

Bluetooth Keyboard
        ↓
 Raspberry Pi Zero 2 W
        ↓
 USB HID Gadget
        ↓
       PS5

## Installation

### Clone repository

```bash
git clone https://github.com/Nothka/ps5-keyboard-proxy.git
cd ps5-keyboard-proxy
