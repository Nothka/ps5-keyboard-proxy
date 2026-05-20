import time
from evdev import InputDevice, ecodes, list_devices

kbd = None

for path in list_devices():
    dev = InputDevice(path)
    if "G915" in dev.name and "Keyboard" in dev.name:
        kbd = dev
        print("Using", dev.path, dev.name)
        break

if kbd is None:
    raise Exception("Keyboard not found")

hid = open("/dev/hidg0", "wb")

keymap = {
    ecodes.KEY_A: 0x04, ecodes.KEY_B: 0x05, ecodes.KEY_C: 0x06,
    ecodes.KEY_D: 0x07, ecodes.KEY_E: 0x08, ecodes.KEY_F: 0x09,
    ecodes.KEY_G: 0x0A, ecodes.KEY_H: 0x0B, ecodes.KEY_I: 0x0C,
    ecodes.KEY_J: 0x0D, ecodes.KEY_K: 0x0E, ecodes.KEY_L: 0x0F,
    ecodes.KEY_M: 0x10, ecodes.KEY_N: 0x11, ecodes.KEY_O: 0x12,
    ecodes.KEY_P: 0x13, ecodes.KEY_Q: 0x14, ecodes.KEY_R: 0x15,
    ecodes.KEY_S: 0x16, ecodes.KEY_T: 0x17, ecodes.KEY_U: 0x18,
    ecodes.KEY_V: 0x19, ecodes.KEY_W: 0x1A, ecodes.KEY_X: 0x1B,
    ecodes.KEY_Y: 0x1C, ecodes.KEY_Z: 0x1D,

    ecodes.KEY_1: 0x1E, ecodes.KEY_2: 0x1F, ecodes.KEY_3: 0x20,
    ecodes.KEY_4: 0x21, ecodes.KEY_5: 0x22, ecodes.KEY_6: 0x23,
    ecodes.KEY_7: 0x24, ecodes.KEY_8: 0x25, ecodes.KEY_9: 0x26,
    ecodes.KEY_0: 0x27,

    ecodes.KEY_ENTER: 0x28,
    ecodes.KEY_ESC: 0x29,
    ecodes.KEY_BACKSPACE: 0x2A,
    ecodes.KEY_TAB: 0x2B,
    ecodes.KEY_SPACE: 0x2C,

    ecodes.KEY_MINUS: 0x2D,
    ecodes.KEY_EQUAL: 0x2E,
    ecodes.KEY_LEFTBRACE: 0x2F,
    ecodes.KEY_RIGHTBRACE: 0x30,
    ecodes.KEY_BACKSLASH: 0x31,
    ecodes.KEY_SEMICOLON: 0x33,
    ecodes.KEY_APOSTROPHE: 0x34,
    ecodes.KEY_GRAVE: 0x35,
    ecodes.KEY_COMMA: 0x36,
    ecodes.KEY_DOT: 0x37,
    ecodes.KEY_SLASH: 0x38,

    ecodes.KEY_F1: 0x3A, ecodes.KEY_F2: 0x3B, ecodes.KEY_F3: 0x3C,
    ecodes.KEY_F4: 0x3D, ecodes.KEY_F5: 0x3E, ecodes.KEY_F6: 0x3F,
    ecodes.KEY_F7: 0x40, ecodes.KEY_F8: 0x41, ecodes.KEY_F9: 0x42,
    ecodes.KEY_F10: 0x43, ecodes.KEY_F11: 0x44, ecodes.KEY_F12: 0x45,

    ecodes.KEY_RIGHT: 0x4F,
    ecodes.KEY_LEFT: 0x50,
    ecodes.KEY_DOWN: 0x51,
    ecodes.KEY_UP: 0x52,
}

modmap = {
    ecodes.KEY_LEFTCTRL: 0x01,
    ecodes.KEY_LEFTSHIFT: 0x02,
    ecodes.KEY_LEFTALT: 0x04,
    ecodes.KEY_LEFTMETA: 0x08,
    ecodes.KEY_RIGHTCTRL: 0x10,
    ecodes.KEY_RIGHTSHIFT: 0x20,
    ecodes.KEY_RIGHTALT: 0x40,
    ecodes.KEY_RIGHTMETA: 0x80,
}

pressed = []
mods = 0

def send_report():
    report = bytearray(8)
    report[0] = mods

    for i, key in enumerate(pressed[:6]):
        report[2 + i] = key

    hid.write(report)
    hid.flush()

for event in kbd.read_loop():
    if event.type != ecodes.EV_KEY:
        continue

    code = event.code
    value = event.value

    if code in modmap:
        if value == 1:
            mods |= modmap[code]
        elif value == 0:
            mods &= ~modmap[code]
        send_report()
        continue

    key = keymap.get(code)
    if not key:
        continue

    if value == 1:
        if key not in pressed:
            pressed.append(key)
    elif value == 0:
        if key in pressed:
            pressed.remove(key)

    send_report()
    time.sleep(0.005)
