import mouse
import time
import random 

mouse.move(10, 10, absolute=True, duration=0.01)
time.sleep(.1)

while True:
    mouse.move(0, random.randint(0,2100), absolute=False, duration=.5)
    mouse.move(random.randint(0,2100),0, absolute=False, duration=.5)
    mouse.move(0, -(random.randint(0,1900)), absolute=False, duration=.5)
    mouse.move(-(random.randint(0,1900)), 0, absolute=False, duration=.5)
    time.sleep(1)
    