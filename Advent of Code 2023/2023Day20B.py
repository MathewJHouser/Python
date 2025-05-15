from collections import deque
from itertools import count
import math

with open('Day20Input') as f:
    puzzle = f.read()
modules = puzzle.split('\n')

graph = {}
flip_flop = {}
memory = {}
for module in modules:
    type, destination = module.split(' -> ')
    name = type.lstrip('%&')
    destinations = destination.split(', ')
    graph[name] = destinations
    if type[0] == '%':
        flip_flop[name] = 0
    elif type[0] == '&':
        memory[name] = {}

for conjunction in memory.keys():
    for name, destinations in graph.items():
        if conjunction in destinations:
            memory[conjunction][name] = 0



pulses = [0, 0]
for i in range(1000):
    pulses[0] = pulses[0] + 1
    queue = deque([('broadcaster', dest, 0) for dest in graph['broadcaster']])
    while queue:
        source, dest, pulse = queue.popleft()
        pulses[pulse] = pulses[pulse] + 1

        if dest in flip_flop and pulse == 0:
            flip_flop[dest] = 1 - flip_flop[dest]
            signal = flip_flop[dest]

        elif dest in memory:
            memory[dest][source] = pulse
            signal = 1 if 0 in memory[dest].values() else 0

        else:
            continue

        queue.extend([(dest, nxt, signal) for nxt in graph[dest]])

ans = pulses[0] * pulses[1]
print(ans)


