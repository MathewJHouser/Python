from itertools import combinations

with open('Day11Input') as f:
    input = f.read()

lines = input.split('\n')
grid = [[ele for ele in line] for line in lines]
m, n = len(grid), len(grid[0])

i = 0
while i < len(grid):
    if '#' not in grid[i]:
        grid.insert(i, ['.']*n)
        m = m+1
        i = i + 2
    else:
        i = i + 1

j = 0
while j < len(grid[0]):
    if '#' not in [grid[i][j] for i in range(m)]:
        for i in range(m):
            grid[i].insert(j, '.')
        n = n + 1
        j = j + 2
    else:
        j = j + 1

galaxy = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
combos = list(combinations(galaxy, 2))

dist = []
for ((a,b), (c,d)) in combos:
    x = abs(a-c)
    y = abs(b-d)
    d = x + y
    dist.append(d)
print(sum(dist))
