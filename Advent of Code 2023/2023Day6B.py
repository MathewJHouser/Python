import re

with open("Day6Input") as f:
    input = f.read()
#print(input)

lines = input.split('\n')
#print(lines)

times = re.findall(r'(\d+)', lines[0])
records = re.findall(r'\d+', lines[1])
print(times, records)
results = []
# Race 1
for i, time in enumerate(times):
    time1 = int(times[i])
    record1 = int(records[i])
    #print(time1)
    i = 0
    wins = 0
    while i < time1:
        hold = i
        speed = hold
        move = time1 - i
        distance = speed * move
        if distance > record1:
            wins = wins + 1
            i = i + 1
        else:
            i = i+1
    results.append(wins)
    print(results)
result = 1
for x in results:
    result = result * x
print("Total Wins:", result)