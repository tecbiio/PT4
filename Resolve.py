import RubiksCube
import Movement as move

class Resolve():

    def solve(self, cube):
        self.posCube(cube)
        self.whiteCross(cube)
        self.whiteFace(cube)

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
                move.up(cube)
                move.up(cube)
                move.right(cube)
                move.up(cube)
                move.invFront(cube)
                move.up(cube)
        if (cube.getEdges()[1][3] == 4): # Arête blanche (1,1,2)
            if (cube.getEdges()[2][1] == 0): # Arête blanc/vert
                move.up(cube)
                move.up(cube)
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
                move.up(cube)
                move.up(cube)
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
                move.up(cube)
                move.up(cube)
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
                move.back(cube)
                move.back(cube)
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
                move.left(cube)
                move.left(cube)
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
                move.right(cube)
                move.right(cube)
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
                move.up(cube)
                move.up(cube)
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
                move.up(cube)
                move.up(cube)
                move.right(cube)
                move.up(cube)
                move.up(cube)

        """ FACE JAUNE """

        if (cube.getEdges()[5][0] == 4): # Arête blanche (5,0,1)
            if (cube.getEdges()[2][2] == 0): # Arête blanc/vert
                move.down(cube)
                move.down(cube)
                move.front(cube)
                move.front(cube)
            if (cube.getEdges()[2][2] == 1): # Arête blanc/rouge
                move.invDown(cube)
                move.right(cube)
                move.right(cube)
            if (cube.getEdges()[2][2] == 2): # Arête blanc/bleu
                move.back(cube)
                move.back(cube)
            if (cube.getEdges()[2][2] == 3): # Arête blanc/orange
                move.down(cube)
                move.left(cube)
                move.left(cube)
        if (cube.getEdges()[5][1] == 4): # Arête blanche (5,1,0)
            if (cube.getEdges()[1][2] == 0): # Arête blanc/vert
                move.invDown(cube)
                move.front(cube)
                move.front(cube)
            if (cube.getEdges()[1][2] == 1): # Arête blanc/rouge
                move.right(cube)
                move.right(cube)
            if (cube.getEdges()[1][2] == 2): # Arête blanc/bleu
                move.down(cube)
                move.back(cube)
                move.back(cube)
            if (cube.getEdges()[1][2] == 3): # Arête blanc/orange
                move.down(cube)
                move.down(cube)
                move.right(cube)
                move.right(cube)
        if (cube.getEdges()[5][2] == 4): # Arête blanche (5,2,1)
            if (cube.getEdges()[0][2] == 0): # Arête blanc/vert
                move.front(cube)
                move.front(cube)
            if (cube.getEdges()[0][2] == 1): # Arête blanc/rouge
                move.down(cube)
                move.right(cube)
                move.right(cube)
            if (cube.getEdges()[0][2] == 2): # Arête blanc/bleu
                move.down(cube)
                move.down(cube)
                move.back(cube)
                move.back(cube)
            if (cube.getEdges()[0][2] == 3): # Arête blanc/orange
                move.invDown(cube)
                move.left(cube)
                move.left(cube)
        if (cube.getEdges()[5][3] == 4): # Arête blanche (5,1,2)
            if (cube.getEdges()[3][2] == 0): # Arête blanc/vert
                move.down(cube)
                move.front(cube)
                move.front(cube)
            if (cube.getEdges()[3][2] == 1): # Arête blanc/rouge
                move.down(cube)
                move.down(cube)
                move.right(cube)
                move.right(cube)
            if (cube.getEdges()[3][2] == 2): # Arête blanc/bleu
                move.invDown(cube)
                move.back(cube)
                move.back(cube)
            if (cube.getEdges()[3][2] == 3): # Arête blanc/orange
                move.left(cube)
                move.left(cube)
        # whiteCross checked

    def whiteFace(self, cube):
        # Teste chaque coin pour placer la face blanche

        """ FACE VERTE """

        if (cube.getCorners()[0][0] == 4): # Coin (0,0,0) blanc-?-?
            if (cube.getCorners()[4][1] == 0): # Coin (4,2,0) blanc-vert-?
            # Une seule disposition possible (0,0,0)-(4,2,0)-(3,0,2) -> blanc-vert-rouge
            # Car blanc-vert-vert ou blanc-vert-bleu ou blanc-vert-blanc
            # ou encore blanc-vert-jaune n'existent pas.
            # blanc-vert-orange est impossible à produire, ou s'il est produit
            # par changement de couleur (triche) le cube devient insolvable
            # CQFD : (0,0,0)-(4,2,0)-(3,0,2) / blanc-vert-orange : impossible
            # => Pas besoin de tester la troisième couleur
                move.invFront(cube) # Placement
                move.down(cube)
                move.front(cube)
                move.down(cube)
                move.invRight(cube) # 1
                move.invDown(cube)
                move.right(cube)
                move.down(cube)
                move.invRight(cube) # 2
                move.invDown(cube)
                move.right(cube)
                move.down(cube)
                move.invRight(cube) # 3
                move.invDown(cube)
                move.right(cube)
            if (cube.getCorners()[4][1] == 1): # Coin (4,2,0) blanc-rouge-bleu
                move.invFront(cube) # Placement
                move.down(cube)
                move.front(cube)
                move.down(cube)
                move.down(cube)
                move.invBack(cube) # 1
                move.invDown(cube)
                move.back(cube)
                move.down(cube)
                move.invBack(cube) # 2
                move.invDown(cube)
                move.back(cube)
                move.down(cube)
                move.invBack(cube) # 3
                move.invDown(cube)
                move.back(cube)
            if (cube.getCorners()[4][1] == 2): # Coin (4,2,0) blanc-bleu-orange
                move.invFront(cube) # Placement
                move.invDown(cube)
                move.front(cube)
                move.invLeft(cube) # 1
                move.invDown(cube)
                move.left(cube)
            if (cube.getCorners()[4][1] == 3): # Coin (4,2,0) blanc-orange-vert
                move.invFront(cube) # Placement
                move.invDown(cube)
                move.front(cube)
                move.down(cube) # 1
                move.invFront(cube)
                move.invDown(cube)
                move.front(cube)
        if (cube.getCorners()[0][1] == 4): # Coin (0,2,0) blanc-?-?
            if (cube.getCorners()[5][2] == 0): # Coin (5,2,2) blanc-vert-orange
                move.invFront(cube)
                move.invDown(cube)
                move.front(cube)
            if (cube.getCorners()[5][2] == 1): # Coin (5,2,2) blanc-rouge-vert
                move.down(cube)
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
            if (cube.getCorners()[5][2] == 2): # Coin (5,2,2) blanc-bleu-rouge
                move.down(cube)
                move.down(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
            if (cube.getCorners()[5][2] == 3): # Coin (5,2,2) blanc-orange-bleu
                move.invDown(cube)
                move.invLeft(cube)
                move.invDown(cube)
                move.left(cube)
        if (cube.getCorners()[0][2] == 4): # Coin (0,2,2) blanc-?-?
            if (cube.getCorners()[5][1] == 0): # Coin (5,2,0) blanc-vert-rouge
                move.invDown(cube)
                move.invRight(cube)
                move.down(cube)
                move.right(cube)
            if (cube.getCorners()[5][1] == 1): # Coin (5,2,0) blanc-rouge-bleu
                move.invBack(cube)
                move.down(cube)
                move.back(cube)
                move.invDown(cube)
            if (cube.getCorners()[5][1] == 2): # Coin (5,2,0) blanc-bleu-orange
                move.invLeft(cube)
                move.down(cube)
                move.down(cube)
                move.left(cube)
            if (cube.getCorners()[5][1] == 3): # Coin (5,2,0) blanc-orange-vert
                move.down(cube)
                move.invFront(cube)
                move.invDown(cube)
                move.invDown(cube)
                move.front(cube)
        if (cube.getCorners()[0][3] == 4): # Coin (0,0,2) blanc-?-?
            if (cube.getCorners()[4][2] == 0): # Coin (4,2,2) blanc-vert-orange
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
                move.invFront(cube) # 1
                move.invDown(cube)
                move.front(cube)
                move.down(cube)
                move.invFront(cube) # 2
                move.invDown(cube)
                move.front(cube)
                move.down(cube)
                move.invFront(cube) # 3
                move.invDown(cube)
                move.front(cube)
            if (cube.getCorners()[4][2] == 1): # Coin (4,2,2) blanc-rouge-vert
                move.invRight(cube)
                move.down(cube)
                move.right(cube)
                move.invDown(cube)
                move.invRight(cube)
                move.down(cube)
                move.right(cube)
            if (cube.getCorners()[4][2] == 2): # Coin (4,2,2) blanc-bleu-rouge
                move.invRight(cube)
                move.down(cube)
                move.right(cube)
                move.invBack(cube)
                move.down(cube)
                move.back(cube)
            if (cube.getCorners()[4][2] == 3): # Coin (4,2,2) blanc-orange-bleu
                move.invRight(cube)
                move.down(cube)
                move.right(cube)
                move.invLeft(cube)
                move.down(cube)
                move.down(cube)
                move.left(cube)

        """ FACE ROUGE """

        if (cube.getCorners()[1][0] == 4): # Coin (1,0,0) blanc-?-?
            if (cube.getCorners()[4][2] == 0): # Coin (4,2,2) blanc-vert-rouge
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
                move.down(cube)
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
            if (cube.getCorners()[4][2] == 1): # Coin (4,2,2) blanc-rouge-bleu
                move.invRight(cube)
                move.down(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
                move.right(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
            if (cube.getCorners()[4][2] == 2): # Coin (4,2,2) blanc-bleu-orange
                move.invRight(cube)
                move.down(cube)
                move.down(cube)
                move.invLeft(cube)
                move.invDown(cube)
                move.left(cube)
            if (cube.getCorners()[4][2] == 3): # Coin (4,2,2) blanc-orange-vert
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
                move.invFront(cube)
                move.invDown(cube)
                move.front(cube)
        if (cube.getCorners()[1][1] == 4): # Coin (1,2,0) blanc-?-?
            if (cube.getCorners()[5][1] == 0): # Coin (5,2,0) blanc-vert-orange
                move.left(cube)
                move.invDown(cube)
                move.invLeft(cube)
            if (cube.getCorners()[5][1] == 1): # Coin (5,2,0) blanc-rouge-vert
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
            if (cube.getCorners()[5][1] == 2): # Coin (5,2,0) blanc-bleu-rouge
                move.down(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
            if (cube.getCorners()[5][1] == 3): # Coin (5,2,0) blanc-orange-bleu
                move.invDown(cube)
                move.back(cube)
                move.invDown(cube)
                move.invBack(cube)
        if (cube.getCorners()[1][2] == 4): # Coin (1,2,2) blanc-?-?
            if (cube.getCorners()[5][0] == 0): # Coin (5,0,0) blanc-vert-rouge
                move.down(cube)
                move.down(cube)
                move.invRight(cube)
                move.down(cube)
                move.right(cube)
            if (cube.getCorners()[5][0] == 1): # Coin (5,0,0) blanc-rouge-bleu
                move.invDown(cube)
                move.invBack(cube)
                move.down(cube)
                move.back(cube)
            if (cube.getCorners()[5][0] == 2): # Coin (5,0,0) blanc-bleu-orange
                move.invLeft(cube)
                move.down(cube)
                move.left(cube)
            if (cube.getCorners()[5][0] == 3): # Coin (5,0,0) blanc-orange-vert
                move.down(cube)
                move.invFront(cube)
                move.down(cube)
                move.front(cube)
        if (cube.getCorners()[1][3] == 4): # Coin (1,0,2) blanc-?-?
            if (cube.getCorners()[4][3] == 0): # Coin (4,0,2) blanc-vert-orange

            if (cube.getCorners()[4][3] == 1): # Coin (4,0,2) blanc-rouge-vert
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
                move.down(cube)
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
                move.down(cube)
                move.invRight(cube)
                move.invDown(cube)
                move.right(cube)
            if (cube.getCorners()[4][3] == 2): # Coin (4,0,2) blanc-bleu-rouge
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
                move.down(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
                move.down(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
                move.down(cube)
                move.invBack(cube)
                move.invDown(cube)
                move.back(cube)
            if (cube.getCorners()[4][3] == 3): # Coin (4,0,2) blanc-orange-bleu

        """ FACE BLEUE """

        if (cube.getCorners()[2][0] == 4): # Coin (2,0,0) blanc-?-?
            if (cube.getCorners()[4][3] == 0): # Coin (4,0,2) blanc-vert-rouge
            if (cube.getCorners()[4][3] == 1): # Coin (4,0,2) blanc-rouge-bleu
            if (cube.getCorners()[4][3] == 2): # Coin (4,0,2) blanc-bleu-orange
            if (cube.getCorners()[4][3] == 3): # Coin (4,0,2) blanc-orange-vert
        if (cube.getCorners()[2][1] == 4): # Coin (2,2,0) blanc-?-?
            if (cube.getCorners()[5][0] == 0): # Coin (5,0,0) blanc-vert-orange
            if (cube.getCorners()[5][0] == 1): # Coin (5,0,0) blanc-rouge-vert
            if (cube.getCorners()[5][0] == 2): # Coin (5,0,0) blanc-bleu-rouge
            if (cube.getCorners()[5][0] == 3): # Coin (5,0,0) blanc-orange-bleu
        if (cube.getCorners()[2][2] == 4): # Coin (2,2,2) blanc-?-?
            if (cube.getCorners()[5][3] == 0): # Coin (5,0,2) blanc-vert-rouge
            if (cube.getCorners()[5][3] == 1): # Coin (5,0,2) blanc-rouge-bleu
            if (cube.getCorners()[5][3] == 2): # Coin (5,0,2) blanc-bleu-orange
            if (cube.getCorners()[5][3] == 3): # Coin (5,0,2) blanc-orange-vert
        if (cube.getCorners()[2][3] == 4): # Coin (2,0,2) blanc-?-?
            if (cube.getCorners()[4][0] == 0): # Coin (4,0,0) blanc-vert-orange
            if (cube.getCorners()[4][0] == 1): # Coin (4,0,0) blanc-rouge-vert
            if (cube.getCorners()[4][0] == 2): # Coin (4,0,0) blanc-bleu-rouge
            if (cube.getCorners()[4][0] == 3): # Coin (4,0,0) blanc-orange-bleu

        """ FACE ORANGE """

        if (cube.getCorners()[3][0] == 4): # Coin (3,0,0) blanc-?-?
            if (cube.getCorners()[4][0] == 0): # Coin (4,0,0) blanc-vert-rouge
            if (cube.getCorners()[4][0] == 1): # Coin (4,0,0) blanc-rouge-bleu
            if (cube.getCorners()[4][0] == 2): # Coin (4,0,0) blanc-bleu-orange
            if (cube.getCorners()[4][0] == 3): # Coin (4,0,0) blanc-orange-vert
        if (cube.getCorners()[3][1] == 4): # Coin (3,2,0) blanc-?-?
            if (cube.getCorners()[5][3] == 0): # Coin (5,0,2) blanc-vert-orange
            if (cube.getCorners()[5][3] == 1): # Coin (5,0,2) blanc-rouge-vert
            if (cube.getCorners()[5][3] == 2): # Coin (5,0,2) blanc-bleu-rouge
            if (cube.getCorners()[5][3] == 3): # Coin (5,0,2) blanc-orange-bleu
        if (cube.getCorners()[3][2] == 4): # Coin (3,2,2) blanc-?-?
            if (cube.getCorners()[5][2] == 0): # Coin (5,2,2) blanc-vert-rouge
            if (cube.getCorners()[5][2] == 1): # Coin (5,2,2) blanc-rouge-bleu
            if (cube.getCorners()[5][2] == 2): # Coin (5,2,2) blanc-bleu-orange
            if (cube.getCorners()[5][2] == 3): # Coin (5,2,2) blanc-orange-vert
        if (cube.getCorners()[3][3] == 4): # Coin (3,0,2) blanc-?-?
            if (cube.getCorners()[4][1] == 0): # Coin (4,2,0) blanc-vert-orange
            if (cube.getCorners()[4][1] == 1): # Coin (4,2,0) blanc-rouge-vert
            if (cube.getCorners()[4][1] == 2): # Coin (4,2,0) blanc-bleu-rouge
            if (cube.getCorners()[4][1] == 3): # Coin (4,2,0) blanc-orange-bleu

        """ FACE BLANCHE """

        if (cube.getCorners()[4][0] == 4): # Coin (4,0,0) blanc-?-?
            if (cube.getCorners()[2][3] == 0): # Coin (2,0,2) blanc-vert-rouge
            if (cube.getCorners()[2][3] == 1): # Coin (2,0,2) blanc-rouge-bleu
            # if (cube.getCorners()[2][3] == 2): # Coin (2,0,2) blanc-bleu-orange
            if (cube.getCorners()[2][3] == 3): # Coin (2,0,2) blanc-orange-vert
        if (cube.getCorners()[4][1] == 4): # Coin (4,2,0) blanc-?-?
            # if (cube.getCorners()[0][0] == 0): # Coin (0,0,0) blanc-vert-orange
            if (cube.getCorners()[0][0] == 1): # Coin (0,0,0) blanc-rouge-vert
            if (cube.getCorners()[0][0] == 2): # Coin (0,0,0) blanc-bleu-rouge
            if (cube.getCorners()[0][0] == 3): # Coin (0,0,0) blanc-orange-bleu
        if (cube.getCorners()[4][2] == 4): # Coin (4,2,2) blanc-?-?
            # if (cube.getCorners()[0][3] == 0): # Coin (0,0,2) blanc-vert-rouge
            if (cube.getCorners()[0][3] == 1): # Coin (0,0,2) blanc-rouge-bleu
            if (cube.getCorners()[0][3] == 2): # Coin (0,0,2) blanc-bleu-orange
            if (cube.getCorners()[0][3] == 3): # Coin (0,0,2) blanc-orange-vert
        if (cube.getCorners()[4][3] == 4): # Coin (4,0,2) blanc-?-?
            if (cube.getCorners()[2][0] == 0): # Coin (2,0,0) blanc-vert-orange
            if (cube.getCorners()[2][0] == 1): # Coin (2,0,0) blanc-rouge-vert
            # if (cube.getCorners()[2][0] == 2): # Coin (2,0,0) blanc-bleu-rouge
            if (cube.getCorners()[2][0] == 3): # Coin (2,0,0) blanc-orange-bleu

        """ FACE JAUNE """

        if (cube.getCorners()[5][0] == 4): # Coin (5,0,0) blanc-?-?
            if (cube.getCorners()[2][1] == 0): # Coin (2,2,0) blanc-vert-rouge
            if (cube.getCorners()[2][1] == 1): # Coin (2,2,0) blanc-rouge-bleu
            if (cube.getCorners()[2][1] == 2): # Coin (2,2,0) blanc-bleu-orange
            if (cube.getCorners()[2][1] == 3): # Coin (2,2,0) blanc-orange-vert
        if (cube.getCorners()[5][1] == 4): # Coin (5,2,0) blanc-?-?
            if (cube.getCorners()[0][2] == 0): # Coin (0,2,2) blanc-vert-orange
            if (cube.getCorners()[0][2] == 1): # Coin (0,2,2) blanc-rouge-vert
            if (cube.getCorners()[0][2] == 2): # Coin (0,2,2) blanc-bleu-rouge
            if (cube.getCorners()[0][2] == 3): # Coin (0,2,2) blanc-orange-bleu
        if (cube.getCorners()[5][2] == 4): # Coin (5,2,2) blanc-?-?
            if (cube.getCorners()[0][1] == 0): # Coin (0,2,0) blanc-vert-rouge
            if (cube.getCorners()[0][1] == 1): # Coin (0,2,0) blanc-rouge-bleu
            if (cube.getCorners()[0][1] == 2): # Coin (0,2,0) blanc-bleu-orange
            if (cube.getCorners()[0][1] == 3): # Coin (0,2,0) blanc-orange-vert
        if (cube.getCorners()[5][3] == 4): # Coin (5,0,2) blanc-?-?
            if (cube.getCorners()[2][2] == 0): # Coin (2,2,2) blanc-vert-orange
            if (cube.getCorners()[2][2] == 1): # Coin (2,2,2) blanc-rouge-vert
            if (cube.getCorners()[2][2] == 2): # Coin (2,2,2) blanc-bleu-rouge
            if (cube.getCorners()[2][2] == 3): # Coin (2,2,2) blanc-orange-bleu
