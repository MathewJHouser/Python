import copy


class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return 'item:{}, price:{}, total weight: {}'.format(
            self.name, self.price, self.weight
            )

warehouse = list()

warehouse.append(Delicacy('Lolly Pop', 0.4, 133))
warehouse.append(Delicacy('Licorice', 0.1, 251))
warehouse.append(Delicacy('Chocolate', 1, 601))
warehouse.append(Delicacy('Sours', 0.01, 513))
warehouse.append(Delicacy('Hard candies', 0.3, 433))

new_warehouse = copy.deepcopy(warehouse)
for item in new_warehouse:
    if item.weight > 300:
        item.price *= 0.8

print('*' * 20)
print('Source list of candies')
for item in warehouse:
    print(item)

print('*' * 20)
print('Price proposal')
for item in new_warehouse:
    print(item)

# Check what happens if the line:
# new_warehouse = copy.deepcopy(warehouse)
# is exchanged with the following line:
# new_warehouse = copy.copy(warehouse)
