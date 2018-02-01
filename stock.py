y
# STOCKHOUSE
import pandas
import quandl
import time

import Adafruit_MCP4725 


dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
auth = "SNbqZypqf-CzSt51ZQkL"

df = quandl.get("WIKI/AAPL", authtoken=auth)

close_price_df = df["Close"]
print close_price_df.as_matrix()
