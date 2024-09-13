# This program illustrates how indenting changes code execution
# %%
anInteger = 10
# Case 1: Second if statement executes only if the first if statement is true
print("\nCase 1")
if anInteger > 11:
    print("anInteger is greater than 11")
    if anInteger <= 20:
        print("anInteger is less than or equal to 20")
print("End Case 1")

# %%	
# Case 2: Second if statement executes
print("\nCase 2")
if anInteger > 11:
    print("anInteger is greater than 11")
if anInteger <= 20:
    print("anInteger is less than or equal to 20")
print("End Case 2")
# %%
