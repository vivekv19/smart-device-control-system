from motor import Motor
from light import Light
from controller import Controller

motor = Motor()
light = Light()

motor_controller = Controller()
light_controller = Controller()

motor_controller.operate(motor)
light_controller.operate(light)
