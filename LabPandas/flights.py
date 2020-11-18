import pandas as pd  # TASK 2
from matplotlib import pyplot as plt

df = pd.read_csv("flights/flights.csv", index_col=0)

amount = pd.DataFrame({"COUNT": df.groupby(["CARGO"]).size()})
summary = df.groupby("CARGO").sum()

df2 = pd.merge(summary, amount, on="CARGO")

fig, axs = plt.subplots(1, 3)
df2["COUNT"].plot(ax=axs[0], title="Number of flights", kind='bar')
df2["WEIGHT"].plot(ax=axs[1], title="Total weight", kind='bar')
df2["PRICE"].plot(ax=axs[2], title="Total price", kind='bar')
plt.show()
