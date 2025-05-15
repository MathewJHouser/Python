with open("Day1Input") as f:
    lines = [line.rstrip() for line in f]
print(lines)

sum = 0

for i in lines:
    test = ''.join(c for c in i if c.isdigit())
    z = str(test)
    a = int(z[0])
    b = int(z[-1])
    Ans = 10 * a + b
    sum = sum + Ans

print(sum)
