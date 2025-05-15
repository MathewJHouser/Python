with open("Day1Input") as f:
    lines = [line.rstrip() for line in f]
print(lines)

list1 = lines

list1 = [sub.replace("one", "o1e") for sub in list1]
list1 = [sub.replace("two", "t2o") for sub in list1]
list1 = [sub.replace("three", "t3e") for sub in list1]
list1 = [sub.replace("four", "f4r") for sub in list1]
list1 = [sub.replace("five", "f5e") for sub in list1]
list1 = [sub.replace("six", "s6x") for sub in list1]
list1 = [sub.replace("seven", "s7n") for sub in list1]
list1 = [sub.replace("eight", "e8t") for sub in list1]
list1 = [sub.replace("nine", "n9e") for sub in list1]

print(str(list1))

sum = 0

for i in list1:
    test = ''.join(c for c in i if c.isdigit())
    z = str(test)
    a = int(z[0])
    b = int(z[-1])
    Ans = 10 * a + b
    sum = sum + Ans

print(sum)