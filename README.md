
## Raspberry PI

### Raspberry PI 4

- Broadcom BCM2711, quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz
- 2GB LPDDR4-3200 SDRAM
- 2.4 GHz and 5.0 GHz IEEE 802.11ac wireless, Bluetooth 5.0, BLE
- 2 USB 3.0 ports; 2 USB 2.0 ports.
- Raspberry Pi standard 40 pin GPIO header (fully backwards compatible with previous boards)
- 2 × micro-HDMI ports (up to 4kp60 supported)
- 2-lane MIPI DSI display port
- 2-lane MIPI CSI camera port
- 4-pole stereo audio and composite video port
- H.265 (4kp60 decode), H264 (1080p60 decode, 1080p30 encode)
- OpenGL ES 3.1, Vulkan 1.0

#### Operacios rendszer

> Raspberry PI OS / Raspbian

## Sensors

- 1x LED
- 1x PIR Motion Detector
- 1x BUZZER
- 1x Touch Sensor
- 1x Web Camera

## Dependencies (Python libraries)

- `RPi.GPIO`
- `smtplib`
- `ssl`

## Main idea

`server.py` module: start the program on command line.  
`raspberrypi_init.py`: server calls this module, and initialize GPIO pins for sensors.  
`led_sensor.py`: main focus for this module, is to make the operation of leds easier.  
`buzzer_sensor.py`: same as `led_sensor.py` just for the buzzer sensor.
`pimail.py`: class for sending email notifications.  
`auth.py`: authenticate user with touch sensor  
`notifcation.py`: send email notification about event detected, alert notification if person did not authenticate him-/herself.  

## Web

**Apache2 Http server configuration**

> sudo apt update && apt upgrade  
> sudo apt install apache2
