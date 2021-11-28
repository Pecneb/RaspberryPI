from gpio_init import PIR, init, cleanup, LED
import led_sensor as led
import RPi.GPIO as gpio
import alert
import time

gpio.setwarnings(False)

def main():
    # initialize the board
    init()
    
    # begin the watch
    try:
        # start pir sensor, and look out for any motion in room
        # when pir sends signal then start_alert is called
        while True:
            signal = gpio.wait_for_edge(PIR, gpio.RISING, timeout=2000)
            if signal == None:
                led.on(LED)
                time.sleep(1)
                led.off(LED)
                time.sleep(1)
            else:
                alert.start_alert()
    # the program can be shut down with C^
    except KeyboardInterrupt:
        # reset pins
        cleanup()

if __name__ == "__main__":
    main()
