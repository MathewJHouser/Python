w1 = input("Enter a word: ")
w2 = input("Enter another word: ")

def anagrams(w1, w2):
    if w1 and w2 == "":
        return "Please enter two words."
    W1 = ""
    W2 = ""
    for c in w1:
        if c.isalpha():
            c = c.upper()
            W1 += c
    for c in w2:
        if c.isalpha():
            c = c.upper()
            W2 += c
    for a in W1:
        if W1.count(a) != W2.count(a):
            return "Not anagrams."
    for b in W2:
        if W1.count(b) != W2.count(b):
            return "Not anagrams. "
        else: return "Anagrams."

print(anagrams(w1, w2))
