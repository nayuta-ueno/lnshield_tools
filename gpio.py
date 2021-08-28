import RPi.GPIO as GPIO
import os
import sys

LED1 = 15
LED2 = 13

LED_ON = GPIO.LOW
LED_OFF = GPIO.HIGH

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

led1 = LED_OFF
led2 = LED_OFF
if len(sys.argv) == 3:
    led1 = LED_ON if sys.argv[1] == '1' else LED_OFF
    led2 = LED_ON if sys.argv[2] == '1' else LED_OFF

    if sys.argv[1] != '-':
        GPIO.output(LED1, led1)
    if sys.argv[2] != '-':
        GPIO.output(LED2, led2)
