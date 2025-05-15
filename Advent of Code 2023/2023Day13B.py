with open('Day13Input') as f:
    input = f.read()

grids = input.strip().split('\n\n')
#print(grids)
z = []
for i, grid in enumerate(grids, start=1):
    #print("Grid #" + str(i))
    block = grid.splitlines()
    #print(block)

    for j, r in enumerate(range(1, len(block))):
        #print("#" + str(j+1))
        above = block[:r][::-1]
        below = block[r:]
        s = 0
        for x, y in zip(above, below):
            s = s + sum(0 if a == b else 1 for a, b in zip(x, y))
        #print(s)

        if s == 1:
            z.append(r * 100)

    block = list(zip(*block))
    print(block)
    for j, r in enumerate(range(1, len(block))):
        #print("#" + str(j+1))
        above = block[:r][::-1]
        below = block[r:]
        s = 0
        for x, y in zip(above, below):
            s = s + sum(0 if a == b else 1 for a, b in zip(x, y))
        #print(s)

        if s == 1:
            z.append(r)
#print(z)

ans = sum(z)
print(ans)