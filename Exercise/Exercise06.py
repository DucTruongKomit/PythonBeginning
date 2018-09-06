s = str(input("Please type: "))
#read frome the end to the start of string
sbw = s[::-1]
print()
if s == sbw:
    print("This string is a palindrome")
else:
    print("This string isn't a palindrome")