from gpio_init import PIR, init, cleanup, LED, TOUCH
import led_sensor as led
import RPi.GPIO as gpio
import alert
import time

gpio.setwarnings(False)

def main():
    # initialize the board
    init()
    switch = True 
    # begin the watch
    try:
        # start pir sensor, and look out for any motion in room
        # when pir sends signal then start_alert is called
        while True:
            if switch:
                print("Switch: ON")
                signal = gpio.wait_for_edge(PIR, gpio.RISING, timeout=4000)
                if signal == None:
                    led.on(LED)
                    time.sleep(1)
                    led.off(LED)
                    time.sleep(1)
                else:
                    auth = alert.start_alert()
                    if auth:
                        switch = False
                        print("Switch OFF")
                    else:
                        continue
            else:
                switch_signal = gpio.wait_for_edge(TOUCH, gpio.RISING)
                if signal == None:
                    switch = False
                else:
                    switch = True
                    time.sleep(5)

    # the program can be shut down with C^
    except KeyboardInterrupt:
        # reset pins
        cleanup()

if __name__ == "__main__":
    main()
