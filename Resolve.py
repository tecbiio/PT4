import RubiksCube
import Movement as move

class Resolve():

    def solve(self, cube):
        self.posCube(cube)
        self.whiteCross(cube)

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
        if (cube.getValTab(0,1,1) == 3): # Face orange en face
            move.y(cube)
        # RubiksCube good positioning

    def whiteCross(self, cube):
        # Teste chaque arête pour placer la croix blanche
        """ mémo : Attention à placer les arêtes en ne modifiant pas les places des autres
        arêtes qui peuvent être bien placées """

        """ FACE VERTE """

        if (cube.getEdges()[0][0] == 4): # Arête blanche (0,0,1)
            if (cube.getEdges()[4][2] == 0): # Arête blanc/vert
                move.invFront(cube)
                move.up(cube)
                move.invLeft(cube)
                move.invUp(cube)
            if (cube.getEdges()[4][2] == 1): # Arête blanc/rouge
                move.front(cube)
                move.right(cube)
            if (cube.getEdges()[4][2] == 2): # Arête blanc/bleu
                move.invFront(cube)
                move.invUp(cube)
                move.invLeft(cube)
                move.invUp(cube)
            if (cube.getEdges()[4][2] == 3): # Arête blanc/orange
                move.invFront(cube)
                move.invLeft(cube)
        if (cube.getEdges()[0][1] == 4): # Arête blanche (0,1,0)
            if (cube.getEdges()[3][3] == 0): # Arête blanc/vert
                move.up(cube)
                move.invLeft(cube)
                move.invUp(cube)
            if (cube.getEdges()[3][3] == 1): # Arête blanc/rouge
                move.up(cube)
                move.front(cube)
                move.front(cube)
                move.invUp(cube)
                move.right(cube)
            if (cube.getEdges()[3][3] == 2): # Arête blanc/bleu
                move.invUp(cube)
                move.invLeft(cube)
                move.invUp(cube)
            if (cube.getEdges()[3][3] == 3): # Arête blanc/orange
                move.invLeft(cube)
        if (cube.getEdges()[0][2] == 4): # Arête blanche (0,2,1)
            if (cube.getEdges()[5][2] == 0): # Arête blanc/vert
                move.invFront(cube)
                move.invUp(cube)
                move.right(cube)
                move.up(cube)
            if (cube.getEdges()[5][2] == 1): # Arête blanc/rouge
                move.up(cube)
                move.invFront(cube)
                move.invUp(cube)
                move.right(cube)
            if (cube.getEdges()[5][2] == 2): # Arête blanc/bleu
                move.up(cube)
                move.up(cube)
                move.invFront(cube)
                move.invUp(cube)
                move.right(cube)
                move.invUp(cube)
            if (cube.getEdges()[5][2] == 3): # Arête blanc/orange
                move.invUp(cube)
                move.front(cube)
                move.up(cube)
                move.invLeft(cube)
        if (cube.getEdges()[0][3] == 4): # Arête blanche (0,1,2)
            if (cube.getEdges()[1][1] == 0): # Arête blanc/vert
                move.invUp(cube)
                move.right(cube)
                move.up(cube)
            if (cube.getEdges()[1][1] == 1): # Arête blanc/rouge
                move.right(cube)
            if (cube.getEdges()[1][1] == 2): # Arête blanc/bleu
                move.up(cube)
                move.right(cube)
                move.invUp(cube)
            if (cube.getEdges()[1][1] == 3): # Arête blanc/orange
                move.invUp(cube)
                move.front(cube)
                move.front(cube)
                move.up(cube)
                move.invLeft(cube)

        """ FACE ROUGE """

        if (cube.getEdges()[1][0] == 4): # Arête blanche (1,0,1)
            if (cube.getEdges()[4][3] == 0): # Arête blanc/vert
                move.invRight(cube)
                move.invFront(cube)
            if (cube.getEdges()[4][3] == 1): # Arête blanc/rouge
                move.invRight(cube)
                move.up(cube)
                move.invFront(cube)
                move.invUp(cube)
            if (cube.getEdges()[4][3] == 2): # Arête blanc/bleu
                move.right(cube)
                move.back(cube)
            if (cube.getEdges()[4][3] == 3): # Arête blanc/orange
                move.invRight(cube)
                move.invUp(cube)
                move.invFront(cube)
                move.up(cube)
        if (cube.getEdges()[1][1] == 4): # Arête blanche (1,1,0)
            if (cube.getEdges()[0][3] == 0): # Arête blanc/vert
                move.invFront(cube)
            if (cube.getEdges()[0][3] == 1): # Arête blanc/rouge
                move.up(cube)
                move.invFront(cube)
                move.invUp(cube)
            if (cube.getEdges()[0][3] == 2): # Arête blanc/bleu
                move.up(cube)
                move.right(cube)
                move.right(cube)
                move.invUp(cube)
                move.back(cube)
            if (cube.getEdges()[0][3] == 3): # Arête blanc/orange
                move.invUp(cube)
                move.invFront(cube)
                move.up(cube)
        if (cube.getEdges()[1][2] == 4): # Arête blanche (1,2,1)
            if (cube.getEdges()[5][1] == 0): # Arête blanc/vert
                move.invUp(cube)
                move.right(cube)
                move.up(cube)
                move.invFront(cube)
            if (cube.getEdges()[5][1] == 1): # Arête blanc/rouge
                move.right(cube)
                move.up(cube)
                move.invFront(cube)
                move.invUp(cube)
            if (cube.getEdges()[5][1] == 2): # Arête blanc/bleu
                move.up(cube)
                move.invRight(cube)
                move.invUp(cube)
                move.back(cube)
            if (cube.getEdges()[5][1] == 3): # Arête blanc/orange
                move.invUp(cube)
                move.invUp(cube)
                move.right(cube)
                move.up(cube)
                move.invFront(cube)
                move.up(cube)
        if (cube.getEdges()[1][3] == 4): # Arête blanche (1,1,2)
            if (cube.getEdges()[2][1] == 0): # Arête blanc/vert
                move.invUp(cube)
                move.invUp(cube)
                move.back(cube)
                move.up(cube)
                move.up(cube)
            if (cube.getEdges()[2][1] == 1): # Arête blanc/rouge
                move.invUp(cube)
                move.back(cube)
                move.up(cube)
            if (cube.getEdges()[2][1] == 2): # Arête blanc/bleu
                move.back(cube)
            if (cube.getEdges()[2][1] == 3): # Arête blanc/orange
                move.up(cube)
                move.back(cube)
                move.invUp(cube)

        """ FACE BLEUE """

        if (cube.getEdges()[2][0] == 4): # Arête blanche (2,0,1)
            if (cube.getEdges()[4][0] == 0): # Arête blanc/vert
                move.back(cube)
                move.invUp(cube)
                move.left(cube)
                move.invUp(cube)
                move.invFront(cube)
                move.invUp(cube)
                move.invUp(cube)
                move.front(cube)
            if (cube.getEdges()[4][0] == 1): # Arête blanc/rouge
                move.invBack(cube)
                move.invRight(cube)
            if (cube.getEdges()[4][0] == 2): # Arête blanc/bleu
                move.back(cube)
                move.invUp(cube)
                move.left(cube)
                move.up(cube)
            if (cube.getEdges()[4][0] == 3): # Arête blanc/orange
                move.back(cube)
                move.left(cube)
        if (cube.getEdges()[2][1] == 4): # Arête blanche (2,1,0)
            if (cube.getEdges()[1][3] == 0): # Arête blanc/vert
                move.invUp(cube)
                move.invRight(cube)
                move.up(cube)
            if (cube.getEdges()[1][3] == 1): # Arête blanc/rouge
                move.invRight(cube)
            if (cube.getEdges()[1][3] == 2): # Arête blanc/bleu
                move.up(cube)
                move.invRight(cube)
                move.invUp(cube)
            if (cube.getEdges()[1][3] == 3): # Arête blanc/orange
                move.up(cube)
                move.back(cube)
                move.back(cube)
                move.invUp(cube)
                move.left(cube)
        if (cube.getEdges()[2][2] == 4): # Arête blanche (2,2,1)
            if (cube.getEdges()[5][0] == 0): # Arête blanc/vert
                move.invUp(cube)
                move.invUp(cube)
                move.back(cube)
                move.up(cube)
                move.invRight(cube)
                move.up(cube)
            if (cube.getEdges()[5][0] == 1): # Arête blanc/rouge
                move.invUp(cube)
                move.back(cube)
                move.up(cube)
                move.invRight(cube)
            if (cube.getEdges()[5][0] == 2): # Arête blanc/bleu
                move.back(cube)
                move.up(cube)
                move.invRight(cube)
                move.invUp(cube)
            if (cube.getEdges()[5][0] == 3): # Arête blanc/orange
                move.up(cube)
                move.invBack(cube)
                move.invUp(cube)
                move.left(cube)
        if (cube.getEdges()[2][3] == 4): # Arête blanche (2,1,2)
            if (cube.getEdges()[3][1] == 0): # Arête blanc/vert
                move.up(cube)
                move.left(cube)
                move.invUp(cube)
            if (cube.getEdges()[3][1] == 1): # Arête blanc/rouge
                move.invUp(cube)
                move.invBack(cube)
                move.invBack(cube)
                move.up(cube)
                move.invRight(cube)
            if (cube.getEdges()[3][1] == 2): # Arête blanc/bleu
                move.invUp(cube)
                move.left(cube)
                move.up(cube)
            if (cube.getEdges()[3][1] == 3): # Arête blanc/orange
                move.left(cube)

        """ FACE ORANGE """

        if (cube.getEdges()[3][0] == 4): # Arête blanche (3,0,1)
            if (cube.getEdges()[4][1] == 0): # Arête blanc/vert
                move.left(cube)
                move.front(cube)
            if (cube.getEdges()[4][1] == 1): # Arête blanc/rouge
                move.left(cube)
                move.up(cube)
                move.front(cube)
                move.invUp(cube)
            if (cube.getEdges()[4][1] == 2): # Arête blanc/bleu
                move.invLeft(cube)
                move.invBack(cube)
            if (cube.getEdges()[4][1] == 3): # Arête blanc/orange
                move.left(cube)
                move.invUp(cube)
                move.front(cube)
                move.up(cube)
        if (cube.getEdges()[3][1] == 4): # Arête blanche (3,1,0)
            if (cube.getEdges()[2][3] == 0): # Arête blanc/vert
                move.up(cube)
                move.left(cube)
                move.left(cube)
                move.invUp(cube)
                move.front(cube)
            if (cube.getEdges()[2][3] == 1): # Arête blanc/rouge
                move.invUp(cube)
                move.invBack(cube)
                move.up(cube)
            if (cube.getEdges()[2][3] == 2): # Arête blanc/bleu
                move.invBack(cube)
            if (cube.getEdges()[2][3] == 3): # Arête blanc/orange
                move.up(cube)
                move.invBack(cube)
                move.invUp(cube)
        if (cube.getEdges()[3][2] == 4): # Arête blanche (3,2,1)
            if (cube.getEdges()[5][3] == 0): # Arête blanc/vert
                move.up(cube)
                move.invLeft(cube)
                move.invUp(cube)
                move.front(cube)
            if (cube.getEdges()[5][3] == 1): # Arête blanc/rouge
                move.up(cube)
                move.up(cube)
                move.invLeft(cube)
                move.invUp(cube)
                move.front(cube)
                move.invUp(cube)
            if (cube.getEdges()[5][3] == 2): # Arête blanc/bleu
                move.invUp(cube)
                move.left(cube)
                move.up(cube)
                move.invBack(cube)
            if (cube.getEdges()[5][3] == 3): # Arête blanc/orange
                move.invLeft(cube)
                move.invUp(cube)
                move.front(cube)
                move.up(cube)
        if (cube.getEdges()[3][3] == 4): # Arête blanche (3,1,2)
            if (cube.getEdges()[0][1] == 0): # Arête blanc/vert
                move.front(cube)
            if (cube.getEdges()[0][1] == 1): # Arête blanc/rouge
                move.up(cube)
                move.front(cube)
                move.invUp(cube)
            if (cube.getEdges()[0][1] == 2): # Arête blanc/bleu
                move.invUp(cube)
                move.invLeft(cube)
                move.invLeft(cube)
                move.up(cube)
                move.invBack(cube)
            if (cube.getEdges()[0][1] == 3): # Arête blanc/orange
                move.invUp(cube)
                move.front(cube)
                move.up(cube)

        """ FACE BLANCHE """

        if (cube.getEdges()[4][0] == 4): # Arête blanche (4,0,1)
            if (cube.getEdges()[2][0] == 0): # Arête blanc/vert
                move.back(cube)
                move.invUp(cube)
                move.left(cube)
                move.left(cube)
                move.up(cube)
                move.front(cube)
            if (cube.getEdges()[2][0] == 1): # Arête blanc/rouge
                move.invBack(cube)
                move.invRight(cube)
                move.invRight(cube)
                move.up(cube)
                move.invFront(cube)
                move.invUp(cube)
            # if (cube.getEdges()[2][0] == 2): # Arête blanc/bleu
            if (cube.getEdges()[2][0] == 3): # Arête blanc/orange
                move.back(cube)
                move.left(cube)
                move.left(cube)
                move.invUp(cube)
                move.front(cube)
                move.up(cube)
        if (cube.getEdges()[4][1] == 4): # Arête blanche (4,1,0)
            if (cube.getEdges()[3][0] == 0): # Arête blanc/vert
                move.invLeft(cube)
                move.up(cube)
                move.left(cube)
                move.invUp(cube)
            if (cube.getEdges()[3][0] == 1): # Arête blanc/rouge
                move.left(cube)
                move.up(cube)
                move.up(cube)
                move.invLeft(cube)
                move.invUp(cube)
                move.invUp(cube)
            if (cube.getEdges()[3][0] == 2): # Arête blanc/bleu
                move.left(cube)
                move.invUp(cube)
                move.invLeft(cube)
                move.up(cube)
            # if (cube.getEdges()[3][0] == 3): # Arête blanc/orange
        if (cube.getEdges()[4][2] == 4): # Arête blanche (4,2,1)
            # if (cube.getEdges()[0][0] == 0): # Arête blanc/vert
            if (cube.getEdges()[0][0] == 1): # Arête blanc/rouge
                move.invFront(cube)
                move.up(cube)
                move.front(cube)
                move.invUp(cube)
            if (cube.getEdges()[0][0] == 2): # Arête blanc/bleu
                move.front(cube)
                move.up(cube)
                move.up(cube)
                move.invFront(cube)
                move.up(cube)
                move.up(cube)
            if (cube.getEdges()[0][0] == 3): # Arête blanc/orange
                move.invFront(cube)
                move.invUp(cube)
                move.front(cube)
                move.up(cube)
        if (cube.getEdges()[4][3] == 4): # Arête blanche (4,1,2)
            if (cube.getEdges()[1][0] == 0): # Arête blanc/vert
                move.invRight(cube)
                move.invUp(cube)
                move.right(cube)
                move.up(cube)
            # if (cube.getEdges()[1][0] == 1): # Arête blanc/rouge
            if (cube.getEdges()[1][0] == 2): # Arête blanc/bleu
                move.invRight(cube)
                move.up(cube)
                move.right(cube)
                move.invUp(cube)
            if (cube.getEdges()[1][0] == 3): # Arête blanc/orange
                move.invRight(cube)
                move.invUp(cube)
                move.invUp(cube)
                move.right(cube)
                move.up(cube)
                move.up(cube)

        """ FACE JAUNE """

        if (cube.getEdges()[5][0] == 4): # Arête blanche (5,0,1)
            if (cube.getEdges()[2][2] == 0): # Arête blanc/vert
            if (cube.getEdges()[2][2] == 1): # Arête blanc/rouge
            if (cube.getEdges()[2][2] == 2): # Arête blanc/bleu
            if (cube.getEdges()[2][2] == 3): # Arête blanc/orange
        if (cube.getEdges()[5][1] == 4): # Arête blanche (5,1,0)
            if (cube.getEdges()[1][2] == 0): # Arête blanc/vert
            if (cube.getEdges()[1][2] == 1): # Arête blanc/rouge
            if (cube.getEdges()[1][2] == 2): # Arête blanc/bleu
            if (cube.getEdges()[1][2] == 3): # Arête blanc/orange
        if (cube.getEdges()[5][2] == 4): # Arête blanche (5,2,1)
            if (cube.getEdges()[0][2] == 0): # Arête blanc/vert
            if (cube.getEdges()[0][2] == 1): # Arête blanc/rouge
            if (cube.getEdges()[0][2] == 2): # Arête blanc/bleu
            if (cube.getEdges()[0][2] == 3): # Arête blanc/orange
        if (cube.getEdges()[5][3] == 4): # Arête blanche (5,1,2)
            if (cube.getEdges()[3][2] == 0): # Arête blanc/vert
            if (cube.getEdges()[3][2] == 1): # Arête blanc/rouge
            if (cube.getEdges()[3][2] == 2): # Arête blanc/bleu
            if (cube.getEdges()[3][2] == 3): # Arête blanc/orange

            # whiteCross checked
