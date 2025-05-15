word = input("Enter word to search for: ")
puzzle = input("Enter puzzle string: ")
def FindWord (word, puzzle):
    k = 0
    word = word.upper()
    puzzle = puzzle.upper()
    for w in word:
        f = puzzle.find(w, k)
        if f < 0:
            return "No."
        k = f
    return "Yes. "

print(FindWord(word, puzzle))