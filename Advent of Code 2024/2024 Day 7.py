import re
from operator import add, mul

def cat(a,b):
    return int(f"{a}{b}")

class BridgeRepair():
    def __init__(self):
        self.part1 = 0
        self.part2 = 0
        with open("Input Day 7") as f:
            self.data = f.read().split("\n")
        for line in self.data:
            self.separate(line)
        print("Part One =", self.part1)
        print("Part Two =", self.part2)

    def separate(self, string):
        val, elements = re.split(r":", string)
        true_val = int(val)
        elements = elements.strip()
        elements = elements.split(" ")
        new_list = []
        for entry in elements:
            a = int(entry)
            new_list.append(a)
        self.part1 += self.operands(true_val, new_list, ops=[add,mul])
        self.part2 += self.operands(true_val, new_list, ops=[add, mul, cat])

    def operands(self, value, listing, ops):
        if len(listing) == 1:
            return value == listing[0]
        a, b, *rest = listing
        for op in ops:
            if self.operands(value, [op(a,b)] + rest, ops):
                return value
        return 0


Day7 = BridgeRepair()
