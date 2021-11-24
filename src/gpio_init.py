import RPi.GPIO as gpio

"""
Here we can set up the gpio pins of the RaspberryPI.
The global variables below can be changed.
"""
LED = 8
GREEN = 10 # 13
YELLOW = 11 # 15
PIR = 12 # 10
BUZZER = 13 # 12
TOUCH = 15 # 11

def init():
    print("Initialize board...")
    # set up the board
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    
    gpio.setup(LED, gpio.OUT)
    gpio.setup(YELLOW, gpio.OUT)
    gpio.setup(GREEN, gpio.OUT)
    gpio.setup(PIR, gpio.IN)
    gpio.setup(BUZZER, gpio.OUT)
    gpio.setup(TOUCH, gpio.IN)
    print("Initialized!")

def cleanup():
    # reset board pins
    print("Exiting...")
    gpio.cleanup()
    print("Exited successfully")
