from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_A
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from time import sleep
from queue import Queue


queue = Queue()
queue.put('left')
queue.put('right')
queue.put('straight')
queue.put('back')

while not queue.empty():
	print(queue.get())
