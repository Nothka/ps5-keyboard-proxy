# Troubleshooting

## Keyboard not typing on PS5

Check service status:

```bash
sudo systemctl status kbpassthrough.service
```

Restart service:

```bash
sudo systemctl restart kbpassthrough.service
```

---

## Bluetooth keyboard disconnects after reboot

Check Bluetooth connection:

```bash
bluetoothctl info YOUR_KEYBOARD_MAC
```

If `Connected: no`:

```bash
bluetoothctl
connect YOUR_KEYBOARD_MAC
```

---

## Raspberry Pi not detected by PS5

Check USB gadget mode:

```bash
lsmod | grep libcomposite
```

Check HID device:

```bash
ls -l /dev/hidg0
```

If missing, reboot Raspberry Pi:

```bash
sudo reboot
```

---

## Keyboard detected as mouse

List input devices:

```bash
cat /proc/bus/input/devices
```

Find correct keyboard event:

```bash
ls /dev/input/by-id/
```

Update `kb_passthrough.py` with correct event device.

---

## SSH connection reset

Sometimes restarting services may close SSH connection.

Reconnect:

```bash
ssh pi@ps5proxy.local
```

---

## Raspberry Pi hostname not found

Find device IP:

```bash
arp -a
```

Connect using IP:

```bash
ssh pi@192.168.X.X
```

---

## Bluetooth pairing issues

Remove and repair device:

```bash
bluetoothctl
remove YOUR_KEYBOARD_MAC
scan on
pair YOUR_KEYBOARD_MAC
trust YOUR_KEYBOARD_MAC
connect YOUR_KEYBOARD_MAC
```

---

## Check running services

```bash
sudo systemctl status kbpassthrough.service
sudo systemctl status btautoconnect.service
```

---

## Manual passthrough test

```bash
sudo python3 /home/pi/kb_passthrough.py
```

If working manually but not automatically, service configuration is incorrect.

---

## Reboot everything

```bash
sudo reboot
```
