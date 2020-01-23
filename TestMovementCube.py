import RubiksCube
import MovementCube

cube = RubiksCube.RubiksCube()
mc = MovementCube.Movement()
print(cube.getTab())
mc.right(cube)
print(cube.getTab())
