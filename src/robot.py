from ev3dev.ev3 import *
from time import sleep

COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']

k_P = 15
k_I = 5

class Robot():
    def __init__(self, mSx, mDx, cSx, cDx, controller, f, SPEED):
        self.SPEED = SPEED
        self.controller = controller   #allows to use a generic kind of controller, instead of forcing the use of Controller class
        self.f = f
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

    def drive(self):
        e = 0
        while True:
            color = self.readColor()
            if color[0] == 'black':
                if e > 0:
                    e = 0
                e -= 1
            if color[1] == 'black':
                if e < 0:
                    e = 0
                e += 1
            if color == ('black', 'black'):
                self.stop()
                sleep(5)
            corr = self.controller.getCorrection(e, self.SPEED)
            self.move(self.SPEED - corr, self.SPEED + corr)
            sleep(1/self.f)


class Controller():
    def __init__(self, k_P, k_I):
        self.k_P, self.k_I = k_P, k_I

    def sgn(self, x):
        if x < 0:
            return -1
        if x == 0:
            return 0
        return 1

    def getCorrection(self, error, SPEED):  #error has integer values: negative if black is detected on the left and positive if it is detected on the right. The absolute value is the number of consecutive identical mesurements 
        P = -k_P * self.sgn(error) * SPEED
        I = -k_I * error * SPEED
        return P + I

if __name__=='main':
    Robot('outB', 'outA', 'in1', 'in2', Controller(15, 5), 10, 200).drive()
