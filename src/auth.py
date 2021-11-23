import RPi.GPIO as gpio
import pimail
from gpio_init import LED, YELLOW, GREEN, TOUCH, BUZZER
import time
import led_sensor as led
import buzzer_sensor as buzzer
from event_class import Event
from db_operations import add_event

def make_notif(notif : Event, auth_succ : bool):
    notif.auth_success(auth_succ)
    notif.create_notification()
    notif.send_notification()
    add_event(notif._date, notif.getAuthInBit())

def authenticate() -> bool:
    '''
    user have 10 seconds to authenticate,  
    then the system sends an email notification
    '''
    print("Authentication process started!")
    
    notification = Event()
    auth_success = False

    # touch sensor waits for finger print input for 10 sec
    signal = gpio.wait_for_edge(TOUCH, gpio.RISING, timeout=10000)
    # if no finger print was given send alert msg
    if signal == None:
        # send email notif if theres no signal
        print("Authentication failed, alert notification sent!")
        make_notif(notification, auth_success)
        return auth_success
    # continue auth process
    else:
        led.off(LED) # red led off
        led.on(YELLOW) # yellow led on
        
        # hold finger onto sensor for 2 seconds
        now = time.time()
        target = now + 2
        while now < target:
            if gpio.input(TOUCH) != gpio.HIGH:
                print("Authentication failed, alert notification sent!")
                led.off(YELLOW)
                make_notif(notification, auth_success)
                return auth_success
            time.sleep(0.5)
            now = time.time()

        # auth success
        auth_success = True
        make_notif(notification, auth_success)
        led.off(YELLOW) # yellow led off
        led.on(GREEN) # green led on
        print("Authentication success, welcome home!")
        print("Auth success msg sent!")
        time.sleep(2)
        led.off(GREEN)
        buzzer.off(BUZZER)
        return auth_success
