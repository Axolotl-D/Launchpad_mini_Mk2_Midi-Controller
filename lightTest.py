import sys
from time import sleep

from rtmidi.midiutil import open_midioutput

def sendLight(key, color, midiout):
    colordict = {
        "red": 79,
        "green": 100,
        "off": 0,
        "yellow": 127,
        "amber": 50,
        "dark red": 10
    }

    midiout.send_message([144, key, colordict[color]])

    print("Color done")