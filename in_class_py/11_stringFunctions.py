# %%
# This program illustrates functions that operate on strings

myString = input("Enter a string at least 5 characters long to play with ")
print(" The first character in your string is ", myString[0])
print(" The slice of your string between the 2nd and 4th character is ", myString[1:3])

myConcat = myString + myString[1:3]
print(" Your string plus your slice is ", myConcat)

newLetter = input("Enter a single letter ")
if newLetter in myString:
    print(" ", newLetter, "is in your string")
    print(" The smallest letter in your string is ", min(myString))
else:
    print(" ", newLetter, "is not in your string")
    print(" The largest letter in your string is ", max(myString))

# %%
