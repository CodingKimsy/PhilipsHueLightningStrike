from phue import Bridge
from pygame import mixer
import time

b = Bridge('192.168.2.102')
b.connect()
b.get_api()

lights = b.lights

# Print light names
for l in lights:
    print(l.name )


mixer.init()


def blitz():
    b.set_light('Keller', 'on', True)

    b.set_light('Keller', 'bri', 120)
    b.set_light('Keller', 'on', False)
    time.sleep(.1)
    mixer.music.load('storm-thunder.wav')
    mixer.music.play()
    b.set_light('Keller', 'on', True)
    b.set_light('Keller', 'bri', 210)
    time.sleep(.1)
    b.set_light('Keller', 'bri', 0)
    time.sleep(.45)
    b.set_light('Keller', 'bri', 255)
    time.sleep(.1)
    b.set_light('Keller', 'bri', 80)
    time.sleep(.4)
    b.set_light('Keller', 'bri', 40)
    time.sleep(.3)
    b.set_light('Keller', 'bri', 255)
    time.sleep(.35)
    b.set_light('Keller', 'bri', 150)
    b.set_light('Keller', 'bri', 50)
    b.set_light('Keller', 'on', False)
    time.sleep(1.5)
    

    mixer.music.load('thundr04.wav')
    mixer.music.play()
    b.set_light('Keller', 'on', True)
    b.set_light('Keller', 'bri', 255)
    time.sleep(.3)
    b.set_light('Keller', 'bri', 160)
    time.sleep(.15)
    b.set_light('Keller', 'bri', 65)
    b.set_light('Keller', 'bri', 0)
    time.sleep(.27)
    b.set_light('Keller', 'bri', 110)
    time.sleep(.3)
    b.set_light('Keller', 'bri', 220)
    b.set_light('Keller', 'bri', 0)
    b.set_light('Keller', 'bri', 165)
    b.set_light('Keller', 'bri', 0)
    b.set_light('Keller', 'bri', 190)
    b.set_light('Keller', 'bri', 0)
    b.set_light('Keller', 'bri', 60)
    time.sleep(.3)
    b.set_light('Keller', 'bri', 170)
    b.set_light('Keller', 'bri', 0)
    b.set_light('Keller', 'bri', 210)
    time.sleep(.45)
    b.set_light('Keller', 'bri', 0)
    time.sleep(.29)
    b.set_light('Keller', 'bri', 40)
    time.sleep(.27)
    b.set_light('Keller', 'on', False)
    time.sleep(3)

blitz()



