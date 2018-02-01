# STOCKHOUSE
import pandas
import quandl
import time
import Adafruit_MCP4725 

auth = "SNbqZypqf-CzSt51ZQkL"
dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
dac2 = Adafruit_MCP4725.MCP4725(address=0x61, busnum=1)
df = quandl.get("WIKI/AAPL", authtoken=auth)

close_price_df = df["Close"]
dac_data = close_price_df.as_matrix()

for x in range(0, dac_data.size):
    dac1.set_voltage(dac_data[x])
