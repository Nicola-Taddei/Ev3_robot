#! /usr/bin/python3
from ev3dev.ev3 import *
from time import sleep
from robot import Robot

STD_DIR_SPEED=300
STD_ROT_SPEED=200
STD_DELAY = 3

r = Robot('outB', 'outA', 'in1', 'in2') # B->sinistro e A->destro

sleep(5)

speed=STD_DIR_SPEED

r.drive(300, 300, 150)

'''
while True:
    sleep(0.1)
    color = r.readColor()
    if color==('black', 'black'):
        speed=-speed
        r.move(speed, speed)
        sleep(1)
    r.move(speed, speed)
'''