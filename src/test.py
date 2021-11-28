#! /usr/bin/python3
from ev3dev.ev3 import *
from time import sleep
from robot import Robot, Controller

STD_DIR_SPEED=200

r = Robot('outB', 'outA', 'in1', 'in2', Controller(15, 5), 10, STD_DIR_SPEED) # B->sinistro e A->destro

sleep(5)

r.drive()
