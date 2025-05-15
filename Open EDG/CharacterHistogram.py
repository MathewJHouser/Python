file_name = input("Enter file name: ")
stream = open(file_name, "rt")
data = stream.read().lower()
stream.close()

my_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
           "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

for key in my_dict.keys():
    cnt = data.count(key)
    my_dict[key] = cnt

counters = sorted(my_dict.keys(), key=lambda x: my_dict[x], reverse=True)
out = ""

for letter in counters:
    if my_dict[letter] != 0:
        s = letter + " -> " + str(my_dict[letter]) + "\n"
        out += s

handle = open(file_name + ".hist", "wt")
handle.write(out)
handle.close()
