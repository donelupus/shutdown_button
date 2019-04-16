import RPi.GPIO as GPIO
from subprocess import call

BUTTON_PIN = 18

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

def destroy():
    GPIO.cleanup()

def shutDown(ev=None):
    call("sudo shutdown -h now", shell=True)

if __name__ == '__main__':
    setup()
    try:
        GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=shutDown, bouncetime=200)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()