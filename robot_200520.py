import socketio
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveTank, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from time import sleep
from queue import Queue

sio = socketio.Client()

host = 'http://192.168.0.21:5000'

ts = TouchSensor()
cs = ColorSensor()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
left_motor = LargeMotor(OUTPUT_C)
right_motor = LargeMotor(OUTPUT_B)

@sio.on('hello')
def hello():
    print("Hello")

@sio.on('up')
def go_straight():
    tank_pair.on_for_seconds(left_speed=10, right_speed=10, seconds=1)

@sio.on('/left')
def turn_left():
    print("left")
    right_motor.on_for_seconds(speed = 10, seconds=1)

@sio.on('/right')
def turn_right():
    left_motor.on_for_seconds(speed=10, seconds=1)

@sio.on('/down')
def go_back():
    tank_pair.on_for_seconds(left_speed=-10, right_speed=-10, seconds=1)

@sio.on('connect')
def connect():
        print('Connected')

if __name__ == '__main__':
        sio.connect(host)
        sio.wait()
