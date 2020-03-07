import Movement
import RubiksCube

cube = RubiksCube.RubiksCube()
move = Movement.Movement()
move.fin()
move.initialisation()
move.right(cube)
move.down(cube)
move.left(cube)
move.invUp(cube)
move.invRight(cube)
move.fin()