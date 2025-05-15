import re

with open("Day3Input") as f:
    input = f.read()
#print(input)

lines = input.split('\n')
#print(lines)
symbol_regex = r'[^.\d]'
symbol_adjacent = set()

part_num = 0

for i, line in enumerate(lines):
    mi = re.finditer(r'[^.\d]', line)
    for m in mi:
        j = m.start()
        symbol_adjacent |= {(r, c) for r in range(i - 1, i + 2) for c in range(j - 1, j + 2)}
        #print(i, symbol_adjacent)
for i, line in enumerate(lines):
    ni = re.finditer(r'\d+', line)
    for n in ni:
        if any ((i,j) in symbol_adjacent for j in range(*n.span())):
            part_num = part_num + int(n.group())
            print(part_num)
