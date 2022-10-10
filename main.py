import machine
import neopixel
import time

# Get potentiometer reading
adc = machine.ADC(26)
# Initialize LEDs
np = neopixel.NeoPixel(machine.Pin(0, machine.Pin.OUT), 30)

while True:

    # Get the potentiometer reading, convert to RGB 0 to 255 
    b = int(2.55 * int(adc.read_u16() / 655.35))

    # Write to the Neopixels
    np.fill((b,b,b))
    np.write()

    # Wait 0.1 seconds and loop
    time.sleep(0.1)