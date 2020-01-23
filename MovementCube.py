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
        tab[1,0,2] = tmp1
        tab[1,1,0] = tab[1,2,1]
        tab[1,2,0] = tab[1,2,2]
        tab[1,2,1] = tab[1,1,2]
        tab[1,2,2] = tmp3
        tab[1,1,2] = tmp2

    # Mouvement invRight face 0 (en face) : antihoraire arête droite
    def invRight(self, cube):
        for i in range (0,3):
            self.right(cube)

    # Mouvement left face 0 (en face) : antihoraire arête gauche
    def left(self, cube):
        tab = cube.getTab()
        # Rotation arête gauche face 0
        tmp1 = tab[0,0,0]
        tmp2 = tab[0,1,0]
        tmp3 = tab[0,2,0]

        tab[0,0,0] = tab[4,0,0]
        tab[0,1,0] = tab[4,1,0]
        tab[0,2,0] = tab[4,2,0]

        tab[4,0,0] = tab[2,2,0]
        tab[4,1,0] = tab[2,1,0]
        tab[4,2,0] = tab[2,0,0]

        tab[2,0,0] = tab[5,0,0]
        tab[2,1,0] = tab[5,1,0]
        tab[2,2,0] = tab[5,2,0]

        tab[5,0,0] = tmp3
        tab[5,1,0] = tmp2
        tab[5,2,0] = tmp1
        # Pivot face 3 sur elle-même
        tmp1 = tab[1,0,0]
        tmp2 = tab[1,0,1]
        tmp3 = tab[1,0,2]
        tab[1,0,1] = tab[1,1,0]
        tab[1,0,0] = tab[1,2,0]
        tab[1,0,2] = tmp1
        tab[1,1,0] = tab[1,2,1]
        tab[1,2,0] = tab[1,2,2]
        tab[1,2,1] = tab[1,1,2]
        tab[1,2,2] = tmp3
        tab[1,1,2] = tmp2
