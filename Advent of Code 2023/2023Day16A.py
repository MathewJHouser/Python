import re
with open('Day16Input', 'r') as f:
    puzzle = f.read()

split = puzzle.split('\n')
grid = [list(r) for r in split]
m, n = len(grid), len(grid[0])

visited = set()
energized = set()
next = set([(0, 0, 'right')])

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

print(len(energized))