import numpy as np
import MovementCube

class RubiksCube:

    # Par défaut on imagine un cube entièrement fait
    def __init__(self):
        tab = np.zeros((6,3,3))
        for i in range(0,6):
            tab[i,:,:] = i
        self.__tab = tab

    def getTab(self):
        return self.__tab

    def setTab(self, tab):
        self.__tab = tab

    def getValTab(self, index1, index2, index3):
        return self.__tab[index1, index2, index3]

    def setValTab(self, index1, index2, index3, val):
        self.__tab[index1, index2, index3] = val
