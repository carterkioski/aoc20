#PART ONE
f = open('inputs/day5.txt', 'r')
high_id = (0, 0, 0)
ids = set()
for line in f.readlines():
    row = line[0:7]
    row = row.replace('F','0')
    row = row.replace('B','1')
    row = int(row,2)
    col = line[7:]
    col = col.replace('L','0')
    col = col.replace('R','1')
    col = int(col,2)
    s_id = 8 * row + col
    seat = row, col
    ids.add(s_id)
    if s_id > high_id[0]:
    	high_id = (s_id, row, col)
#PART TWO
print(set(range(high_id[0])) - ids)
