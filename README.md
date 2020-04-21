Le cube est représenté par un tableau 3D, les faces sont numérotés de 0 à 5 :
- face 0 en face
- face 1 à droite
- face 2 derrière
- face 3 à gauche
- face 4 au dessus
- face 5 en dessous

Les valeurs dans le tableau correspondent aux couleurs :
- 0 - vert
- 1 - rouge
- 2 - bleu
- 3 - orange
- 4 - blanc
- 5 - jaune

LES COULEURS N'ONT AUCUN IMPACT SUR LE TRAITEMENT DES MOUVEMENTS

On ne traite que des mouvements avec la face 0 car le robot ne les effectue qu'avec celle là

Avec la résolution du cube, on place le Rubik's Cube de façon à que :
- La face verte soit en face (0)
- La face rouge soit à droite (1)
- La face bleue soit derrière (2)
- La face orange soit à gauche (3)
- La face blanche soit au dessus (4)
- La face jaune soit en dessous (5)

# Fichier RubiksCube.py
## Objet représentant un cube sous la forme d'un tableau 3D où, le premier indice indique les faces et les deux derniers indiquent la position de la couleur.  
- __init__() : Création du tableau 3D initialement résolu
- getCorners() : Retourne un tableau 2D de chaque coin du cube
- getEdges() : Retourne un tableau 2D de chaque arête du cube
- getTab() : Retourne le tableau 3D
- setTab() : Change le tableau 3D par un autre
- getValTab() : Retourne la valeur du tableau 3D avec les indices
- setValTab() : Change une valeur du tableau 3D par un paramètre

# Fichier MovementCube.py  
## Fonctions de mouvements numériques :     
### Rotation d'une face du cube dans l'espace      
- right(), left(), up(), down(), front(), back()  
- leurs opposés (mouvements antihoraires)
### Rotations complètes du cube dans l'espace   
- x(), y(), z()
- leurs opposés (mouvements antihoraires)   

# Fichier MovementRobot.py
## Fonctions de mouvements physiques :
### Rotation d'une face du cube dans l'espace     
- right(), left(), up(), down(), front(), back()
- leurs opposés (mouvements antihoraires)
### Rotations complètes du cube dans l'espace
- x(), y(), z()
- leurs opposés (mouvements antihoraires)

# Fichier Movement.py
## Fonctions de mouvements physiques et numériques :
### Rotation d'une face du cube dans l'espace
- right(), left(), up(), down(), front(), back()
- leurs opposés (mouvements antihoraires)
### Rotations complètes du cube dans l'espace
- x(), y(), z()
- leurs opposés (mouvements antihoraires)

# Fichier Resolve.py
## Fonctions d'algorithmes de résolution :
- solve() : Résoud le Rubik's Cube (Appel de toutes les autres fonctions)
- posCube() : Positionne le Rubik's Cube avec le placement des faces par défaut
- whiteCross() : Effectue la croix blanche
- whiteFace() : Effectue la face blanche
- crown() : Effectue la deuxième couronne (Non Implémenté)
- yellowCrossOne() : Effectue la croix jaune (Non Implémenté)
- yellowCrossTwo() : Effectue la croix jaune avec les bonnes arêtes (NI)
- yellowCorners() : Place les coins jaunes (NI)
- yellowFace() : Effectue la face jaune (NI)
