with open("inputdata.txt", "r") as f:  # opens inputdata txt file and reads contents.
    s = f.read()
for i in range(len(s)):  # for the length of the inputdata
    if s[i].isalnum():
        print(s[i], end="")  # prints string in one line
    else:
        if s[i - 1].isalnum():  # prints lexemes in newline
            print()
        print(s[i])
