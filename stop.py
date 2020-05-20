from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C

mm = MediumMotor(OUTPUT_A)
lmr = LargeMotor(OUTPUT_B)
lml = LargeMotor(OUTPUT_C)

#mm.on_for_seconds(speed=10, seconds=0.2)
lml.on_for_seconds(speed=-10, seconds=0.2)
lmr.on_for_seconds(speed=-10, seconds=0.2)
