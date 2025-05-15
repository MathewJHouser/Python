text = input("Please Enter Your Message: ")
try:
    s = int(input("Please Enter a Shift Value Between 1 and 25: "))
except:
    print("Shift value entered is not a number. Please try again. ")
if s > 25 or s < 1:
    print("Shift value must be a number between 1 and 25. ")

cipher = ""
for c in text:
    if not c.isalpha():
        cipher += c
        continue
    code = ord(c) + s
    if c.isupper() and code > ord("Z"):
        code = ord("A") + code - ord("Z") - 1
    if c.islower() and code > ord("z"):
        code = ord("a") + code - ord("z") -1
    cipher += chr(code)
print(cipher)
