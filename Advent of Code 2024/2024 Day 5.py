import re

class SafetyManual():
    def __init__(self):
        with open("Input Day 5") as f:
            self.data = f.read()
        a, b = self.data.split("\n\n")
        self.rule = a.split()
        self.pages = b.split()
        self.good = 0
        self.bad = 0
        self.sum = 0
        self.total = 0

    def rules(self, string):
        for r in self.rule:
            first, last = re.findall(r"(\d+)", r)
            a = string.find(first)
            b = string.find(last)
            if a and b != -1:
                if a>b:
                    self.bad +=1
                    return False
        self.good +=1
        return True

    def orders(self):
        for lists in self.pages:
            a = str(lists)
            b = self.rules(a)
            if b == True:
                self.count(a)
            if b != True:
                self.correcting(a)

    def count(self, string):
        a = re.findall(r"(\d+)", string)
        middle = (len(a) - 1)//2
        b = a[middle]
        self.sum += int(b)

    def correcting(self, string):
        a = re.findall(r"(\d+)", string)
        for r in self.rule:
            first, last = re.findall(r"(\d+)", r)
            try:
                b = a.index(first)
                c = a.index(last)
                if b > c:
                    a[b], a[c] = last, first
            except:
                pass
        d = ','.join(a)
        if self.rules(d) == True:
            self.summation(d)
        if self.rules(d) == False:
            self.correcting(d)

    def summation(self, string):
        a = re.findall(r"(\d+)", string)
        middle = (len(a) - 1) // 2
        b = a[middle]
        self.total += int(b)


day5 = SafetyManual()
day5.orders()
print("Part One =", day5.sum, "\nPart Two =", day5.total)