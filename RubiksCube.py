import numpy as np
import MovementCube

class RubiksCube:

    # Par défaut on imagine un cube entièrement fait
    def __init__(self):
        tab = np.zeros((6,3,3))
        for i in range(0,6):
            tab[i,:,:] = i
        self.__tab = tab

    # Retourne un tableau représentant l'ensemble des faces de type coin
    def getCorners(self):
        tab = np.zeros((6,4))
        tab[0][0] = self.__tab[0,0,0]
        tab[0][1] = self.__tab[0,2,0]
        tab[0][2] = self.__tab[0,2,2]
        tab[0][3] = self.__tab[0,0,2]
        tab[1][0] = self.__tab[1,0,0]
        tab[1][1] = self.__tab[1,2,0]
        tab[1][2] = self.__tab[1,2,2]
        tab[1][3] = self.__tab[1,0,2]
        tab[2][0] = self.__tab[2,0,0]
        tab[2][1] = self.__tab[2,2,0]
        tab[2][2] = self.__tab[2,2,2]
        tab[2][3] = self.__tab[2,0,2]
        tab[3][0] = self.__tab[3,0,0]
        tab[3][1] = self.__tab[3,2,0]
        tab[3][2] = self.__tab[3,2,2]
        tab[3][3] = self.__tab[3,0,2]
        tab[4][0] = self.__tab[4,0,0]
        tab[4][1] = self.__tab[4,2,0]
        tab[4][2] = self.__tab[4,2,2]
        tab[4][3] = self.__tab[4,0,2]
        tab[5][0] = self.__tab[5,0,0]
        tab[5][1] = self.__tab[5,2,0]
        tab[5][2] = self.__tab[5,2,2]
        tab[5][3] = self.__tab[5,0,2]
        return tab

    def getEdges(self):
        tab = np.zeros((6,4))
        tab[0][0] = self.__tab[0,0,1]
        tab[0][1] = self.__tab[0,1,0]
        tab[0][2] = self.__tab[0,2,1]
        tab[0][3] = self.__tab[0,1,2]
        tab[1][0] = self.__tab[1,0,1]
        tab[1][1] = self.__tab[1,1,0]
        tab[1][2] = self.__tab[1,2,1]
        tab[1][3] = self.__tab[1,1,2]
        tab[2][0] = self.__tab[2,0,1]
        tab[2][1] = self.__tab[2,1,0]
        tab[2][2] = self.__tab[2,2,1]
        tab[2][3] = self.__tab[2,1,2]
        tab[3][0] = self.__tab[3,0,1]
        tab[3][1] = self.__tab[3,1,0]
        tab[3][2] = self.__tab[3,2,1]
        tab[3][3] = self.__tab[3,1,2]
        tab[4][0] = self.__tab[4,0,1]
        tab[4][1] = self.__tab[4,1,0]
        tab[4][2] = self.__tab[4,2,1]
        tab[4][3] = self.__tab[4,1,2]
        tab[5][0] = self.__tab[5,0,1]
        tab[5][1] = self.__tab[5,1,0]
        tab[5][2] = self.__tab[5,2,1]
        tab[5][3] = self.__tab[5,1,2]
        return tab

    def getTab(self):
        return self.__tab

    def setTab(self, tab):
        self.__tab = tab

    def getValTab(self, index1, index2, index3):
        return self.__tab[index1, index2, index3]

    def setValTab(self, index1, index2, index3, val):
        self.__tab[index1, index2, index3] = val
