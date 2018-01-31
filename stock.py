# STOCKHOUSE
import pandas
import quandl

auth = "SNbqZypqf-CzSt51ZQkL"

df = quandl.get("WIKI/AAPL", authtoken=auth)

close_price_df = df["Close"]
print close_price_df.as_matrix()
