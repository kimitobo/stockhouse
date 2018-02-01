# STOCKHOUSE
import pandas
import quandl
import time
import Adafruit_MCP4725 

auth = "SNbqZypqf-CzSt51ZQkL"
dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
dac2 = Adafruit_MCP4725.MCP4725(address=0x61, busnum=1)
df1 = quandl.get("WIKI/AAPL", authtoken=auth)
df2 = quandl.get("WIKI/MSFT", authtoken=auth)

stock1 = df1["Close"]
stock2 = df2["Close"]

dac1_data = stock1.as_matrix()
dac2_data = stock2.as_matrix()

def playStock():
	for x in range(0, dac1_data.size):
		dac1.set_voltage(int(dac1_data[x]))
		dac2.set_voltage(int(dac2_data[x]))
		print (dac1_data[x], dac2_data[x])
		#time.sleep(1)

while True:
	playStock()
