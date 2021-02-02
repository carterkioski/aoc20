#PART ONE
f = open('inputs/day6.txt', 'r')
group = set()
sum = 0
for line in f.readlines():
    line = line.strip()
    if not line:
        sum += len(group)
        group = set()
    else:
        for i in line:
            group.add(i)
print(sum)