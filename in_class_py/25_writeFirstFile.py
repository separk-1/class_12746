# %%
# use the open function to create a new file in write mode
newFile = open('output.text', 'w')

# create a string to write to the file
firstLine = 'This is the first line \n'

# use the write method to write the string to the file
newFile.write(firstLine)

# use the close method to close the file
newFile.close()

# %%
