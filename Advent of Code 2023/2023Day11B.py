from itertools import combinations

with open('Day11Input') as f:
    input = f.read()

lines = input.split('\n')
grid = [[ele for ele in line] for line in lines]
m, n = len(grid), len(grid[0])

emptyrows = [i for i in range(m) if '#' not in grid[i]]
emptycolumns = [j for j in range(n) if '#' not in [grid[i][j] for i in range(m)]]
galaxy = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
combos = list(combinations(galaxy, 2))

dist = []
for ((a, b), (c, d)) in combos:
    x1, x2 = sorted((a, c))
    y1, y2 = sorted((b, d))
    ar = 999999 * sum([r in range(x1,x2) for r in emptyrows])
    ac = 999999 * sum([r in range(y1, y2) for r in emptycolumns])
    x = abs(a-c)
    y = abs(b-d)
    d = x + y + ar + ac
    dist.append(d)
print(sum(dist))
