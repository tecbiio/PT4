import RubiksCube
import MovementCube

cube = RubiksCube.RubiksCube()
mc = MovementCube.Movement()
mc.x(cube)
mc.right(cube)
mc.invUp(cube)
mc.z(cube)
mc.invLeft(cube)
print(cube.getTab())
