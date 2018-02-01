import quandl as q
import matplotlib.pyplot as plt

plt.style.use("dark_background")

aapl = q.get("WIKI/AAPL", start_date="2001-1-1", collapse="monthly")
msft = q.get("WIKI/MSFT", start_date="2001-1-1", collapse="monthly")

plt.subplot(1,1,1)
plt.plot(aapl.index, aapl)

plt.xticks(aapl.index[0::3],[])

plt.title("Stocks")

plt.ylabel("Apple")
plt.subplot(1,1,1)
plt.plot(msft.index,msft)

plt.xlabel("year")
plt.ylabel("Microsoft")
plt.show()
