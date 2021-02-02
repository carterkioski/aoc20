#PART ONE
f = open('inputs/day2.txt', 'r')
correct = 0
for line in f.readlines():
    line = line.split()
    if line[2].count(line[1].replace(':','')) <= int(line[0].split('-')[1]) and line[2].count(line[1].replace(':','')) >= int(line[0].split('-')[0]):
        correct += 1 
print(correct)
f.close()
print('-------------------------------------------')
#PART TWO
f = open('inputs/day2.txt', 'r')
correct = 0
for line in f.readlines():
    line = line.split()
    if bool(line[2][int(line[0].split('-')[1])-1] == line[1].replace(':','')) ^ bool(line[2][int(line[0].split('-')[0])-1] == line[1].replace(':','')):
    	correct += 1
print(correct)