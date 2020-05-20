import socketio
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveTank
from ev3dev2.sensor.lego import TouchSensor
from time import sleep

sio = socketio.Client()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
ts = TouchSensor()
left_motor = LargeMotor(OUTPUT_C)
right_motor = LargeMotor(OUTPUT_B)
fork = MediumMotor(OUTPUT_A)

#host = 'https://robot-warehouse-server.herokuapp.com/'
host = 'http://192.168.43.58:5000'

@sio.on('connect')
def connect():
        print('Connected')

@sio.on('run')
def run():
	print("Running...")
	tank_pair.on(left_speed=10, right_speed=10)
	while not ts.is_pressed:
		sleep(0.01)
	tank_pair.on_for_seconds(left_speed=-40, right_speed=-40, seconds=0.15, brake=True, block=True)

@sio.on('left')
def turn_left():
    right_motor.on_for_seconds(speed = 10, seconds=1)

@sio.on('right')
def turn_right():
    left_motor.on_for_seconds(speed=10, seconds=1)

@sio.on('down')
def go_back():
    tank_pair.on_for_seconds(left_speed=-10, right_speed=-10,seconds=1)


@sio.on('up')
def go_straight():
    tank_pair.on_for_seconds(left_speed=10, right_speed=10, seconds=1)

@sio.on('pickup')
def grab(fork):
    fork.on_for_degrees(speed=10, degree=90)

@sio.on('drop')
def ungrab(fork):
    fork.on_for_degrees(speed=10, degree=-90)

if __name__ == '__main__':
	sio.connect(host)
	sio.wait()
