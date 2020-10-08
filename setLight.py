import time

import rtmidi


def setLight(status, key, Velocity):

    global set_note
    statusValue = 0x0
    if status == True:
        statusValue = 0x90
    else:
        statusValue = 0x80
        set_note = [statusValue, key, Velocity]
        return set_note