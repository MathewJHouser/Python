with open('Day15Input') as f:
    input = f.read()

entries = input.split(',')
total = []
for entry in entries:
    #print(entry)
    s = 0
    for c in entry:
        a = ord(c)
        s = s + a
        s = s * 17
        s = s % 256
    #print(s)
    total.append(s)
ans = sum(total)
print(ans)