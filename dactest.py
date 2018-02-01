# Simple demo of setting the output voltage of the MCP4725 DAC.
# Will alternate setting 0V, 1/2VDD, and VDD each second.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the MCP4725 module.
import Adafruit_MCP4725

# Create a DAC instance.
dac = Adafruit_MCP4725.MCP4725()

# Note you can change the I2C address from its default (0x62), and/or the I2C
# bus by passing in these optional parameters:
dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
dac2 = Adafruit_MCP4725.MCP4725(address=0x61, busnum=1)

# Loop forever alternating through different voltage outputs.

def  sineWave():
	for x in range(0, 4096, 1):
		dac1.set_voltage(x)
		dac2.set_voltage(abs(4096-x))

	for x in range(4096, 0, -1):
		dac1.set_voltage(x)
		dac2.set_voltage(abs(4096-x))

def main ():
	sineWave()

while True:
	main()
