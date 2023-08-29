#remote_control.py
from bottle import route,run,template,request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
CONTROL_PIN=13
GPIO.setup(CONTROL_PIN,GPIO.OUT)

@route('/')
def index():
	return template('home.tpl')

@route('/on')
def index():
	GPIO.output(CONTROL_PIN,1)
	return template('home.tpl')

@route('/off')
def index():
	GPIO.output(CONTROL_PIN,0)
	return template('home.tpl')

try:
	run(host='0.0.0.0',port=80)
finally:
	print('Cleaning up GPIO')
	GPIO.cleanup()
