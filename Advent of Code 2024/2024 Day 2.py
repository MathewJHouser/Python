with open("Input Day 2") as f:
    reports = f.read().split("\n")

safe = 0
unsafe = 0

for report in reports:
    levels = []
    repor = report.split()

    for r in repor:
        levels.append(int(r))

    level_down = levels[:]
    level_down.sort()
    level_up = level_down[:]
    level_down.reverse()

    if levels == level_up or levels == level_down:
        l = len(levels)
        for i in range(l-1):
            d = abs(levels[i]-levels[i+1])

            if d < 1 or d > 3:
                unsafe += 1
                break

            else:
                if i+2 == l:
                    safe += 1

    else:
        unsafe += 1

print("Safe = ", safe, "Unsafe = ", unsafe)

safety = []
unsafety = []
yes = 0
no = 0

class Difference:
    def __init__(self, list):
        self.levels = list
        self.length = len(list)
    def diff(self):
        for i in range(self.length-1):
            d = abs(self.levels[i]-self.levels[i+1])

            if d < 1 or d > 3:
                return False
        return True

class Order:
    def __init__(self, list):
        self.levels = list
        self.down = sorted(list, reverse=True)
        self.up = sorted(list)
    def compare(self):
        if self.levels == self.down:
            return True
        elif self.levels == self.up:
            return True
        else:
            return False

class Dampener:
    def __init__(self, list):
        self.initial = list
        self.final = []
    def remake(self):
        l = len(self.initial)
        for i in range(l):
            a = self.initial[:]
            del a[i]
            self.final.append(a)
        return self.final

for report in reports:
    levels = []
    repor = report.split()

    for r in repor:
        levels.append(int(r))

    if Order(levels).compare():
        if Difference(levels).diff():
            safety.append(levels)
            yes += 1
        else:
            unsafety.append(levels)
    else:
        unsafety.append(levels)


for code in unsafety:
    z = []
    for entry in Dampener(code).remake():
        if Order(entry).compare() == True and Difference(entry).diff() == True:
            z.append(1)
        else:
            z.append(0)
    if 1 in z:
        yes += 1
    else:
        no += 1


print("Safe =", yes, " Unsafe =", no)

