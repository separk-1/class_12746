# %%
def reverse(aList):
    # This is a user defined function that returns a list in reverse order
    # Note that user defined function "reverse" has the same name as the
    # built-in method "reverse" for strings
    # Note that the reverse method operates on the string itself and does
    # not return a value. 
    aList.reverse()
    return aList

# %%
myWords = ["this", "is", "a", "test"]

print("My words are: ", myWords)

# Use the user-defined function to create a new variable containing the reverse the list
reverseWords = reverse(myWords)
print("My words reversed with my user defined function are ", reverseWords)

# Use the reverse method to reverse the list in place
myWords.reverse()
print("My words reversed using the reverse method for lists are", myWords)

# %%
