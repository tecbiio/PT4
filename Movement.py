import MovementCube
import MovementRobot
import maestro

class Movement():

    # Initialisation des poitions des servomoteurs
    def initialisation(self):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mr.initialisation(servo)
        servo.close()

    # Desenclenchement de tous les servomoteurs
    def fin(self):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mr.fin(servo)
        servo.close()

    # Mouvement right face 0 (en face) : horaire arête droite
    def right(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.right(servo)
        mc.right(cube)
        servo.close()

    # Mouvement invRight face 0 (en face) : antihoraire arête droite
    def invRight(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invRight(servo)
        mc.invRight(cube)
        servo.close()

    # Mouvement left face 0 (en face) : horaire arête gauche
    def left(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.left(servo)
        mc.left(cube)
        servo.close()

    # Mouvement invLeft face 0 (en face) : antihoraire arête gauche
    def invLeft(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invLeft(servo)
        mc.invLeft(cube)
        servo.close()

    # Mouvement up face 0 (en face) : horaire arête haute
    def up(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.up(servo)
        mc.up(cube)
        servo.close()

    # Mouvement invUp face 0 (en face) : antihoraire arête haute
    def invUp(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invUp(servo)
        mc.invUp(cube)
        servo.close()

    # Mouvement down face 0 (en face) : horaire arête basse
    def down(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.down(servo)
        mc.down(cube)
        servo.close()

    # Mouvement invDown face 0 (en face) : antihoraire arête basse
    def invDown(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invDown(servo)
        mc.invDown(cube)
        servo.close()

    # Mouvement front face 0 (en face) : horaire face avant
    def front(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.front(servo)
        mc.front(cube)
        servo.close()

    # Mouvement invFront face 0 (en face) : antihoraire face avant
    def invFront(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invFront(servo)
        mc.invFront(cube)
        servo.close()

    # Mouvement back face 0 (en face) : horaire face arrière
    def back(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.back(servo)
        mc.back(cube)
        servo.close()

    # Mouvement invBack face 0 (en face) : antihoraire face arrière
    def invBack(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invBack(servo)
        mc.invBack(cube)
        servo.close()

    # Mouvement x de rotation horaire complète du cube suivant l'axe x
    def x(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.x(servo)
        mc.x(cube)
        servo.close()

    # Mouvement invX de rotation antihoraire complète du cube suivant l'axe x
    def invX(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invX(servo)
        mc.invX(cube)
        servo.close()

    # Mouvement y de rotation horaire complète du cube suivant l'axe y
    def y(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.y(servo)
        mc.y(cube)
        servo.close()

    # Mouvement invY de rotation antihoraire complète du cube suivant l'axe y
    def invY(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invY(servo)
        mc.invY(cube)
        servo.close()

    # Mouvement z de rotation horaire complète du cube suivant l'axe z
    def z(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.z(servo)
        mc.z(cube)
        servo.close()

    # Mouvement invZ de rotation antihoraire complète du cube suivant l'axe z
    def invZ(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        mr.invZ(servo)
        mc.invZ(cube)
        servo.close()
