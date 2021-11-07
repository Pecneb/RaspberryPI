import RPi.GPIO as gpio

LED = 8
PIR = 10
BUZZER = 12
TOUCH = 11
YELLOW = 15
GREEN = 13

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
