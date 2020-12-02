import pandas as pd  # TASK 3
from matplotlib import pyplot as plt
df1 = pd.read_excel("students/students_info.xlsx", sheet_name="logins")
df2 = pd.read_html("students/results_ejudge.html")
df3 = pd.merge(df1, df2[0], left_on="login", right_on="User")

faculty = df3.groupby("group_faculty").mean()
out = df3.groupby("group_out").mean()

fig, axs = plt.subplots(1, 2)
faculty["Solved"].plot(ax=axs[0], title="Average by faculty groups", kind='bar')
out["Solved"].plot(ax=axs[1], title="Average by IT groups", kind='bar')
plt.setp(axs, ylim=(0, 8))
plt.show()

print("================================")
print("Geniuses - guys, who got > 10 points in problem G or in problem H, so:")
print("Geniuses :\n",
      df3[(df3["H"] > 10) | (df3["G"] > 10)])

