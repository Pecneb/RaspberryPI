from gpio_init import LED, BUZZER
import led_sensor as led
import buzzer_sensor as buzzer
from auth import authenticate


def start_alert():
    '''
    Starts alert, switches on led and buzzer.
    '''
    print("Motion detected!")
    led.on(LED)
    buzzer.on(BUZZER)
    # event object should be created here
    return authenticate()
    
