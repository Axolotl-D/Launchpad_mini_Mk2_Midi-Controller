#!/usr/bin/env python
#
# midiin_callback.py
#
"""Show how to receive MIDI input by setting a callback function."""

from __future__ import print_function

import logging
import sys
import time

from pynput.keyboard import Controller, Key
from rtmidi.midiutil import open_midiinput, open_midioutput

from lightTest import sendLight, sendLight2, blinkLight, blinkLight2

log = logging.getLogger('midiin_callback')
logging.basicConfig(level=logging.DEBUG)
keyboard = Controller()


# global lastAction
# lastAction = True

class MidiInputHandler(object):
    lastAction = []
    lastAction2 = []
    int = 123
    for x in range(int):
        lastAction.append(True)
        lastAction2.append(True)
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
        if message[0] == 144:
            i = 123
            for x in range(i):
                if message[1] == x:
                    if message[2] != 0:
                        if x == 123:
                            pass

                        elif MidiInputHandler.lastAction[x] == True:
                            sendLight(x, "red", midiout)
                            MidiInputHandler.lastAction[x] = not MidiInputHandler.lastAction[x]
                        else:
                            sendLight(x, "green", midiout)
                            MidiInputHandler.lastAction[x] = not MidiInputHandler.lastAction[x]
        elif message[0] == 176:
            i = 123
            for x in range(i):
                if message[1] == x:
                    if message[2] != 0:
                        if x == 104:
                            pass

                        elif MidiInputHandler.lastAction2[x] == True:
                            sendLight2(x, "red", midiout)
                            MidiInputHandler.lastAction2[x] = not MidiInputHandler.lastAction2[x]
                        else:
                            sendLight2(x, "green", midiout)
                            MidiInputHandler.lastAction2[x] = not MidiInputHandler.lastAction2[x]

        if message[1] == 0:
            if message[2] == 0:

                print("Done")

            elif message[2] != 0:
                print("Taste 0")
                keyboard.press(Key.f13)
                keyboard.release(Key.f13)

        elif message[1] == 1:
            if message[2] == 0:
                print("Done")

            elif message[2] != 0:
                print("Taste 1")
                keyboard.press(Key.f14)
                keyboard.release(Key.f14)


        elif message[1] == 2:
            if message[2] == 0:

                print("Done")

            elif message[2] != 0:
                print("Taste 2")
                #     True,0,15
                if MidiInputHandler.lastAction[2] == True:
                    keyboard.press(Key.f15)
                    keyboard.release(Key.f15)
                else:
                    keyboard.press(Key.f16)
                    keyboard.release(Key.f16)




        elif message[1] == 104 and message[0] == 176:
            if message[2] == 0:

                print("Done")

            elif message[2] != 0:
                print("Taste ArrowUp")
                keyboard.press('t')
                keyboard.release('t')
                keyboard.press('!')
                keyboard.release('!')
                keyboard.press('r')
                keyboard.release('r')
                keyboard.press('e')
                keyboard.release('e')
                keyboard.press('p')
                keyboard.release('p')
                keyboard.press(' ')
                keyboard.release(' ')
                keyboard.press('@')
                keyboard.release('@')
                keyboard.press('k')
                keyboard.release('k')
                keyboard.press('a')
                keyboard.release('a')
                keyboard.press('w')
                keyboard.release('w')
                keyboard.press('a')
                keyboard.release('a')
                keyboard.press('i')
                keyboard.release('i')
                keyboard.press('i')
                keyboard.release('i')
                keyboard.press('_')
                keyboard.release('_')
                keyboard.press('n')
                keyboard.release('n')
                keyboard.press('e')
                keyboard.release('e')
                keyboard.press('k')
                keyboard.release('k')
                keyboard.press('o')
                keyboard.release('o')
                keyboard.press('#')
                keyboard.release('#')
                keyboard.press('8')
                keyboard.release('8')
                keyboard.press('6')
                keyboard.release('6')
                keyboard.press('7')
                keyboard.release('7')
                keyboard.press('9')
                keyboard.release('9')
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

                blinkLight2(104, "green", "red", 10, midiout)




        #     True,0,15


# Prompts user for MIDI input port, unless a valid port number or name d
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
i = 121
for x in range(i):
    sendLight(x, "green", midiout)
j = 112
for x in range(104,j):
    sendLight2(x, "green", midiout)

print("Entering main loop. Press Control-C to exit.")
try:
    # Just wwait for keyboard interrupt,
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
