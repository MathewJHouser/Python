import re
import operator
import math

with open('Day19Input') as f:
    puzzle = f.read()

workflows, parts = puzzle.split('\n\n')
flow = {}
for name, rules in re.findall(r'(\w+)\{([^}]+)\}', workflows):
    conditional = []
    for cat, op, amt, res in re.findall(r'(\w)(<|>)(\d+):(\w+)', rules):
        conditional.append(('xmas'.index(cat), op, int(amt), res))
    final = rules.split(',')[-1]
    flow[name] = conditional + [final]

start = ('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))
queue = [start]
total_accepted = 0
while queue:
    curr, *intervals = queue.pop()
    if curr in ('A', 'R'):
        if curr == 'A':
            g = 1
            for lo, hi in intervals:
                h = hi-lo+1
                g = g * h
            total_accepted = total_accepted + g
        continue

    for cat_idx, op, amt, res in flow[curr][:-1]:
        lo, hi = intervals[cat_idx]

        # All passthrough, no transfer
        if (op == '>' and amt >= hi) or (op == '<' and amt <= lo):
            continue

        # All transfer no passthrough
        if (op == '>' and amt < lo) or (op == '<' and amt > hi):
            queue.append((res, *intervals))
            break

        # Some of both
        if op == '>':
            transfer = (amt + 1, hi)
            passthrough = (lo, amt)
        else:
            transfer = (lo, amt - 1)
            passthrough = (amt, hi)
        intervals[cat_idx] = passthrough
        intervals2 = intervals.copy()
        intervals2[cat_idx] = transfer
        queue.append((res, *intervals2))

    else:  # Remaining is transferred
        queue.append((flow[curr][-1], *intervals))
print(total_accepted)

