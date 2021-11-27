#! /usr/bin/env/python3

from ev3dev.ev3 import *
from time import sleep
from robot import Robot

STD_SPEED = 500
STD_DELAY = 3

r = Robot('outA', 'outB')

sleep(5)

while True:
    r.move(STD_SPEED, STD_SPEED)
    sleep(STD_DELAY)
    r.stop()
    sleep(STD_DELAY)
    r.move(STD_SPEED, -STD_SPEED)
    sleep(STD_DELAY)
    r.stop()
    sleep(STD_DELAY)
    r.move(-STD_SPEED, STD_SPEED)
    sleep(STD_DELAY)