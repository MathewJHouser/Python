class GuardGallivant():
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        self.visited = set()
        self.blocked = []
        for x, line in enumerate(self.grid):
            for y, tile in enumerate(line):
                if tile == "^":
                    self.u = x
                    self.v = y
        try:
            self.directions(self.u, self.v)
            print("Part One =", len(self.visited)+1)
        except IndexError:
            print("Part One =", len(self.visited)+1)

    def directions(self,x,y):
        self.visited.add((x, y))
        tile = self.grid[x][y]
        if tile == "^":
            self.up(x,y)
        if tile == ">":
            self.right(x,y)
        if tile == "v":
            self.down(x,y)
        if tile == "<":
            self.left(x, y)

    def up(self, x, y):
        while 1 <= x <= self.rows:
            if self.grid[x - 1][y] == ".":
                self.visited.add((x, y))
                self.grid[x - 1][y] = "^"
                self.grid[x][y] = "."
                x -= 1
            else:
                break
        if self.grid[x - 1][y] == "#":
            self.grid[x][y] = ">"
            self.directions(x, y)

    def right(self, x, y):
        while 0 <= y <= self.columns-1:
            if self.grid[x][y + 1] == ".":
                self.visited.add((x, y))
                self.grid[x][y + 1] = ">"
                self.grid[x][y] = "."
                y += 1
            else:
                break
        if self.grid[x][y + 1] == "#":
            self.grid[x][y] = "v"
            self.directions(x, y)

    def down(self,x,y):
        while 0 <= x <= self.rows-1:
            if self.grid[x + 1][y] == ".":
                self.visited.add((x, y))
                self.grid[x + 1][y] = "v"
                self.grid[x][y] = "."
                x += 1
            else:
                break
        if self.grid[x + 1][y] == "#":
            self.grid[x][y] = "<"
            self.directions(x, y)

    def left(self,x,y):
        while 1 <= y <= self.columns:
            if self.grid[x][y - 1] == ".":
                self.visited.add((x, y))
                self.grid[x][y - 1] = "<"
                self.grid[x][y] = "."
                y -= 1
            else:
                break
        if self.grid[x][y - 1] == "#":
            self.grid[x][y] = "^"
            self.directions(x, y)


class Part2():
    def __init__(self):
        with open("Input Day 6") as f:
            data = f.read()
        self.grid = [[ele for ele in line if ele != '\n'] for line in data.split()]
        self.loops = set()
        self.gridlock()
        print("Part Two =", len(self.loops))

    def gridlock(self):
        for x, line in enumerate(self.grid):
            for y, tile in enumerate(line):
                copied = [t[:] for t in self.grid]
                copied[x][y] = "#"
                try:
                    GuardGallivant(copied)
                except RecursionError:
                    self.loops.add((x, y))
                except:
                    pass

with open("Input Day 6") as f:
    data = f.read()
grid1 = [[ele for ele in line if ele != '\n'] for line in data.split()]
Day6 = GuardGallivant(grid1)
P2 = Part2()

