import re
from itertools import cycle
from collections import Counter

with open('Day8Input') as f:
    input = f.read()

directions, data = input.split('\n\n')
directions = cycle(0 if d == 'L' else 1 for d in directions)
graph = {}

nodes = (re.findall(r'(\w{2}[A]) ', data))
print(nodes)

for node, left, right in re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', data):
    graph[node] = [left, right]

list1=[]

for node in nodes:
    for steps, d in enumerate(directions, start=1):
        node = graph[node][d]
        if node[2] == 'Z':
            break
    list1.append(steps)

print(list1)

def factors(num):
    i = 2
    factors = []
    while i <= num:
        if (num % i) == 0:
            factors.append(i)
            num = num / i
        else:
            i = i + 1
    return(factors)

def lcm_of_factors(list):
    # empty dictionary
    unique = {}

    for i in range(0, len(list)):
        number = list[i]
        numbers = factors(number)
        count = Counter(numbers)

        for k, v in count.items():
            if k not in unique:
                unique[k] = v
            elif k in unique and v > unique[k]:
                unique[k] = v
            else:
                pass
    result = 1

    for k, v in unique.items():
        result = result * (k ** v)

    return result

print(lcm_of_factors(list1))