# %%
# This program illustrates methods defined for the class string

myString = "This is a test"
print('My string is: ',myString, '\nIt is a Python variable of ', type(myString))
upString = str.upper(myString)
print('\n',upString,'\n')

tees = myString.count('t')
print('The number of ts in myString is ', tees)

whereIsT = myString.index('T')

print('The first T is at index ', whereIsT)

print('It is ', upString.isupper(), 'that upString is upper case')
print('It is ', myString.isupper(), 'that myString is upper case')


# %%
