def sudoku():
    grid = []
    for i in range(9):
        text = input("Enter Row "+str(i + 1) + ": ")
        if not text.isdigit():
            return "No."
        if len(text) != 9:
            return "No."
        if "0" in text:
            return "No."
        for n in "123456789":
            if text.count(n) != 1:
                return "No."
        lis = list(text)
        grid.append(lis)
    for i in range(9):
        col = ""
        for j in range(9):
            col += grid[i][j]
        for n in "123456789":
            if col.count(n) != 1:
                return "No."
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            tile = ""
            for m in range(3):
                for n in range(3):
                    tile += grid[i+m][j+n]
            for n in "123456789":
                if tile.count(n) != 1:
                    return "No."
    return "Yes."


print(sudoku())
