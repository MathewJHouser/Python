def read_int(prompt, mini, maxi):
    text = input(prompt)
    try:
        n = int(text)
        assert mini < n < maxi
        return n
    except ValueError:
        print("Error: Wrong Input. ")
        return read_int(prompt, mini, maxi)
    except AssertionError:
        print("Error: The value is not within the permitted range: (", mini, ",", maxi, ").")
        return read_int(prompt, mini, maxi)


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
