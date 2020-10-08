#!/usr/bin/env python
#
# midiin_callback.py
#
"""Show how to receive MIDI input by setting a callback function."""

from __future__ import print_function

import logging
import sys
import time

import rtmidi
from pynput.keyboard import Controller, Key
from rtmidi.midiutil import open_midiinput, open_midioutput

log = logging.getLogger('midiin_callback')
logging.basicConfig(level=logging.DEBUG)
keyboard = Controller()

# global lastAction
# lastAction = True

class MidiInputHandler(object):

    lastAction = True


    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None, ):
        message, deltatime = event
        # midiout = rtmidi.MidiOut()
        # available_ports = midiout.get_ports()
        # # print(available_ports)
        # midiout.open_port(port)
        # # if available_ports:
        # #     midiout.open_port(1)
        # # else:
        # #     midiout.open_virtual_port("My virtual output")
        self._wallclock += deltatime
        print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))

        self.midimethod(message, midiout)

    def midimethod(self, message, midiout):
        if message[1] == 0:
            if message[2] == 0:

                print("Done")

            elif message[2] != 0:
                print("Taste 0")
                keyboard.press(Key.f13)
                keyboard.release(Key.f13)
                #     True,0,15
                with midiout:
                    if MidiInputHandler.lastAction == True:
                        # midiout.send_message([176, 0, 0])
                        midiout.send_message([0x90, 0, 12])
                        midiout.close_port
                        print("Lights on")
                        MidiInputHandler.lastAction = not MidiInputHandler.lastAction
                    else:
                        midiout.send_message([0x90, 0, 12])
                        print("Lights off")
                        MidiInputHandler.lastAction = not MidiInputHandler.lastAction
                        midiout.close_port



# Prompts user for MIDI input port, unless a valid port number or name
# is given as the first argument on the command line.
# API backend defaults to ALSA on Linux.
port = sys.argv[1] if len(sys.argv) > 1 else None

try:
    midiin, port_name = open_midiinput(port)
    midiout, port_name = open_midioutput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()
lastAction = True
print("Attaching MIDI input callback handler.")

midiin.set_callback(MidiInputHandler(port_name))
print("Entering main loop. Press Control-C to exit.")
try:
    # Just wait for keyboard interrupt,
    # everything else is handled via the input callback.
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    midiout.close_port()
    del midiin