# Detect Bird Presence
import RPi.GPIO as GPIO
import time

class BirdDetector():
    
    def __init__(self):
        # Define PIR input and LED output GPIO pins
        self.PIR = 11
        self.LED = 3
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIR, GPIO.IN)         #Read output from PIR motion sensor
        GPIO.setup(self.LED, GPIO.OUT)         #LED output pin

    def set_led(self, on=True):
        """Set led to on or off"""
        if on:
            GPIO.output(self.LED, GPIO.HIGH)
        else:
            GPIO.output(self.LED, GPIO.LOW)

    def detect(self):
        c=GPIO.input(self.PIR)
        if c==0:
            #print("No bird")
            self.set_led(on=False)
        elif c==1:
            #print("Yes bird")
            self.set_led(on=True)
        return c
    
    def led_state(self):
        return GPIO.input(self.LED)
    
    def PIR_state(self):
        return GPIO.input(self.PIR)

if __name__ == 'main':
    watchdog = BirdDetector()
    while True:     
        i = watchdog.detect()
        print(i, watchdog.led_state())
        time.sleep(0.5)
