import re

with open('Day18Input', 'r') as f:
    puzzle = f.read()

hex = re.findall(r'(\#\w+)', puzzle)
directions = {'3': (-1, 0), '0': (0, 1), '1': (1, 0), '2': (0, -1)}
x = y = 0
visited = set([(0,0)])

for a in hex:
    d = a[-1]
    hex1 = a[1:-1]
    steps = int(hex1, 16)
    dx, dy = directions[d]
    for i in range(int(steps)):
        x = x + dx
        y = y + dy
        visited.add((x, y))
print('Done')
x, y = min(visited)
next = [(x+1, y+1)]
while next:
    x1, y1 = next.pop()
    for dx, dy in directions.values():
        x2, y2 = x1+dx, y1+dy
        if (x2, y2) not in visited:
            next.append((x2, y2))
            visited.add((x2, y2))
    print(1)
print(len(visited))
