import time


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

def sendLight2(key, color, midiout):
    colordict = {
        "red": 79,
        "green": 100,
        "off": 0,
        "yellow": 127,
        "amber": 50,
        "dark red": 10
    }

    midiout.send_message([176, key, colordict[color]])

    print("Color done")

def blinkLight(key, color1, color2, times, midiout):
    colordict = {
        "red": 79,
        "green": 100,
        "off": 0,
        "yellow": 127,
        "amber": 50,
        "dark red": 10
    }

    for x in range(times):
        midiout.send_message([176, key, colordict[color1]])
        time.sleep(0.5/(times/2))
        midiout.send_message([176, key, colordict[color2]])
        time.sleep(0.5/(times/2))

    midiout.send_message([144, key, 100])

def blinkLight2(key, color1, color2, times, midiout):
    colordict = {
        "red": 79,
        "green": 100,
        "off": 0,
        "yellow": 127,
        "amber": 50,
        "dark red": 10
    }

    for x in range(times):
        midiout.send_message([176, key, colordict[color1]])
        time.sleep(0.5/(times/2))
        midiout.send_message([176, key, colordict[color2]])
        time.sleep(0.5/(times/2))

    midiout.send_message([176, key, 100])