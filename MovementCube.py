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
        tab[4,0,2] = tmp3
        tab[4,1,2] = tmp2
        tab[4,2,2] = tmp1
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
        tab[4,0,0] = tab[2,0,2]
        tab[4,1,0] = tab[2,1,2]
        tab[4,2,0] = tab[2,2,2]
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
        tab[4,2,0] = tmp1
        tab[4,1,0] = tmp2
        tab[4,0,0] = tmp3

    # Mouvement invUp face 0 (en face) : antihoraire arête haute
    def invUp(self, cube):
        for i in range(0,3):
            self.up(cube)
