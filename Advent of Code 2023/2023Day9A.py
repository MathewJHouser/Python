with open('Day9Input') as f:
    input = f.read()

sequences = input.split('\n')
print(sequences)

total = 0
for line in input.split('\n'):
    sequence = [int(n) for n in line.split()]
    nums = []

    while set(sequence) != set([0]):
        nums.append(sequence[-1])
        sequence = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    total = total + sum(nums)
print(total)
