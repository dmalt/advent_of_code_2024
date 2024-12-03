from collections import Counter

firsts = []
seconds = Counter()
with open("input1.txt") as f:
    for line in f:
        first, second = line.split()
        firsts.append(int(first))
        seconds[int(second)] += 1
firsts.sort()

sum = 0

for f in firsts:
    if f in seconds:
        sum += f * seconds[f]
print(sum)
