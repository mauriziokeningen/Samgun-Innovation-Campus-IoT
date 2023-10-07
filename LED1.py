from gpiozero import LED, Button

# Declare the 3 LEDs on GPIO pins 17, 27 and 22: 
green_led = LED(17)
amber_led = LED(27)
red_led = LED(22)

# Declare the button on GPIO pin 4
button = Button(4)

# Start the program with the green LED turned on
green_led.on()

def changeLED():
    # Check which LED is currently active, turn it off, and turn on the next LED
    if green_led.is_active:
        green_led.off()
        amber_led.on()
    elif amber_led.is_active:
        amber_led.off()
        red_led.on()
    elif red_led.is_active:
        red_led.off()
        green_led.on()

if __name__ == "__main__":
    # Wait for the button to be pressed to change the LED
    while True:
        button.when_pressed = changeLED
