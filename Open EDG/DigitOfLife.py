text = input("Please enter your birthday: ")

def LifeDigit(t):
    if not t.isdigit():
        return "Please use a numerical format."

    while len(t) != 1:
        total = 0
        for c in t:
            total += int(c)
        t = str(total)
    return t

print( LifeDigit(text))
