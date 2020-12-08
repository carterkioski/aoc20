import re
f = open('inputs/day4.txt','r')
req = r'(byr)|(iyr)|(eyr)|(hgt)|(hcl)|(ecl)|(pid)'
valid = 0
hcl = r'#[0-9a-f]{6}'
ecl = r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)'
pid = r'\d{9}'
a = ''
for line in f.readlines():
    if not line.strip():
        x = re.findall(req, a)
        if len(set(x)) == 7:
            x2 = re.split(req,a)
            P = ''.join(i for i in x2 if i != None)
            P = P.split()
            isValid = True
            for i in P:
                i = i.split(':')
                if i[0] == 'byr':
                    if int(i[1]) < 1920 or int(i[1]) > 2002:
                        isValid = False
                if i[0] == 'iyr':
                    if int(i[1]) < 2010 or int(i[1]) > 2020:
                        isValid = False
                if i[0] == 'eyr':
                    if int(i[1]) < 2020 or int(i[1]) > 2030:
                        isValid = False
                if i[0] == 'hgt':
                    if 'cm' in i[1]:
                        h = int(i[1].replace('cm', ''))
                        if h < 150 or h > 193:
                            isValid = False
                    elif 'in' in i[1]:
                        h = int(i[1].replace('in', ''))
                        if h < 59 or h > 76:
                            isValid = False
                    else:
                        isValid = False
                if i[0] == 'hcl':
                    if not bool(re.fullmatch(hcl, i[1])):
                        isValid = False
                if i[0] == 'ecl':
                    if not bool(re.fullmatch(ecl, i[1])):
                        isValid = False
                if i[0] == 'pid':
                    if not bool(re.fullmatch(pid, i[1])):
                        isValid = False
            valid += isValid
        a = ''
    else:
    	a += line.strip() + ' '

print(valid)
