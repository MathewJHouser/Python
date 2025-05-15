import re

with open("Day3Input") as f:
    input = f.read()
#print(input)

lines = input.split('\n')
#print(lines)
symbol_regex = r'[^.\d]'
symbol_adjacent = set()

part_num = 0
gear_regex = r'\*'
gears = dict()

for i, line in enumerate(lines):
    mi = re.finditer(r'\*', line)
    for m in mi:
        gears[(i, m.start())] = []
        #print(gears)
for i, line in enumerate(lines):
    ni = re.finditer(r'\d+', line)
    for n in ni:
        for r in range(i-1, i+2):
            for c in range(n.start()-1, n.end()+1):
                if (r,c) in gears:
                    gears[(r,c)].append(int(n.group()))
print(gears)

sum = 0
for num in gears.values():
    if len(num) == 2:
        sum += num[0] * num[1]
print(sum)