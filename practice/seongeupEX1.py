'''
Exercise 1
Name: Seongeun Park, Linna Zhang
'''

def enter_details():
    """
    This function prompts the user to enter their own details: name, age, and weight.
    """
    # Get user details
    name = input("name: ")
    age = int(input("age (in years): "))
    weight = float(input("weight (in kilograms): "))
    
    return name, age, weight


def compare_users(my_name, my_age, my_weight, other_name, other_age, other_weight):
    # Compare ages
    if other_age > my_age:
        age_difference = other_age - my_age
        print(f"{other_name} is older than you.")
        print(f"{other_name} is {age_difference} years older than you.")
    elif other_age < my_age:
        age_difference = my_age - other_age
        print(f"{other_name} is {age_difference} years younger than you.")
    else:
        print(f"{other_name} is the same age as you.")
    
    # Compare weights
    if other_weight > my_weight:
        weight_difference = other_weight - my_weight
        print(f"{other_name} weighs {weight_difference} kilograms more than you.")
    elif other_weight < my_weight:
        weight_difference = my_weight - other_weight
        print(f"{other_name} weighs {weight_difference} kilograms less than you.")
    else:
        print(f"{other_name} weighs the same as you.")

# Enter details for the current user
my_name, my_age, my_weight = enter_details()

# Enter details for another user
other_name, other_age, other_weight = enter_details()

# Compare the two users
compare_users(my_name, my_age, my_weight, other_name, other_age, other_weight)

