from ev3dev.ev3 import *
from time import sleep

COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']


class Robot():
    def __init__(self, mSx, mDx, cSx, cDx, controller, f, SPEED, MIN_SPEED, LOW_SPEED):
        self.LOW_SPEED = LOW_SPEED
        self.MIN_SPEED = MIN_SPEED
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

    def normalize(self, speed):
        if speed > 500:
            return 500
        if -self.MIN_SPEED < speed and speed < self.MIN_SPEED:
            return -self.MIN_SPEED
        if speed < -500:
            return -500
        return speed

    def attach(self):
        e = 0
        color = ('red', 'red')
        while color != ('yellow', 'yellow'):
            if color == ('red', 'red'):
                e = 0
            if color[0] not in ['black','red'] or color[1] == 'black':
                e = 1
            if color[1] not in ['black','red'] or color[0] == 'black':
                e = -1
            corr = self.controller.getCorrection(e, self.LOW_SPEED, 'ATTACH')
            self.move(self.normalize(self.LOW_SPEED - corr), self.normalize(self.LOW_SPEED + corr))
            sleep(1/self.f)
            color = self.readColor()


    def drive(self):
        e = 0
        stop=0
        while True:
            color = self.readColor()
            if color == ('red', 'red') :
                self.attach()
                self.stop()
                sleep(5)
            if color == ('black', 'black'):
                pass
            else:
                if color[0] == 'black':
                    if e > 0:
                        e = 0
                    e -= 1
                if color[1] == 'black':
                    if e < 0:
                        e = 0
                    e += 1

            corr = self.controller.getCorrection(e, self.SPEED, 'STD')
            self.move(self.normalize(self.SPEED - corr), self.normalize(self.SPEED + corr))
            sleep(1/self.f)

    def catch(self):
        self.move(100, 100)
        self.stop()

class Controller():
    def __init__(self, k_P, k_I, k_P_attach):
        self.k_P, self.k_I, self.k_P_attach = k_P, k_I, k_P_attach

    def sgn(self, x):
        if x < 0:
            return -1
        if x == 0:
            return 0
        return 1

    def getCorrection(self, error, SPEED, STATE):  #error has integer values: negative if black is detected on the left and positive if it is detected on the right. The absolute value is the number of consecutive identical mesurements
        if STATE == 'STD':
            P = -self.k_P * self.sgn(error) * SPEED/30
            I = -self.k_I * error * SPEED/30
            return P + I
        if STATE == 'ATTACH':
            P = -self.k_P_attach * self.sgn(error) * SPEED/30
            return P

class Nipper():
    def __init__(self, motorMove, motorRotate, sensor):
        self.motorMove, self.motorRotate, self.sensor = MediumMotor(motorMove), MediumMotor(motorRotate), ColorSensor(sensor)
        self.sensor.mode = 'COL-COLOR'

    def pull(self, colors):  # colors is a list of product colors which we are allowed to take
        pass
        #codice

    def push(self):
        pass
        #codice


if __name__=='main':
    Robot('outB', 'outA', 'in1', 'in2', Controller(15, 5), 10, 200).drive()


