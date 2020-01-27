# -*- coding: utf-8 -*-
import maestro
import time

class Movement():

    # Initialisation des positions des servomoteurs
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

    # Desenclenchement de tous les servomoteurs
    def fin(self, servo):
        servo.setTarget(0, 10000) #10000 desenclenchement
        servo.setTarget(2, 10000)
        servo.setTarget(4, 10000)
        servo.setTarget(6, 10000)

    # Mouvement right face 0 (en face) : horaire arête droite
    def right(self, servo):
    	servo.setTarget(7, 10000)
    	time.sleep(1)
    	servo.setTarget(6, 10000)
    	time.sleep(1)
    	servo.setTarget(7, 6250)
    	time.sleep(1)
    	servo.setTarget(6, 1000)
    	time.sleep(1)

    # Mouvement invRight face 0 (en face) : antihoraire arête droite
    def invRight(self, servo):
    	servo.setTarget(7, 1000)
    	time.sleep(1)
    	servo.setTarget(6, 10000)
    	time.sleep(1)
    	servo.setTarget(7, 6250)
    	time.sleep(1)
    	servo.setTarget(6, 1000)
    	time.sleep(1)

    # Mouvement left face 0 (en face) : horaire arête gauche
    def left(self, servo):
    	servo.setTarget(3, 10000)
    	time.sleep(1)
    	servo.setTarget(2, 10000)
    	time.sleep(1)
    	servo.setTarget(3, 5750)
    	time.sleep(1)
    	servo.setTarget(2, 1000)
    	time.sleep(1)

    # Mouvement invLeft face 0 (en face) : antihoraire arête gauche
    def invLeft(self, servo):
    	servo.setTarget(3, 1000)
    	time.sleep(1)
    	servo.setTarget(2, 10000)
    	time.sleep(1)
    	servo.setTarget(3, 5750)
    	time.sleep(1)
    	servo.setTarget(2, 1000)
    	time.sleep(1)

    # Mouvement up face 0 (en face) : horaire arête haute
    def up(self, servo):
    	servo.setTarget(1, 10000)
    	time.sleep(1)
    	servo.setTarget(0, 10000)
    	time.sleep(1)
    	servo.setTarget(1, 5750)
    	time.sleep(1)
    	servo.setTarget(0, 1000)
    	time.sleep(1)

    # Mouvement invUp face 0 (en face) : antihoraire arête haute
    def invUp(self, servo):
    	servo.setTarget(1, 1000)
    	time.sleep(1)
    	servo.setTarget(0, 10000)
    	time.sleep(1)
    	servo.setTarget(1, 5750)
    	time.sleep(1)
    	servo.setTarget(0, 1000)
    	time.sleep(1)

    # Mouvement down face 0 (en face) : horaire arête basse
    def down(self, servo):
    	servo.setTarget(5, 10000)
    	time.sleep(1)
    	servo.setTarget(4, 10000)
    	time.sleep(1)
    	servo.setTarget(5, 5750)
    	time.sleep(1)
    	servo.setTarget(4, 1000)
    	time.sleep(1)

    # Mouvement invDown face 0 (en face) : antihoraire arête basse
    def invDown(self, servo):
    	servo.setTarget(5, 1000)
    	time.sleep(1)
    	servo.setTarget(4, 10000)
    	time.sleep(1)
    	servo.setTarget(5, 5750)
    	time.sleep(1)
    	servo.setTarget(4, 1000)
    	time.sleep(1)

    # Mouvement front face 0 (en face) : horaire face avant
    # Mouvement invFront face 0 (en face) : antihoraire face avant
    # Mouvement back face 0 (en face) : horaire face arrière
    # Mouvement invBack face 0 (en face) : antihoraire face arrière

    # Mouvement x de rotation horaire complète du cube suivant l'axe x
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

    # Mouvement invX de rotation antihoraire complète du cube suivant l'axe x

    # Mouvement y de rotation horaire complète du cube suivant l'axe y
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

    # Mouvement invY de rotation antihoraire complète du cube suivant l'axe y
    # Mouvement z de rotation horaire complète du cube suivant l'axe z
    # Mouvement invZ de rotation antihoraire complète du cube suivant l'axe z
