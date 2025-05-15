from collections import defaultdict
import re

with open('Day15Input') as f:
    input = f.read()

labels = defaultdict(list)
lenses = defaultdict(list)
regex = r'(\w+)(=|-)(\d+)?'

for label, op, lense in re.findall(regex, input):
    s = 0
    for c in label:
        a = ord(c)
        s = s + a
        s = s * 17
        s = s % 256

    if label in labels[s]:
        i = labels[s].index(label)

        if op == '-':
            labels[s].pop(i)
            lenses[s].pop(i)

        if op == '=':
            lenses[s][i] = int(lense)

    elif op == '=':
        labels[s].append(label)
        lenses[s].append(int(lense))

total = []
for box, lenses in lenses.items():
    for i, lense in enumerate(lenses, start=1):
        w = box + 1
        power = w * i * lense
        total.append(power)

ans = sum(total)
print(ans)
