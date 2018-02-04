# STOCKHOUSE
import pandas
import quandl
import time
import Adafruit_MCP4725
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
dac2 = Adafruit_MCP4725.MCP4725(address=0x61, busnum=1)

auth = "SNbqZypqf-CzSt51ZQkL"
df1 = quandl.get("WIKI/AAPL", authtoken=auth)
df2 = quandl.get("WIKI/MSFT", authtoken=auth)

stock1 = df1["Close"]
stock2 = df2["Close"]

scalar1 = 4096 / stock1.max()
scalar2 = 4096 / stock2.max()

dac1_data = stock1.as_matrix()
dac2_data = stock2.as_matrix()

if dac1_data.size >= dac2_data.size:
	data_range = dac2_data.size
else:
	data_range = dac1_data.size

point = 0
step = 1

while True:
	input_state = GPIO.input(18)
	dac1.set_voltage(int(dac1_data[point]*scalar1))
	dac2.set_voltage(int(dac2_data[point]*scalar2))
	print (dac1_data[x], dac2_data[point])
	#time.sleep(1)

	if input_state == False:
		step =+1
			if step > 10
				step = 1
		print(step)
		time.sleep(0.2)
		
	point = point + step
