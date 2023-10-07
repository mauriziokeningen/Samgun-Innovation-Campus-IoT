from gpiozero import LED

# Declare the 3 LEDs on GPIO pins 17, 27 and 22: 
green_led = LED(17)
amber_led = LED(27)
red_led = LED(22)

def traffic_light(instruction):
    # Turn off all the LEDs
    green_led.off()
    amber_led.off()
    red_led.off()

    # Receive the instruction and turn on the corresponding LED
    if instruction == 'go':
        green_led.on()
    elif instruction == 'slow':
        amber_led.on()
    elif instruction == 'stop':
        red_led.on()
    else:
        print('Invalid option, please use only "go", "slow", or "stop".')

if __name__ == "__main__":
    # Receive the instruction from the terminal and call the traffic_light function indefinitely
    while True:
        instruction = input("Enter the traffic light instruction: 'go', 'slow', or 'stop'")
        traffic_light(instruction)
