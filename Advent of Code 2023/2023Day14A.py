with open('Day14Input') as f:
    input = f.read()

grid = [list(row) for row in input.split('\n')]
print(grid)
m = len(grid)
n = len(grid[0])

#North Cycle
for c in range(n):
    limit = 0
    for r in range(m):
        if grid[r][c] == '#':
            limit = r + 1
        elif grid[r][c] == "O":
            if r > limit:
                grid[limit][c] = 'O'
                grid[r][c] = '.'
            limit = limit + 1
print(grid)

load = []
for c in range(n):
    for r in range(m):
        if grid[r][c] == 'O':
            l = n - r
            load.append(l)
ans = sum(load)
print(ans)