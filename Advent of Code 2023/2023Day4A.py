import re

with open("Day4Input") as f:
    input = f.read()
#print(input)

lines = input.split('\n')

#print(lines)
regex = r':(.*?)\|(.*)'
points = 0
score = []
for line in lines:
    cards = line.split(': ')[1]
    #print(cards)

    for card in cards:
        nums = re.search(regex, line)
        winnum = set(map(int, nums.group(1).split()))
        havenum = set(map(int, nums.group(2).split()))
        matchnum = set(map(int, winnum & havenum))
        wins = len(matchnum)
        if wins != 0:
            points = 2 ** (wins - 1)
        else:
            points = 0
    score.append(points)
    #print(winnum, havenum)
print(score)
Ans = sum(score)
print(Ans)
