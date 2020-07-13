import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import csv

rehash = []
count = []
percent_count = [] # % of buckets rehashed to specific count
cumulative = [] # number of buckets rehashed at each round
percent_cumu = [] # % of buckets rehashed at round

with open('../csv/main_rehash.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        rehash.append(int(row['rehashes per bucket']))
        count.append(int(row[' count']))

print(rehash)
# rehash.pop(0)
# count.pop(0)
print(count)
print(sum(count))

for i in range(0, len(count)):
    c_sum = 0
    percent_count.append(count[i] * 100 / sum(count))
    if i == 0:
        continue
    for j in range(i, len(count)):
        c_sum += count[j]
    percent_cumu.append(c_sum * 100 / sum(count))
    cumulative.append(c_sum)

print(percent_count)
print(cumulative)
percent_cumu.insert(0, 0)
print(percent_cumu)

# fig = plt.figure()
fig, ax = plt.subplots()
# rehash.pop(0)
plt.bar(rehash, percent_cumu, color='y')
plt.bar(rehash, percent_count)
plt.plot(loc = "upper right")
plt.xlabel("Rehash Count")
plt.ylabel("Frequency out of Total Buckets")

# xlocs, xlabs = plt.xticks()
ax.yaxis.set_major_formatter(mtick.PercentFormatter())


plt.grid(True)
plt.show()
fig.savefig("../figures/main_rehash.png")

exit()
