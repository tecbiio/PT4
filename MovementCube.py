import numpy as np
import RubiksCube

class Movement:

    # Mouvement right face 0 (en face) : horaire arête droite
    def right(self, cube):
        tab = cube.getTab()
        # Rotation arête droite face 0
        tmp1 = tab[0,0,2]
        tmp2 = tab[0,1,2]
        tmp3 = tab[0,2,2]
        tab[0,0,2] = tab[5,2,0]
        tab[0,1,2] = tab[5,1,0]
        tab[0,2,2] = tab[5,0,0]
        tab[5,0,0] = tab[2,0,0]
        tab[5,1,0] = tab[2,1,0]
        tab[5,2,0] = tab[2,2,0]
        tab[2,0,0] = tab[4,2,2]
        tab[2,1,0] = tab[4,1,2]
        tab[2,2,0] = tab[4,0,2]
        tab[4,0,2] = tmp1
        tab[4,1,2] = tmp2
        tab[4,2,2] = tmp3
        # Pivot face 1 sur elle-même
        tmp1 = tab[1,0,0]
        tmp2 = tab[1,0,1]
        tmp3 = tab[1,0,2]
        tab[1,0,1] = tab[1,1,0]
        tab[1,0,0] = tab[1,2,0]
        tab[1,1,0] = tab[1,2,1]
        tab[1,2,0] = tab[1,2,2]
        tab[1,2,1] = tab[1,1,2]
        tab[1,0,2] = tmp1
        tab[1,1,2] = tmp2
        tab[1,2,2] = tmp3

    # Mouvement invRight face 0 (en face) : antihoraire arête droite
    def invRight(self, cube):
        for i in range(0,3):
            self.right(cube)

    # Mouvement left face 0 (en face) : horaire arête gauche
    def left(self, cube):
        tab = cube.getTab()
        # Rotation arête gauche face 0
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,1,0]
        tmp3 = tab[0,2,0]
        tab[0,0,0] = tab[4,0,0]
        tab[0,1,0] = tab[4,1,0]
        tab[0,2,0] = tab[4,2,0]
        tab[4,0,0] = tab[2,2,2]
        tab[4,1,0] = tab[2,1,2]
        tab[4,2,0] = tab[2,0,2]
        tab[2,0,2] = tab[5,0,2]
        tab[2,1,2] = tab[5,1,2]
        tab[2,2,2] = tab[5,2,2]
        tab[5,2,2] = tmp1
        tab[5,1,2] = tmp2
        tab[5,0,2] = tmp3
        # Pivot face 3 sur elle-même
        tmp1 = tab[3,0,0]
        tmp2 = tab[3,0,1]
        tmp3 = tab[3,0,2]
        tab[3,0,1] = tab[3,1,0]
        tab[3,0,0] = tab[3,2,0]
        tab[3,1,0] = tab[3,2,1]
        tab[3,2,0] = tab[3,2,2]
        tab[3,2,1] = tab[3,1,2]
        tab[3,0,2] = tmp1
        tab[3,1,2] = tmp2
        tab[3,2,2] = tmp3

    # Mouvement invLeft face 0 (en face) : antihoraire arête gauche
    def invLeft(self, cube):
        for i in range(0,3):
            self.left(cube)

    # Mouvement up face 0 (en face) : horaire arête haute
    def up(self, cube):
        tab = cube.getTab()
        # Rotation arête haute face 0
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,0,1]
        tmp3 = tab[0,0,2]
        tab[0,0,0] = tab[1,0,0]
        tab[0,0,1] = tab[1,0,1]
        tab[0,0,2] = tab[1,0,2]
        tab[1,0,0] = tab[2,0,0]
        tab[1,0,1] = tab[2,0,1]
        tab[1,0,2] = tab[2,0,2]
        tab[2,0,0] = tab[3,0,0]
        tab[2,0,1] = tab[3,0,1]
        tab[2,0,2] = tab[3,0,2]
        tab[3,0,0] = tmp1
        tab[3,0,1] = tmp2
        tab[3,0,2] = tmp3
        # Pivot face 4 sur elle-même
        tmp1 = tab[4,0,0]
        tmp2 = tab[4,0,1]
        tmp3 = tab[4,0,2]
        tab[4,0,1] = tab[4,1,0]
        tab[4,0,0] = tab[4,2,0]
        tab[4,1,0] = tab[4,2,1]
        tab[4,2,0] = tab[4,2,2]
        tab[4,2,1] = tab[4,1,2]
        tab[4,0,2] = tmp1
        tab[4,1,2] = tmp2
        tab[4,2,2] = tmp3

    # Mouvement invUp face 0 (en face) : antihoraire arête haute
    def invUp(self, cube):
        for i in range(0,3):
            self.up(cube)

    # Mouvement down face 0 (en face) : horaire arête basse
    def down(self, cube):
        tab = cube.getTab()
        # Rotation arête basse face 0
        tmp1 = tab[0,2,0]
        tmp2 = tab[0,2,1]
        tmp3 = tab[0,2,2]
        tab[0,2,0] = tab[3,2,0]
        tab[0,2,1] = tab[3,2,1]
        tab[0,2,2] = tab[3,2,2]
        tab[3,2,0] = tab[2,2,0]
        tab[3,2,1] = tab[2,2,1]
        tab[3,2,2] = tab[2,2,2]
        tab[2,2,0] = tab[1,2,0]
        tab[2,2,1] = tab[1,2,1]
        tab[2,2,2] = tab[1,2,2]
        tab[1,2,0] = tmp1
        tab[1,2,1] = tmp2
        tab[1,2,2] = tmp3
        # Pivot face 5 sur elle-même
        tmp1 = tab[5,0,0]
        tmp2 = tab[5,0,1]
        tmp3 = tab[5,0,2]
        tab[5,0,1] = tab[5,1,0]
        tab[5,0,0] = tab[5,2,0]
        tab[5,1,0] = tab[5,2,1]
        tab[5,2,0] = tab[5,2,2]
        tab[5,2,1] = tab[5,1,2]
        tab[5,0,2] = tmp1
        tab[5,1,2] = tmp2
        tab[5,2,2] = tmp3

    # Mouvement invDown face 0 (en face) : antihoraire arête basse
    def invDown(self, cube):
        for i in range(0,3):
            self.down(cube)

    # Mouvement front face 0 (en face) : horaire face avant
    def front(self, cube):
        tab = cube.getTab()
        # Pivot face 0 sur elle-même
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,0,1]
        tmp3 = tab[0,0,2]
        tab[0,0,1] = tab[0,1,0]
        tab[0,0,0] = tab[0,2,0]
        tab[0,1,0] = tab[0,2,1]
        tab[0,2,0] = tab[0,2,2]
        tab[0,2,1] = tab[0,1,2]
        tab[0,0,2] = tmp1
        tab[0,1,2] = tmp2
        tab[0,2,2] = tmp3
        # Rotation arête gauche face 1
        tmp1 = tab[1,0,0]
        tmp2 = tab[1,1,0]
        tmp3 = tab[1,2,0]
        tab[1,0,0] = tab[4,2,0]
        tab[1,1,0] = tab[4,2,1]
        tab[1,2,0] = tab[4,2,2]
        tab[4,2,0] = tab[3,2,2]
        tab[4,2,1] = tab[3,1,2]
        tab[4,2,2] = tab[3,0,2]
        tab[3,2,2] = tab[5,2,0]
        tab[3,1,2] = tab[5,2,1]
        tab[3,0,2] = tab[5,2,2]
        tab[5,2,0] = tmp1
        tab[5,2,1] = tmp2
        tab[5,2,2] = tmp3

    # Mouvement invFront face 0 (en face) : antihoraire face avant
    def invFront(self, cube):
        for i in range(0,3):
            self.front(cube)

    # Mouvement back face 0 (en face) : horaire face arrière
    def back(self, cube):
        tab = cube.getTab()
        # Pivot face 2 sur elle-même
        tmp1 = tab[2,0,0]
        tmp2 = tab[2,0,1]
        tmp3 = tab[2,0,2]
        tab[2,0,1] = tab[2,1,0]
        tab[2,0,0] = tab[2,2,0]
        tab[2,1,0] = tab[2,2,1]
        tab[2,2,0] = tab[2,2,2]
        tab[2,2,1] = tab[2,1,2]
        tab[2,0,2] = tmp1
        tab[2,1,2] = tmp2
        tab[2,2,2] = tmp3
        # Rotation arête droite face 1
        tmp1 = tab[1,0,2]
        tmp2 = tab[1,1,2]
        tmp3 = tab[1,2,2]
        tab[1,0,2] = tab[5,0,0]
        tab[1,1,2] = tab[5,0,1]
        tab[1,2,2] = tab[5,0,2]
        tab[5,0,2] = tab[3,0,0]
        tab[5,0,1] = tab[3,1,0]
        tab[5,0,0] = tab[3,2,0]
        tab[3,0,0] = tab[4,0,2]
        tab[3,1,0] = tab[4,0,1]
        tab[3,2,0] = tab[4,0,0] #
        tab[4,0,0] = tmp1
        tab[4,0,1] = tmp2
        tab[4,0,2] = tmp3

    # Mouvement invBack face 0 (en face) : antihoraire face arrière
    def invBack(self, cube):
        for i in range(0,3):
            self.back(cube)

    # Mouvement x de rotation horaire complète du cube suivant l'axe x
    def x(self, cube):
        tab = cube.getTab()
        # Rotation faces 0,5,2 et 4
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,0,1]
        tmp3 = tab[0,0,2]
        tmp4 = tab[0,1,0]
        tmp5 = tab[0,1,1]
        tmp6 = tab[0,1,2]
        tmp7 = tab[0,2,0]
        tmp8 = tab[0,2,1]
        tmp9 = tab[0,2,2]
        tab[0,0,0] = tab[5,2,2]
        tab[0,0,1] = tab[5,2,1]
        tab[0,0,2] = tab[5,2,0]
        tab[0,1,0] = tab[5,1,2]
        tab[0,1,1] = tab[5,1,1]
        tab[0,1,2] = tab[5,1,0]
        tab[0,2,0] = tab[5,0,2]
        tab[0,2,1] = tab[5,0,1]
        tab[0,2,2] = tab[5,0,0]
        tab[5,2,2] = tab[2,2,2]
        tab[5,2,1] = tab[2,2,1]
        tab[5,2,0] = tab[2,2,0]
        tab[5,1,2] = tab[2,1,2]
        tab[5,1,1] = tab[2,1,1]
        tab[5,1,0] = tab[2,1,0]
        tab[5,0,2] = tab[2,0,2]
        tab[5,0,1] = tab[2,0,1]
        tab[5,0,0] = tab[2,0,0]
        tab[2,2,2] = tab[4,0,0]
        tab[2,2,1] = tab[4,0,1]
        tab[2,2,0] = tab[4,0,2]
        tab[2,1,2] = tab[4,1,0]
        tab[2,1,1] = tab[4,1,1]
        tab[2,1,0] = tab[4,1,2]
        tab[2,0,2] = tab[4,2,0]
        tab[2,0,1] = tab[4,2,1]
        tab[2,0,0] = tab[4,2,2]
        tab[4,0,0] = tmp1
        tab[4,0,1] = tmp2
        tab[4,0,2] = tmp3
        tab[4,1,0] = tmp4
        tab[4,1,1] = tmp5
        tab[4,1,2] = tmp6
        tab[4,2,0] = tmp7
        tab[4,2,1] = tmp8
        tab[4,2,2] = tmp9
        # Pivot faces 1 et 3 sur elles-même
        # Pivot face 1 horaire
        tmp1 = tab[1,0,0]
        tmp2 = tab[1,0,1]
        tmp3 = tab[1,0,2]
        tab[1,0,1] = tab[1,1,0]
        tab[1,0,0] = tab[1,2,0]
        tab[1,1,0] = tab[1,2,1]
        tab[1,2,0] = tab[1,2,2]
        tab[1,2,1] = tab[1,1,2]
        tab[1,0,2] = tmp1
        tab[1,1,2] = tmp2
        tab[1,2,2] = tmp3
        # Pivot face 3 antihoraire
        tmp1 = tab[3,0,0]
        tmp2 = tab[3,0,1]
        tmp3 = tab[3,0,2]
        tab[3,0,1] = tab[3,1,2]
        tab[3,0,2] = tab[3,2,2]
        tab[3,1,2] = tab[3,2,1]
        tab[3,2,2] = tab[3,2,0]
        tab[3,2,1] = tab[3,1,0]
        tab[3,2,0] = tmp1
        tab[3,1,0] = tmp2
        tab[3,0,0] = tmp3

    # Mouvement invX de rotation antihoraire complète du cube suivant l'axe x
    def invX(self, cube):
        for i in range(0,3):
            self.x(cube)

    # Mouvement y de rotation horaire complète du cube suivant l'axe y
    def y(self, cube):
        tab = cube.getTab()
        # Rotation faces 0,1,2 et 3
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,0,1]
        tmp3 = tab[0,0,2]
        tmp4 = tab[0,1,0]
        tmp5 = tab[0,1,1]
        tmp6 = tab[0,1,2]
        tmp7 = tab[0,2,0]
        tmp8 = tab[0,2,1]
        tmp9 = tab[0,2,2]
        tab[0,0,0] = tab[1,0,0]
        tab[0,0,1] = tab[1,0,1]
        tab[0,0,2] = tab[1,0,2]
        tab[0,1,0] = tab[1,1,0]
        tab[0,1,1] = tab[1,1,1]
        tab[0,1,2] = tab[1,1,2]
        tab[0,2,0] = tab[1,2,0]
        tab[0,2,1] = tab[1,2,1]
        tab[0,2,2] = tab[1,2,2]
        tab[1,0,0] = tab[2,0,0]
        tab[1,0,1] = tab[2,0,1]
        tab[1,0,2] = tab[2,0,2]
        tab[1,1,0] = tab[2,1,0]
        tab[1,1,1] = tab[2,1,1]
        tab[1,1,2] = tab[2,1,2]
        tab[1,2,0] = tab[2,2,0]
        tab[1,2,1] = tab[2,2,1]
        tab[1,2,2] = tab[2,2,2]
        tab[2,0,0] = tab[3,0,0]
        tab[2,0,1] = tab[3,0,1]
        tab[2,0,2] = tab[3,0,2]
        tab[2,1,0] = tab[3,1,0]
        tab[2,1,1] = tab[3,1,1]
        tab[2,1,2] = tab[3,1,2]
        tab[2,2,0] = tab[3,2,0]
        tab[2,2,1] = tab[3,2,1]
        tab[2,2,2] = tab[3,2,2]
        tab[3,0,0] = tmp1
        tab[3,0,1] = tmp2
        tab[3,0,2] = tmp3
        tab[3,1,0] = tmp4
        tab[3,1,1] = tmp5
        tab[3,1,2] = tmp6
        tab[3,2,0] = tmp7
        tab[3,2,1] = tmp8
        tab[3,2,2] = tmp9
        # Pivot faces 4 et 5 sur elles-même
        # Pivot face 4 horaire
        tmp1 = tab[4,0,0]
        tmp2 = tab[4,0,1]
        tmp3 = tab[4,0,2]
        tab[4,0,1] = tab[4,1,0]
        tab[4,0,0] = tab[4,2,0]
        tab[4,1,0] = tab[4,2,1]
        tab[4,2,0] = tab[4,2,2]
        tab[4,2,1] = tab[4,1,2]
        tab[4,0,2] = tmp1
        tab[4,1,2] = tmp2
        tab[4,2,2] = tmp3
        # Pivot face 5 antihoraire
        tmp1 = tab[5,0,0]
        tmp2 = tab[5,0,1]
        tmp3 = tab[5,0,2]
        tab[5,0,1] = tab[5,1,2]
        tab[5,0,2] = tab[5,2,2]
        tab[5,1,2] = tab[5,2,1]
        tab[5,2,2] = tab[5,2,0]
        tab[5,2,1] = tab[5,1,0]
        tab[5,2,0] = tmp1
        tab[5,1,0] = tmp2
        tab[5,0,0] = tmp3

    # Mouvement invY de rotation antihoraire complète du cube suivant l'axe y
    def invY(self, cube):
        for i in range(0,3):
            self.y(cube)

    # Mouvement z de rotation horaire complète du cube suivant l'axe z
    def z(self, cube):
        tab = cube.getTab()
        # Rotation faces 1,4,3 et 5
        tmp1 = tab[1,0,0]
        tmp2 = tab[1,0,1]
        tmp3 = tab[1,0,2]
        tmp4 = tab[1,1,0]
        tmp5 = tab[1,1,1]
        tmp6 = tab[1,1,2]
        tmp7 = tab[1,2,0]
        tmp8 = tab[1,2,1]
        tmp9 = tab[1,2,2]
        tab[1,0,2] = tab[4,0,0]
        tab[1,0,1] = tab[4,1,0]
        tab[1,0,0] = tab[4,2,0]
        tab[1,1,0] = tab[4,2,1]
        tab[1,1,1] = tab[4,1,1]
        tab[1,1,2] = tab[4,0,1]
        tab[1,2,0] = tab[4,2,2]
        tab[1,2,1] = tab[4,1,2]
        tab[1,2,2] = tab[4,0,2]
        tab[4,2,2] = tab[3,0,2]
        tab[4,2,1] = tab[3,1,2]
        tab[4,2,0] = tab[3,2,2]
        tab[4,1,2] = tab[3,0,1]
        tab[4,1,1] = tab[3,1,1]
        tab[4,1,0] = tab[3,2,1]
        tab[4,0,2] = tab[3,0,0]
        tab[4,0,1] = tab[3,1,0]
        tab[4,0,0] = tab[3,2,0]
        tab[3,2,2] = tab[5,2,0]
        tab[3,2,1] = tab[5,1,0]
        tab[3,2,0] = tab[5,0,0]
        tab[3,1,2] = tab[5,2,1]
        tab[3,1,1] = tab[5,1,1]
        tab[3,1,0] = tab[5,0,1]
        tab[3,0,2] = tab[5,2,2]
        tab[3,0,1] = tab[5,1,2]
        tab[3,0,0] = tab[5,0,2]
        tab[5,0,0] = tmp3
        tab[5,0,1] = tmp6
        tab[5,0,2] = tmp9
        tab[5,1,0] = tmp2
        tab[5,1,1] = tmp5
        tab[5,1,2] = tmp8
        tab[5,2,0] = tmp1
        tab[5,2,1] = tmp4
        tab[5,2,2] = tmp7
        # Pivot faces 0 et 2 sur elles-même
        # Pivot face 0 horaire
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,0,1]
        tmp3 = tab[0,0,2]
        tab[0,0,1] = tab[0,1,0]
        tab[0,0,0] = tab[0,2,0]
        tab[0,1,0] = tab[0,2,1]
        tab[0,2,0] = tab[0,2,2]
        tab[0,2,1] = tab[0,1,2]
        tab[0,0,2] = tmp1
        tab[0,1,2] = tmp2
        tab[0,2,2] = tmp3
        # Pivot face 2 antihoraire
        tmp1 = tab[2,0,0]
        tmp2 = tab[2,0,1]
        tmp3 = tab[2,0,2]
        tab[2,0,1] = tab[2,1,2]
        tab[2,0,2] = tab[2,2,2]
        tab[2,1,2] = tab[2,2,1]
        tab[2,2,2] = tab[2,2,0]
        tab[2,2,1] = tab[2,1,0]
        tab[2,2,0] = tmp1
        tab[2,1,0] = tmp2
        tab[2,0,0] = tmp3

    # Mouvement invZ de rotation antihoraire complète du cube suivant l'axe z
    def invZ(self, cube):
        for i in range(0,3):
            self.z(cube)
