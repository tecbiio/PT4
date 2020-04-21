import MovementRobot
import maestro

servo = maestro.Controller()
mr = MovementRobot.Movement()
mr.right(servo)
servo.close()