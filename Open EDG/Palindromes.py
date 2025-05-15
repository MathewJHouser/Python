text = input("Enter Your Message: ")
text  = text.strip()
if text == "":
    print("This is not a palindrome.")
r = []
a = ""
for c in text:
    if not c.isalpha():
        continue
    c = c.upper()
    a += c
    r.insert(0, c)
    b = "".join(r)
if a == b:
    print("This is a palindrome. ")
else:
    print("This is not a palindrome. ")