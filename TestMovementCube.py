import RubiksCube
import MovementCube

cube = RubiksCube.RubiksCube()
mc = MovementCube.Movement()
mc.right(cube)
mc.invUp(cube)
mc.front(cube)
mc.invLeft(cube)
mc.up(cube)
mc.invDown(cube)
mc.back(cube)
mc.invFront(cube)
mc.left(cube)
mc.down(cube)
mc.invRight(cube)
mc.invBack(cube)
print(cube.getTab())
