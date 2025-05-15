import re
from functools import cmp_to_key
from collections import Counter

with open("Day7Input") as f:
    input = f.read()
#print(input)

lines = input.split('\n')
#print(lines)

def type(x):
    jokers = x.count('J')
    x = [c for c in x if c != 'J']
    C = sorted(Counter(x).values(), reverse=True)
    if not C:
        C = [0]
    if C[0] + jokers == 5:
        return 6
    elif C[0] + jokers == 4:
        return 5
    elif C[0] + jokers == 3 and C[1] == 2:
        return 4
    elif C[0] + jokers == 3 and C[1] == 1:
        return 3
    elif C[0] == 2 and (jokers or C[1] == 2):
        return 2
    elif (C[0] == 2 or jokers == 1) and C[1] == 1:
        return 1
    else:
        return 0

cards = 'J23456789TQKA'

def compare(a, b):
    typea = type(a[0])
    typeb = type(b[0])
    if typea > typeb:
        return 1
    if typea < typeb:
        return -1
    for carda, cardb in zip(a[0], b[0]):
        if carda == cardb:
            continue
        a_wins = (cards.index(carda) > cards.index(cardb))
        return 1 if a_wins else -1

hands = re.findall(r'(\w{5}) (\d+)', input)
print(hands)
hands.sort(key=cmp_to_key(compare))
print(hands)

total = 0
for rank, (_, bid) in enumerate(hands):
    total = total + (rank + 1) * int(bid)
print(total)

