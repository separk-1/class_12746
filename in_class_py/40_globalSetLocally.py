# A variable that is declared in the main program is available
# anywhere within the program including within functions
# BUT a locally defined variable with the same name overrides
# the global definition. To assign a value to a global variable within
# a function, you need to declare the global variable within the function

showOff = True

def thisIsATest():
# The global statement in the next line tells Python not to create
# a local variable within the function, but to use the global variable
# Except in very special cases, this is a bad idea.
    global showOff
    showOff = False
    print("Within the function, showOff is ", showOff)


thisIsATest()
print("In the main program, showOff is ", showOff)
