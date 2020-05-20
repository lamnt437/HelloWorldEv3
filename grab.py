import socketio
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveTank, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from time import sleep
from queue import Queue

ts = TouchSensor()
cs = ColorSensor()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
left_motor = LargeMotor(OUTPUT_C)
right_motor = LargeMotor(OUTPUT_B)
forklift = MediumMotor(OUTPUT_A)
    
def grab():
    print("Grab")
    forklift.on_for_degrees(speed=10, degrees=-90)

grab()

def ungrab():
    forklift.on_for_degrees(speed=-10, degrees=0)
