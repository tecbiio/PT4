# -*- coding: utf-8 -*-
import maestro
import time

class Movement():

    def initialisation(self, servo):
        servo.setTarget(1, 5750)
        time.sleep(1)
        servo.setTarget(3, 5750)
        time.sleep(1)
        servo.setTarget(5, 5750)
        time.sleep(1)
        servo.setTarget(7, 6250)
        time.sleep(1)
        servo.setTarget(0, 1000) #1000 enclenchement
        servo.setTarget(2, 1000)
        servo.setTarget(4, 1000)
        servo.setTarget(6, 1000)
        time.sleep(1)

    def fin(self, servo):
        servo.setTarget(0, 10000) #10000 desenclenchement
        servo.setTarget(2, 10000)
        servo.setTarget(4, 10000)
        servo.setTarget(6, 10000)

    def x(self, servo):
    	servo.setTarget(2, 10000)
    	servo.setTarget(6, 10000)
    	time.sleep(1)
    	servo.setTarget(1, 10000)
    	servo.setTarget(5, 1000)
    	time.sleep(1)
    	servo.setTarget(2, 1000)
    	servo.setTarget(6, 1000)
    	time.sleep(1)
    	servo.setTarget(0, 10000)
    	servo.setTarget(4, 10000)
    	time.sleep(1)
    	servo.setTarget(1, 5750)
    	servo.setTarget(5, 5750)
    	time.sleep(1)
    	servo.setTarget(0, 1000)
    	servo.setTarget(4, 1000)
    	time.sleep(1)

    def y(self, servo):
    	servo.setTarget(0, 10000)
    	servo.setTarget(4, 10000)
    	time.sleep(1)
    	servo.setTarget(3, 10000)
    	servo.setTarget(7, 1000)
    	time.sleep(1)
    	servo.setTarget(0, 1000)
    	servo.setTarget(4, 1000)
    	time.sleep(1)
    	servo.setTarget(2, 10000)
    	servo.setTarget(6, 10000)
    	time.sleep(1)
    	servo.setTarget(3, 5750)
    	servo.setTarget(7, 6250)
    	time.sleep(1)
    	servo.setTarget(2, 1000)
    	servo.setTarget(6, 1000)
    	time.sleep(1)

    def right(self, servo):
    	servo.setTarget(7, 10000)
    	time.sleep(1)
    	servo.setTarget(6, 10000)
    	time.sleep(1)
    	servo.setTarget(7, 6250)
    	time.sleep(1)
    	servo.setTarget(6, 1000)
    	time.sleep(1)

    def invRight(self, servo):
    	servo.setTarget(7, 1000)
    	time.sleep(1)
    	servo.setTarget(6, 10000)
    	time.sleep(1)
    	servo.setTarget(7, 6250)
    	time.sleep(1)
    	servo.setTarget(6, 1000)
    	time.sleep(1)

    def left(self, servo):
    	servo.setTarget(3, 10000)
    	time.sleep(1)
    	servo.setTarget(2, 10000)
    	time.sleep(1)
    	servo.setTarget(3, 5750)
    	time.sleep(1)
    	servo.setTarget(2, 1000)
    	time.sleep(1)

    def invLeft(self, servo):
    	servo.setTarget(3, 1000)
    	time.sleep(1)
    	servo.setTarget(2, 10000)
    	time.sleep(1)
    	servo.setTarget(3, 5750)
    	time.sleep(1)
    	servo.setTarget(2, 1000)
    	time.sleep(1)

    def up(self, servo):
    	servo.setTarget(1, 10000)
    	time.sleep(1)
    	servo.setTarget(0, 10000)
    	time.sleep(1)
    	servo.setTarget(1, 5750)
    	time.sleep(1)
    	servo.setTarget(0, 1000)
    	time.sleep(1)

    def invUp(self, servo):
    	servo.setTarget(1, 1000)
    	time.sleep(1)
    	servo.setTarget(0, 10000)
    	time.sleep(1)
    	servo.setTarget(1, 5750)
    	time.sleep(1)
    	servo.setTarget(0, 1000)
    	time.sleep(1)

    def down(self, servo):
    	servo.setTarget(5, 10000)
    	time.sleep(1)
    	servo.setTarget(4, 10000)
    	time.sleep(1)
    	servo.setTarget(5, 5750)
    	time.sleep(1)
    	servo.setTarget(4, 1000)
    	time.sleep(1)

    def invDown(self, servo):
    	servo.setTarget(5, 1000)
    	time.sleep(1)
    	servo.setTarget(4, 10000)
    	time.sleep(1)
    	servo.setTarget(5, 5750)
    	time.sleep(1)
    	servo.setTarget(4, 1000)
    	time.sleep(1)
