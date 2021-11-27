from ev3dev.ev3 import *

class Robot():
    def __init__(self, portSx, portDx):
        self.motorSx, self.motorDx = MediumMotor(portSx), MediumMotor(portDx)
    
    def move(self, speedSx, speedDx):
        self.motorSx.run_forever(speed_sp=speedSx)
        self.motorDx.run_forever(spped_sp=-speedDx)

    def stop(self):
        self.motorSx.stop(stop_action='hold')
        self.motorDx.stop(stop_action='hold')


if __name__=='main':
    r = Robot('outA', 'outB')