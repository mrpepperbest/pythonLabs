import pandas as pd  # TASK 1
df = pd.read_csv("transactions/transactions.csv", index_col=0)
print("================================")
print("TOP 3 biggest really done payments:\n",
      df.loc[df["STATUS"] == "OK"].sort_values(by='SUM', ascending=False)[:3])
print("================================")
print("<Umbrella, Inc> really done payments sum:\n",
      ((df["SUM"][df["STATUS"] == "OK"])[df["CONTRACTOR"] == "Umbrella, Inc"]).sum())

