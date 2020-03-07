import Movement
import RubiksCube

cube = RubiksCube.RubiksCube()
move = Movement.Movement()
move.fin()
move.initialisation()
move.right(cube)
move.up(cube)
move.invLeft(cube)
move.invDown(cube)
move.invRight(cube)
move.fin()