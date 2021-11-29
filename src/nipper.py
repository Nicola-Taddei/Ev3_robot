
from ev3dev.ev3 import *
from time import sleep
from datetime import datetime 
import time
import random 

motor_stationA = MediumMotor('outA')
motor_stationB = MediumMotor('outB')
def moveup(motor_station):
        motor_station.run_forever(speed_sp=100)
        sleep(3) 
        motor_station.stop(stop_action="hold")
def movedown(motor_station):
        motor_station.run_forever(speed_sp=-100)
        sleep(3)
        motor_station.stop(stop_action="hold")
def movein(motor_station):
        motor_station.run_forever(speed_sp=-55)
        sleep(2.8)
        motor_station.stop(stop_action="hold")
def moveoff(motor_station):
        motor_station.run_forever(speed_sp=55)
