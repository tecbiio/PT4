import Movement
import RubiksCube

cube = RubiksCube.RubiksCube()
move = Movement.Movement()
move.initialisation()
move.right(cube)
move.up(cube)
move.invLeft(cube)
move.invDown(cube)
move.invRight(cube)
move.down(cube)
move.left(cube)
move.invUp(cube)
move.down(cube)
move.fin()