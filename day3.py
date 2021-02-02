#PART ONE
f = open('inputs/day3.txt', 'r')
a =[]
for line in f.readlines():
    a.append(line.strip())
f.close()
def sled(dx,dy):
    x = 0
    y = 0
    trees = 0
    while y < len(a):
        x = x % len(a[x])
        if a[y][x] == '#':
            trees += 1
        x += dx
        y += dy
    return trees
print(sled(3,1))

#PART TWO

print(sled(1,1) * sled(3,1) * sled(5,1) * sled(7,1) * sled(1,2))
