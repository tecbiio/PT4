import RubiksCube
import Movement

class Resolve():

    def posCube(self, cube):
        if (cube.getValTab(0,1,1) == 4): # Face blanche en face
            move.x(cube)
        if (cube.getValTab(1,1,1) == 4): # Face blanche à droite
            move.y(cube)
            move.x(cube)
        if (cube.getValTab(2,1,1) == 4): # Face blanche derrière
            move.invX(cube)
        if (cube.getValTab(3,1,1) == 4): # Face blanche à gauche
            move.invY(cube)
            move.x(cube)
        if (cube.getValTab(5,1,1) == 4): # Face blanche en dessous
            move.x(cube)
            move.x(cube)
        if (cube.getValTab(0,1,1) == 1): # Face rouge en face
            move.invY(cube)
        if (cube.getValTab(0,1,1) == 2): # Face bleue en face
            move.invY(cube)
            move.invY(cube)
        if (cube.getValTab(0,1,1) == 3): # Face rouge en face
            move.y(cube)
    # RubiksCube good positioning

    def whiteCross(self, cube):
        # Parcourir le tableau d'arête
        if (cube.getEdges()[0].count(0) > 0): # Arêtes blanches face 0
            if (cube.getEdges()[0][0] == 4): # Arête blanche (0,0,1)
                if (cube.getEdges()[4][2] == 0): # Arête blanc/vert
                    move.invFront(cube)
                    move.invLeft(cube)
                    move.invUp(cube)
                if (cube.getEdges()[4][2] == 1): # Arête blanc/rouge
                    move.front(cube)
                    move.right(cube)
                if (cube.getEdges()[4][2] == 2): # Arête blanc/bleu
                    move.invFront(cube)
                    move.invLeft(cube)
                    move.up(cube)
                if (cube.getEdges()[4][2] == 3): # Arête blanc/orange
                    move.invFront(cube)
                    move.invLeft(cube)
            if (cube.getEdges()[0][1] == 4): # Arête blanche (0,1,0)
                if (cube.getEdges()[3][3] == 0): # Arête blanc/vert
                    move.invLeft(cube)
                    move.invUp(cube)
                if (cube.getEdges()[3][3] == 1): # Arête blanc/rouge
                    move.front(cube)
                    move.front(cube)
                    move.right(cube)
                #TODO
                if (cube.getEdges()[3][3] == 2): # Arête blanc/bleu
                    move.invLeft(cube)
                    move.invUp(cube)
                if (cube.getEdges()[3][3] == 3): # Arête blanc/orange
                    move.invLeft(cube)
                    move.invUp(cube)
            if (cube.getEdges()[0][2] == 4):
                if (cube.getEdges()[5][0] == 1):
                    

        # Placer les arêtes blanches
