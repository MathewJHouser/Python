import random


class Apples:
    count = 0
    weight = 0

    def __init__(self, weight):
        self.weight = weight
        Apples.count += 1
        Apples.weight += weight


while Apples.count < 1000 and Apples.weight < 300:
    apple = Apples(random.uniform(0.2, 0.5))

print("Limit reached, details: ")
print("Number of Apples: ", Apples.count)
print("Total Weight: ", Apples.weight)


