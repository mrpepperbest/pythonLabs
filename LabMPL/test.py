import matplotlib.pyplot as plt  # TASK 3
import numpy as np
f = open("test/students.csv")
groups = []
preps = []
marks1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
marks2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
b = []
a = f.read().split("\n")
for _ in range(1, len(a)):
    b.append(a[_].split(";"))

prep = [(b[_][0], int(b[_][2])) for _ in range(len(b))]
group = [(b[_][1], int(b[_][2])) for _ in range(len(b))]

preps = [list(dict.fromkeys((b[_][0]) for _ in range(len(b))))]
groups = [list(dict.fromkeys((b[_][1]) for _ in range(len(b))))]

prep = [(prep[i], prep.count(prep[i])) for i in range(len(prep))]
group = [(group[i], group.count(group[i])) for i in range(len(group))]
prep = sorted(sorted(list(dict.fromkeys(prep)), key=lambda e: e[0][0]), key=lambda e: e[1], reverse=True)
group = sorted(sorted(list(dict.fromkeys(group)), key=lambda e: e[0][0]), key=lambda e: e[1], reverse=True)

for i in range(len(prep)):
    for j in range(len(preps[0])):
        if prep[i][0][0] == preps[0][j]:
            marks1[j][prep[i][0][1]-1] = prep[i][1]

for i in range(len(group)):
    for j in range(len(groups[0])):
        if group[i][0][0] == groups[0][j]:
            marks2[j][group[i][0][1]-1] = group[i][1]

fig, axs = plt.subplots(2, 1)
axs[0].bar(preps[0], [marks1[i][0] for i in range(7)], 0.4, label="1")
for _ in range(1, 10):
    for i in range(7):
        marks1[i][_] += marks1[i][_-1]
    axs[0].bar(preps[0], [marks1[i][_]-marks1[i][_-1] for i in range(7)], bottom=[marks1[i][_-1] for i in range(7)], label=str(_+1))
axs[0].set_ylabel("Marks")
axs[0].set_title("Marks per preps")
axs[0].legend(loc='right')

axs[1].bar(groups[0], [marks2[i][0] for i in range(6)], 0.4, label="1")
for _ in range(1, 10):
    for i in range(6):
        marks2[i][_] += marks2[i][_-1]
    axs[1].bar(groups[0], [marks2[i][_]-marks2[i][_-1] for i in range(6)], bottom=[marks2[i][_-1] for i in range(6)], label=str(_+1))
axs[1].set_ylabel("Marks")
axs[1].set_title("Marks per group")
axs[1].legend(loc='right')
plt.show()
