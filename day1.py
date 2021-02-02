import time
#PART ONE
f = open('inputs/day1.txt', 'r')
a = []
for line in f.readlines():
    a.append(int(line.strip()))
a.sort(reverse = True)
for i in a:
    if (2020 - i) in a:
        print(i*(2020-i))
        break
print('-------------------------------------')


#PART TWO
start_time = time.time()
for i, num1 in enumerate(a):
	for j, num2 in enumerate(a[i:]):
		for num3 in a[j:]:
			if num3 + num2 + num1 == 2020:
				print(num1 * num2 * num3)
				break