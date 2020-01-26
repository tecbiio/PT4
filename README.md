Le cube est représenté par un tableau 3D, les faces sont numérotés de 0 à 5  
0 en face, 1 à droite, 2 derrière, 3 à gauche, 4 au dessus et 5 en dessous

LES COULEURS N'ONT AUCUN IMPACT SUR LE TRAITEMENT DES MOUVEMENTS

On ne traite que des mouvements avec la face 0 car le robot ne les effectue qu'avec celle là


Les fonctions de mouvements ne font que déplacer des couleurs, la face 0 peut donc être verte, bleu, rouge, orange, blanche ou encore jaune (la couleur centrale de coordonnées (1,1) correspond à la couleur de la face)   

## Fichier MovementCube.py  
Fonctions de mouvements numériquement :        
- right, left, up, down, front, back (mouvements horaires)
- leurs opposés (mouvements antihoraires)
# Rotation d'une face du cube dans l'espace   
- x, y, z
- leurs opposés (mouvements antihoraires)
# Rotations complètes du cube dans l'espace   

## Fichier TestMovementCube.py
Test de la bonne fonctionnalité des fonctions implémentées dans le précédent fichier   

## Fichier MovementRobot.py
Fonctions de mouvements physiquement :    
- right, left, up, down, front, back (mouvements horaires)
- leurs opposés (mouvements antihoraires)
# Rotation d'une face du cube dans l'espace   
- x, y, z
- leurs opposés (mouvements antihoraires)
# Rotations complètes du cube dans l'espace   

## Fichier TestMovementRobot.py
Test de la bonne fonctionnalité des fonctions implémentées dans le précédent fichier
(déjà effectuée)   

## Fichier RubiksCube.py
Objet représentant un cube sous forme d'un tableau à trois dimensions représentant les couleurs sur chaque faces   
