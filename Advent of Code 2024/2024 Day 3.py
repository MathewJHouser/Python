import re
with open("Input Day 3") as f:
    data = f.read()
sum = 0
a = re.findall(r"mul\(\d+,\d+\)", data)
for i in a:
    b, c = re.findall(r"(\d+)", i)
    b, c = int(b), int(c)
    sum += b * c

print(sum)

class Mult:
    def __init__(self, string):
        self.sum = 0
        self.string = string
    def mul(self):
        a = re.findall(r"mul\(\d+,\d+\)", self.string)
        for i in a:
            b, c = re.findall(r"(\d+)", i)
            b, c = int(b), int(c)
            self.sum += b * c
        return self.sum



y = re.findall(r"don't|do", data)
x = re.split(r"don't|do", data)
switch = True
total = 0
i = 0
j = 0
while i < len(x):
    if switch == True:
        t = Mult(x[i]).mul()
        total += t
    else:
        pass
    if i < len(y):
        if y[i] == "do":
            switch = True
        if y[i] =="don't":
            switch = False
    i += 1

print(total)
