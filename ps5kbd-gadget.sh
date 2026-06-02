#!/bin/bash
set -e

modprobe libcomposite

if ! mountpoint -q /sys/kernel/config; then
  mount -t configfs none /sys/kernel/config
fi

cd /sys/kernel/config/usb_gadget/

if [ -d ps5kbd ]; then
  echo "" > ps5kbd/UDC 2>/dev/null || true
  rm -f ps5kbd/configs/c.1/hid.usb0 2>/dev/null || true
  rmdir ps5kbd/functions/hid.usb0 2>/dev/null || true
fi

mkdir -p ps5kbd
cd ps5kbd

echo 0x1d6b > idVendor
echo 0x0104 > idProduct
echo 0x0100 > bcdDevice
echo 0x0200 > bcdUSB

mkdir -p strings/0x409
echo "1234567890" > strings/0x409/serialnumber
echo "Generic" > strings/0x409/manufacturer
echo "USB Keyboard" > strings/0x409/product

mkdir -p configs/c.1/strings/0x409
echo "Config 1" > configs/c.1/strings/0x409/configuration
echo 120 > configs/c.1/MaxPower

mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length

printf '\x05\x01\x09\x06\xa1\x01\x05\x07\x19\xe0\x29\xe7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x01\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03\x91\x01\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xc0' > functions/hid.usb0/report_desc

ln -sf functions/hid.usb0 configs/c.1/

UDC_DEVICE=$(ls /sys/class/udc | head -n 1)

if [ -z "$UDC_DEVICE" ]; then
  echo "No USB Device Controller found. Make sure dtoverlay=dwc2,dr_mode=peripheral is under [all] in /boot/firmware/config.txt."
  exit 1
fi

echo "$UDC_DEVICE" > UDC
