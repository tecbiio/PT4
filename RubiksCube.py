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
        tab = [0]*24
        tab[0] = self.__tab[0,0,0]
        tab[1] = self.__tab[0,2,0]
        tab[2] = self.__tab[0,2,2]
        tab[3] = self.__tab[0,0,2]
        tab[4] = self.__tab[1,0,0]
        tab[5] = self.__tab[1,2,0]
        tab[6] = self.__tab[1,2,2]
        tab[7] = self.__tab[1,0,2]
        tab[8] = self.__tab[2,0,0]
        tab[9] = self.__tab[2,2,0]
        tab[10] = self.__tab[2,2,2]
        tab[11] = self.__tab[2,0,2]
        tab[12] = self.__tab[3,0,0]
        tab[13] = self.__tab[3,2,0]
        tab[14] = self.__tab[3,2,2]
        tab[15] = self.__tab[3,0,2]
        tab[16] = self.__tab[4,0,0]
        tab[17] = self.__tab[4,2,0]
        tab[18] = self.__tab[4,2,2]
        tab[19] = self.__tab[4,0,2]
        tab[20] = self.__tab[5,0,0]
        tab[21] = self.__tab[5,2,0]
        tab[22] = self.__tab[5,2,2]
        tab[23] = self.__tab[5,0,2]
        return tab


    def getTab(self):
        return self.__tab

    def setTab(self, tab):
        self.__tab = tab

    def getValTab(self, index1, index2, index3):
        return self.__tab[index1, index2, index3]

    def setValTab(self, index1, index2, index3, val):
        self.__tab[index1, index2, index3] = val
