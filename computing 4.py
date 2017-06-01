from microbit import *

boat1 = Image("90009:"
              "09090:"
              "00900:"
              "99999:"
              "09990:")
boat2 = Image("00000:"
              "09090:"
              "00900:"
              "99999:"
              "09990:")
boat3 = Image("00000:"
              "00000:"
              "00900:"
              "99999:"
              "09990:")
boat4 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "09990:")
boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "09990:")
boat6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000:")
alldots=[boat1,boat2,boat3,boat4,boat5,boat6]
while True:
    display.show(alldots)