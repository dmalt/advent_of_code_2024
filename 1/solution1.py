firsts = []
seconds = []
with open("input1.txt") as f:
    for line in f:
        first, second = line.split()
        firsts.append(int(first))
        seconds.append(int(second))
firsts.sort()
seconds.sort()

sum = 0
for f, s in zip(firsts, seconds):
    d = abs(f - s)
    print(f"{sum=}, {f=}. {s=}, {d=}") 
    sum += d


print(sum)
