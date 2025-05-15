import re

with open('Day18Input', 'r') as f:
    puzzle = f.read()

directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
x = y = 0
visited = set([(0,0)])

for d, steps in re.findall(r'(\w) (\d+)', puzzle):
    dx, dy = directions[d]

    for i in range(int(steps)):
        x = x + dx
        y = y + dy
        visited.add((x, y))

print(visited)

x, y = min(visited)
next = [(x+1, y+1)]
while next:
    x1, y1 = next.pop()
    for dx, dy in directions.values():
        x2, y2 = x1+dx, y1+dy
        if (x2, y2) not in visited:
            next.append((x2, y2))
            visited.add((x2, y2))

print(len(visited))
