import matplotlib.pyplot as plt  # TASK 1
print("Insert test name (001-005):")
f = open("dead_moroz/"+input()+".dat")
x = []
y = []
a = f.read().split("\n")
for _ in range(1, int(a[0])+1):
    x.append(float(a[_].split()[0]))
    y.append(float(a[_].split()[1]))
fig, axs = plt.subplots()
axs.scatter(x, y, 1+50/len(x), "black", marker="o")
axs.set_title("Number of points: " + str(len(x)))
axs.set_box_aspect((max(y)-min(y))/(max(x)-min(x)))

plt.show()
