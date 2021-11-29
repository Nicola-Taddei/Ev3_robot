#! /usr/bin/python3
from ev3dev.ev3 import *
from time import sleep
from robot import Robot, Controller, Nipper, AVG_polimi_lab

STD_DIR_SPEED=300
MIN_SPEED=100
LOW_SPEED=150

r = Robot('outB', 'outA', 'in1', 'in2', Controller(10, 6, 10), 15, STD_DIR_SPEED, MIN_SPEED, LOW_SPEED) # B->sinistro e A->destro
n = Nipper('out3', 'out4', 'in3')
avg = AVG_polimi_lab(r, n)

sleep(5)

r.drive()

#allowed_colors = ['red', 'green']
#avg.conect(allowed_colors)
