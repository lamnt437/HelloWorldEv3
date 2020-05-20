from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveTank, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.sound import Sound
from time import sleep
from queue import Queue

sio = socketio.Client()

host = 'http://192.168.0.21:5000'

ts = TouchSensor()
cs = ColorSensor()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
left_motor = LargeMotor(OUTPUT_C)
right_motor = LargeMotor(OUTPUT_B)
forklift = MediumMotor(OUTPUT_A)

sound = Sound()
str_connected_en = "Connected"

# variables
is_grabbed = False

@sio.on('go_forward')
def go_forward():
    tank_pair.on_for_seconds(left_speed=10, right_speed=10, seconds=1)

@sio.on('turn_left')
def turn_left():
    right_motor.on_for_seconds(speed = 10, seconds=1)

@sio.on('turn_right')
def turn_right():
    left_motor.on_for_seconds(speed=10, seconds=1)
    
@sio.on('grab')
def grab():
    global is_grabbed
    if not is_grabbed:
        print("Grab")
        forklift.on_for_degrees(speed=10, degrees=-120)
        is_grabbed = True
    else:
        print("Already grabbed!")

@sio.on('ungrab')
def ungrab():
    global is_grabbed
    if is_grabbed:
        print("Ungrab")
        forklift.on_for_degrees(speed=10, degrees=120)
        is_grabbed = False
    else:
        print("Not grab yet!")


@sio.on('go_backward')
def go_backward():
    tank_pair.on_for_seconds(left_speed=-10, right_speed=-10, seconds=1)

@sio.on('fork_up')
def fork_up():
    forklift.on_for_degrees(speed=10, degrees=-10)

@sio.on('fork_down')
def fork_down():
    forklift.on_for_degrees(speed=10, degrees=10)

@sio.on('connect')
def connect():
        print('Connected')
        sound.speak(str_connected_en)

if __name__ == '__main__':
        sio.connect(host)
        sio.wait()
