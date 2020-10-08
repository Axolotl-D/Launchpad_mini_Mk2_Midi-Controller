# import time
# import rtmidi
#
# midiout = rtmidi.MidiOut()
# available_ports = midiout.get_ports()
#
# if available_ports:
#     midiout.open_port(1)
# else:
#     midiout.open_virtual_port("My virtual output")
#
# with midiout:
#     note_c = [144, 60, 112] # channel 1, middle C, velocity 112
#     note_d = [144, 62, 112]
#     note_e = [144, 64, 112]
#     note_f = [144, 65, 112]
#     note_g = [144, 67, 112]
#     note_a = [144, 69, 112]
#
#     note_off = [0x80, 0, 0x0D]
#     midiout.send_message(note_c)
#     # print(note_on)
#     time.sleep(0.5)
#     midiout.send_message(note_d)
#     time.sleep(0.5)
#     midiout.send_message(note_e)
#     time.sleep(0.5)
#     midiout.send_message(note_f)
#     time.sleep(0.5)
#     midiout.send_message(note_g)
#     time.sleep(1)
#     midiout.send_message(note_g)
#     time.sleep(1)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_g)
#     time.sleep(2)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_a)
#     time.sleep(0.5)
#     midiout.send_message(note_g)
#     time.sleep(2)
#     midiout.send_message(note_f)
#     time.sleep(0.5)
#     midiout.send_message(note_f)
#     time.sleep(0.5)
#     midiout.send_message(note_f)
#     time.sleep(0.5)
#     midiout.send_message(note_f)
#     time.sleep(0.5)
#     midiout.send_message(note_e)
#     time.sleep(1)
#     midiout.send_message(note_e)
#     time.sleep(1)
#     midiout.send_message(note_g)
#     time.sleep(0.5)
#     midiout.send_message(note_g)
#     time.sleep(0.5)
#     midiout.send_message(note_g)
#     time.sleep(0.5)
#     midiout.send_message(note_g)
#     time.sleep(0.5)
#     midiout.send_message(note_c)
#     time.sleep(5)
#     # midiout.send_message(note_off)
#     # time.sleep(0.1)
#
# del midiout
import time
import rtmidi


def method():
    global midiout, available_ports, note_on, note_off
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    if available_ports:
        midiout.open_port(0)
    else:
        midiout.open_virtual_port("My virtual output")
    with midiout:
        note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
        note_off = [0x80, 60, 0]
        midiout.send_message(note_on)
        time.sleep(0.5)
        midiout.send_message(note_off)
        time.sleep(0.1)
    del midiout


method()

method()