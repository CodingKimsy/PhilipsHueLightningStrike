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


#lightningLights = [Keller", "Flurlampe", "Küchenfenster","Femie","Stehlampe", "Tischleuchte"]
lightningLights = ["Haustür","Keller", "Flurlampe", "Küchenfenster","Femie","Stehlampe"]

mixer.init()

def allLightsOn():
    for l in lightningLights:
        b.set_light(l, 'on', True)

def allLightsOff():
    for l in lightningLights:
        b.set_light(l, 'on', False)    

def allLightsBrightness(brightness):
    for l in lightningLights:
        b.set_light(l, 'bri', brightness)

def blitz():
    allLightsOn()

    allLightsBrightness(120)
    allLightsOff()
    time.sleep(.1)
    mixer.music.load('storm-thunder.wav')
    mixer.music.play()
    allLightsOn()
    allLightsBrightness(210)
    time.sleep(.1)
    allLightsBrightness(0)
    time.sleep(.45)
    allLightsBrightness(255)
    time.sleep(.1)
    allLightsBrightness(80)
    time.sleep(.4)
    allLightsBrightness(40)
    time.sleep(.3)
    allLightsBrightness(255)
    time.sleep(.35)
    allLightsBrightness(150)
    allLightsBrightness(50)
    allLightsOff()
    time.sleep(1.5)
    

    mixer.music.load('thundr04.wav')
    mixer.music.play()
    allLightsOn()
    allLightsBrightness(255)
    time.sleep(.3)
    allLightsBrightness(160)
    time.sleep(.15)
    allLightsBrightness(65)
    allLightsBrightness(0)
    time.sleep(.27)
    allLightsBrightness(110)
    time.sleep(.3)
    allLightsBrightness(220)
    allLightsBrightness(0)
    allLightsBrightness(165)
    allLightsBrightness(0)
    allLightsBrightness(190)
    allLightsBrightness(0)
    allLightsBrightness(60)
    time.sleep(.3)
    allLightsBrightness(170)
    allLightsBrightness(0)
    allLightsBrightness(210)
    time.sleep(.45)
    allLightsBrightness(0)
    time.sleep(.29)
#allLightsBrightness(40)
#time.sleep(.27)
    allLightsOff()
    time.sleep(3)

blitz()



