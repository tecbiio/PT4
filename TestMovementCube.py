import RubiksCube
import MovementCube

cube = RubiksCube.RubiksCube()
mc = MovementCube.Movement()
print("#########################################")
print(cube.getTab())
mc.right(cube)
print("#########################################")
print(cube.getTab())
mc.left(cube)
print("#########################################")
print(cube.getTab())
mc.up(cube)
print("#########################################")
