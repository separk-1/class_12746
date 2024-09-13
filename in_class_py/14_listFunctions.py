# This program illustrates the sequence functions on a string
# %%
myList = [10, 'testing', 6.6, [1, 2]]

print(" \n The number of elements in your List is", len(myList))

print(" \n The first element in your list is ", myList[0])

print(" \n The slice of your list between the 2nd and 4th element is ", myList[1:3])

# %%
myConcat = myList + myList[1:3]
print(" \n Your list plus your slice is ", myConcat)

newLetter = input("\n Enter a single letter ")

if newLetter in myList:
    print("\n ", newLetter, "is in the list ", myList)
else:
    print("\n ", newLetter, "is not in the list", myList)

# %%
myNewList=['S', 'u', 's', 'a', 'n']
print("\n  The smallest element in your newlist", myNewList, "is ", min(myNewList))
print("\n  The largest element in your newlist", myNewList, "is ", max(myNewList))
print("\n  The smallest element in your list is ", min(myList))
print("\n  The largest element in your list is ", max(myList))

