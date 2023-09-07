#Halloweenicorn v.1 betarrr - @mrglennjones - Thanks to my good friend pb and hel from Pimoroni for the ninja style help.
#apololgies to my mum for not commenting the code very well.

import time
import ntptime
import urequests
import random
import os
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN
from wave_player import WavePlayer
from pngdec import PNG
from machine import Pin

graphics = PicoGraphics(display=DISPLAY_COSMIC_UNICORN)
gu = CosmicUnicorn()

#Setup PIR Sensor
pir =  machine.Pin(5)


gu.set_brightness(0.2)

wp = WavePlayer(gu)

#PNG spritesheet
png = PNG(graphics)
png.open_file("/faces.png")

LAUGH_SOUND = [ 'laugh/%s'%f for f in os.listdir('laugh') ]
print (LAUGH_SOUND)

#set the frame size for the animations
frame_width = 32
frame_height = 32

black = graphics.create_pen(0,0,0)

class frame:
    def __init__(self, frame_x, frame_y):
        self.frame_x = frame_x
        self.frame_y = frame_y

skullframes = []
# describe as index from 0 - 3
skullframes.append(frame (0, 0))
skullframes.append(frame (1, 0))
skullframes.append(frame (2, 0))
skullframes.append(frame (3, 0))
skullframes.append(frame (0, 0))
skullframes.append(frame (1, 0))
skullframes.append(frame (2, 0))
skullframes.append(frame (3, 0))

pumpkinframes = []
# describe as index from 0 - 3
pumpkinframes.append(frame (0, 1))
pumpkinframes.append(frame (1, 1))
pumpkinframes.append(frame (2, 1))
pumpkinframes.append(frame (3, 1))
pumpkinframes.append(frame (0, 1))
pumpkinframes.append(frame (1, 1))
pumpkinframes.append(frame (2, 1))
pumpkinframes.append(frame (3, 1))

draculaframes = []
# describe as index from 0 - 3
draculaframes.append(frame (0, 2))
draculaframes.append(frame (1, 2))
draculaframes.append(frame (2, 2))
draculaframes.append(frame (3, 2))
draculaframes.append(frame (2, 2))
draculaframes.append(frame (3, 2))
draculaframes.append(frame (1, 2))
draculaframes.append(frame (0, 2))

ghostframes = []
# describe as index from 0 - 3
ghostframes.append(frame (0, 3))
ghostframes.append(frame (1, 3))
ghostframes.append(frame (2, 3))
ghostframes.append(frame (3, 3))
ghostframes.append(frame (0, 3))
ghostframes.append(frame (1, 3))
ghostframes.append(frame (2, 3))
ghostframes.append(frame (3, 3))

faceframes =["skullframes", "pumpkinframes", "draculaframes", "ghostframes"]

selected_frame = random.choice(faceframes)
print(f"Selected frame: {selected_frame}")

busy = False

def JumpScare():
    global busy
    
    busy = True
     
    #play random sound
    #wp.play('laugh/LAUGH-1.wav', loop=1)
    wp.play(random.choice(LAUGH_SOUND), loop=1)
    
    #pick random face
    selected_frame = random.choice(faceframes)
    print(f"Selected frame: {selected_frame}")
    # Use the correct list of frames based on selected_frame
    if selected_frame == "skullframes":
        frame_list = skullframes
    elif selected_frame == "pumpkinframes":
        frame_list = pumpkinframes
    elif selected_frame == "draculaframes":
        frame_list = draculaframes
    elif selected_frame == "ghostframes":
        frame_list = ghostframes
    else:
        frame_list = []  # Handle the case when selected_frame is invalid


    for frame in frame_list:
        # Clear the display before drawing the new frame
        graphics.set_pen(black)
        graphics.clear()

        # Decode and display the current frame
        png.decode(0, 0, source=(frame.frame_x * frame_width, frame.frame_y * frame_height, frame_width, frame_height), scale=(1, 1), rotate=0)
        
        gu.update(graphics)

        time.sleep(0.1)  # Adjust speed of anim

    # Clear display
    graphics.set_pen(black)
    graphics.clear()
    gu.update(graphics)
    
    time.sleep(5) # Time out so it does not trigger again immediately
    
    busy = False


while True:
    #if gu.is_pressed(CosmicUnicorn.SWITCH_A):
    if pir.value() == 1:
        if not busy:
            JumpScare()
        

    

