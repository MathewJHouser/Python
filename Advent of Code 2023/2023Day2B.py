with open("Day2Input") as f:
    lines = [line.rstrip() for line in f]
print(lines)

power = 0

for line in lines:
    game = line.split(': ')[1]
    print(game)
    round = game.split('; ')
    #print(round)
    max_number = {'red': 0, 'green': 0, 'blue': 0}

    for hand in round:
        #print(hand)
        subset = hand.split(', ')

        for i in subset:
            n, color = i.split()
            #print(n, color)
            max_number[color] = max(int(n), max_number[color])

    print(max_number['red'], max_number['blue'], max_number['green'])
    power = power + max_number['red'] * max_number['blue'] * max_number['green']
    print(power)
