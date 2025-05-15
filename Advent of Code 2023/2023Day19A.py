import re
import operator

with open('Day19Input') as f:
    puzzle = f.read()

workflows, parts = puzzle.split('\n\n')
flow = {}
for name, rules in re.findall(r'(\w+)\{([^}]+)\}', workflows):
    conditions = re.findall(r'(\w)(<|>)(\d+):(\w+)', rules)
    final = rules.split(',')[-1]
    flow[name] = conditions + [final]
print(flow)

comp = {'>': operator.gt, '<': operator.lt}
total = 0
for part in re.findall(r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)', parts):
    print(part)
    part = dict(zip('xmas', map(int, part)))
    print(part)
    current = 'in'
    while current not in ('A', 'R'):
        for cat, op, amt, res in flow[current][:-1]:
            if comp[op](part[cat], int(amt)):
                current = res
                break
        else:
            current = flow[current][-1]
    if current == 'A':
        total = total + sum(part.values())
print(total)