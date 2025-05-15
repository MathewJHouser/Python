import re
with open('Day16Input', 'r') as f:
    puzzle = f.read()

split = puzzle.split('\n')
grid = [list(r) for r in split]
m, n = len(grid), len(grid[0])

starts = ({(x, 0, 'right') for x in range(m)} |
          {(x, n-1, 'left') for x in range(m)} |
          {(0, y, 'down') for y in range(n)} |
          {(m-1, y, 'up') for y in range(n)})

best = 0
for i in starts:
    visited = set()
    energized = set()
    next = set([i])

    while next:
        x, y, direction = next.pop()
        energized.add((x,y))
        tile = grid[x][y]

        if y < n-1 and (x, y+1, 'right') not in visited and (
                (direction == 'right' and tile in '.-') or
                (direction == 'up' and tile in '/-') or
                (direction == 'down' and tile in '\\-')):
            next.add((x, y+1, 'right'))
            visited.add((x, y+1, 'right'))

        if y > 0 and (x, y-1, 'left') not in visited and (
                (direction == 'left' and tile in '.-') or
                (direction == 'up' and tile in '\\-') or
                (direction == 'down' and tile in '/-')):
            next.add((x, y-1, 'left'))
            visited.add((x, y-1, 'left'))

        if x > 0 and (x-1, y, 'up') not in visited and (
                (direction == 'left' and tile in '\\|') or
                (direction == 'right' and tile in '/|') or
                (direction == 'up' and tile in '.|')):
            next.add((x-1, y, 'up'))
            visited.add((x-1, y, 'up'))

        if x < m-1 and (x+1, y, 'down') not in visited and (
                (direction == 'left' and tile in '/|') or
                (direction == 'right' and tile in '\\|') or
                (direction == 'down' and tile in '.|')):
            next.add((x+1, y, 'down'))
            visited.add((x+1, y, 'down'))

    total = (len(energized))
    best = max(best, total)

print(best)