import Movement
import RubiksCube

cube = RubiksCube.RubiksCube()
move = Movement.Movement()
move.initialisation()
move.invDown(cube)
move.up(cube)
move.invLeft(cube)
move.invDown(cube)
move.right(cube)
move.down(cube)
move.left(cube)
move.invUp(cube)
move.invRight(cube)
move.fin()