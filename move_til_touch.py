from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B, LargeMotor
from time import sleep

ts = TouchSensor()

tank_pair = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
tank_pair.on(left_speed=10, right_speed=10)

while not ts.is_pressed:
	sleep(0.01)

tank_pair.on_for_seconds(left_speed=-100, right_speed=-100, seconds=0.15, brake=True, block=True)
sleep(5)

