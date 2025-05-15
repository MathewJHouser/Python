with open("Day22Input") as f:
    puzzle = f.read()

for brick in puzzle.split():
    start, end = brick.split("~")
    x1, y1, z1 = start.split(",")[]
    x2, y2, z2 = end.split(",")
    print(x1+x2)