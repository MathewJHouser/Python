import re

with open("Day4Input") as f:
    input = f.read()
#print(input)

lines = input.split('\n')
#print(lines)

regex = r':(.*?)\|(.*)'

score = []
cards2 = [1] * len(lines)
print cards2
for i, line in enumerate(lines):
    nums = re.search(regex, line)
    winnum = set(map(int, nums.group(1).split()))
    havenum = set(map(int, nums.group(2).split()))
    #print(winnum, havenum)
    wins = len(winnum & havenum)


    for j in range(i+1, i + wins + 1):
        cards2[j] += cards2[i]
        #print(cards2)
ans = sum(cards2)
print(ans)
