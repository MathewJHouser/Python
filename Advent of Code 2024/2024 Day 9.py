

class Compact_Files():
    def __init__(self):
        self.part1 = 0
        with open("Input Day 9") as f:
            data = f.read()
        self.digits = []
        for char in data:
            self.digits.append(int(char))
        print(self.digits)
        self.expand(self.digits)

    def expand(self, digits):
        new_string = ""
        for i, digit in enumerate(digits):
            id = 0
            if i % 2 == 0:
                # file length formula(i, digit) return string to concatenate
                id += 1

            else:
                #free space length



test = Compact_Files()