'''
Exercise 1
Name: Seongeun Park, Linnazhang 

Question:
1. Write a function(s) that lets you enter your name, age and weight. Be sure to
say units you are using for weight and age.
2. Write a function(s) that asks the user the same information about themselves
3. Tell the user whether they are older or younger than you and by how many of
your units (probably years).
4. Tell them whether they weigh more or less than you and by how many of your
units.
'''


def ask_info():
    '''
    This function is to get information(name, age, weight)
    age unit: year
    weight unit: kg
    '''
    name = input("name:")
    age = input("age (year):")
    weight = input("weight (kg):")
    return name, age, weight

def compare_age(a_name, a_age,b_name, b_age):
    '''
    This function is for compare age between two
    '''
    unit = "year"
    if a_age > b_age:
        print(f"{a_name} is older than {b_name} {int(a_age)-int(b_age)}{unit})")
    elif a_age < b_age:
        print(f"{b_name} is older than {a_name} {int(b_age)-int(a_age)}{unit}")
    else:
        print(f"{a_name} and {b_name} is same age ({unit})")
    return

def compare_weight(a_name, a_weight,b_name, b_weight):
    '''
    This function is for compare weight between two
    '''
    unit = "kg"
    if a_weight > b_weight:
        print(f"{a_name} is heavier than {b_name} {float(a_weight)-float(b_weight)}({unit})")
    elif a_weight < b_weight:
        print(f"{b_name} is heavier than {a_name } {float(b_weight)-float(a_weight)}({unit})")
    else:
        print(f"{a_name} and {b_name} is same weight ({unit})")
    return

def main():
    a_name, a_age, a_weight = ask_info()
    b_name, b_age, b_weight = ask_info()

    compare_age(a_name, a_age, b_name, b_age)
    compare_weight(a_name, a_weight, b_name, b_weight)

main()