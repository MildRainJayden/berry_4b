import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(0)
try:
	while 1:
		for dc in range(0,101,20):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100,-1,-20):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardInterrupt:
	pass
p.stop()
GPIO.cleanup()

