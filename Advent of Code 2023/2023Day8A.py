import re
from itertools import cycle

with open('Day8Input') as f:
    input = f.read()

directions, data = input.split('\n\n')
directions = cycle(0 if d == 'L' else 1 for d in directions)
graph = {}

for node, left, right in re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', data):
    graph[node] = [left, right]

node = 'AAA'
for steps, d in enumerate(directions, start=1):
    node = graph[node][d]
    if node == 'ZZZ':
        break

print(steps)