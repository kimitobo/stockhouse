# STOCKHOUSE
import pandas
import quandl
import time
import Adafruit_MCP4725

auth = "SNbqZypqf-CzSt51ZQkL"
dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
dac2 = Adafruit_MCP4725.MCP4725(address=0x61, busnum=1)
df1 = quandl.get("WIKI/AAPL", authtoken=auth)
df2 = quandl.get("WIKI/AAPL", authtoken=auth)

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

def playStock():
	for x in range(0, data_range):
		dac1.set_voltage(int(dac1_data[x]*scalar1))
		dac2.set_voltage(int(dac2_data[x]*scalar2))
		print (dac1_data[x], dac2_data[x])
		time.sleep(0.1)

while True:
	playStock()
