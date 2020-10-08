import time

import rtmidi


def setLight(status, key, Velocity):
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    statusValue = 0x0
    if status == True:
        statusValue = 0x90
    else:
        statusValue = 0x80

    if available_ports:
        midiout.open_port(0)
    else:
        midiout.open_virtual_port("My virtual output")

    with midiout:
        set_note = [statusValue, key, Velocity]
        midiout.send_message(set_note)
    del midiout