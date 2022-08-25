number = int(input("Enter a number > "))
string = input("Enter a string > ")


n = int(len(string) / 2)
string2 = string[0:n]
string3 = string[len(string) - n:]
rev_string3 = string3[len(string3)::-1]

if string2 == rev_string3:
    print("Palindrome!")
else:
    print("Not A Palindrome!")
