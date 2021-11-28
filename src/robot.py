from ev3dev.ev3 import *
from time import sleep

COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']

class Robot():
    def __init__(self, mSx, mDx, cSx, cDx):
        self.motorSx, self.motorDx, self.colorSx, self.colorDx = MediumMotor(mSx), MediumMotor(mDx), ColorSensor(cSx), ColorSensor(cDx)
        self.colorSx.mode, self.colorDx.mode = 'COL-COLOR', 'COL-COLOR'

    def move(self, speedSx, speedDx):
        self.motorSx.run_forever(speed_sp=speedSx)
        self.motorDx.run_forever(speed_sp=-speedDx)

    def stop(self):
        self.motorSx.stop(stop_action='hold')
        self.motorDx.stop(stop_action='hold')

    def readColor(self):
        return (COLORS[self.colorSx.value()], COLORS[self.colorDx.value()])

    def drive(self, speedSx, speedDx, correction):
        while True:
            tmpSx, tmpDx = speedSx, speedDx
            color = self.readColor()
            if color[0] == 'black':
                tmpDx = speedDx + correction
            if color[1] == 'black':
                tmpSx = speedSx + correction
            if color == ('black', 'black'):
                self.stop()
                sleep(5)
            self.move(tmpSx, tmpDx)
            sleep(0.2)

if __name__=='main':
    r = Robot('outA', 'outB', 'in1', 'in2')
