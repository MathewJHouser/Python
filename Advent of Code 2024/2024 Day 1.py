with open("Input Day 1") as f:
    input = f.read()

left = []
right = []
sum = 0
lines = input.split("\n")
total = 0

for line in lines:
    (l, r) = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

for i in range(len(left)):
    difference = abs(left[i]-right[i])
    sum += difference

print(sum)

for i in range(len(left)):
    c = right.count(left[i])
    total += c * left[i]

print(total)
