import RPi.GPIO as gpio
from time import sleep

def on(channel):
    gpio.output(channel, gpio.HIGH)

def off(channel):
    gpio.output(channel, gpio.LOW)

