from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, MoveTank
from time import sleep

ts = TouchSensor()
cs = ColorSensor()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)

#while not cs.color_name == 'White':
#	tank_pair.on(left_speed=20, right_speed=20)
#	sleep(0.01)

i = 0
while cs.color_name != 'White':
	tank_pair.on(left_speed=10, right_speed=10)
	if ts.is_pressed:
		break
	sleep(0.01)
tank_pair.off()
sleep(2)
