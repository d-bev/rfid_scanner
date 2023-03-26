import time

import RPi.GPIO as GPIO

CHANNEL = 19

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CHANNEL, GPIO.OUT)
    
    GPIO.output(CHANNEL, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(CHANNEL, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(CHANNEL, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(CHANNEL, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(CHANNEL, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(CHANNEL, GPIO.LOW)
    time.sleep(5)
finally:
    GPIO.cleanup()
