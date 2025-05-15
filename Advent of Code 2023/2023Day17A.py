from heapq import heappop, heappush

with open('Day17Input', 'r') as f:
    puzzle = f.read()
split = puzzle.split('\n')

grid = [[int(d) for d in line] for line in split]
m, n = len(grid), len(grid[0])
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

# tuple: (heat-loss, x-coord, y-coord, length-of-run, x-direction, y-direction)
q = [(0, 0, 0, 0, 0, 0)]
visited = set()
while q:
    loss, x, y, k, dx, dy = heappop(q)

    if x == m-1 and y == n-1:
        break

    if any((x, y, j, dx, dy) in visited for j in range(1, k + 1)):
        continue

    visited.add((x, y, k, dx, dy))
    for new_dx, new_dy in directions:
        straight = (new_dx == dx and new_dy == dy)
        new_x, new_y = x + new_dx, y + new_dy

        if any((new_dx == -dx and new_dy == -dy,
                k == 3 and straight,
                new_x < 0, new_y < 0,
                new_x == m, new_y == n)):
            continue

        new_k = k + 1 if straight else 1
        heappush(q, (loss + grid[new_x][new_y], new_x, new_y, new_k, new_dx, new_dy))

print(loss)