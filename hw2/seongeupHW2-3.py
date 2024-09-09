# Seongeun Park / seongeup / 12-746 A1 / Homework 2-3

def list_to_str(a_list):
    # list with the number of places aftrer the decimal point corresponding to the item's position in the list +1
    new_list = [f"{i:.{idx}f}" for idx, i in enumerate(a_list, start=1)]

    # string that looks just like the list
    a_str = "[" + ", ".join(new_list) + "]"
    return a_str

listOfIntegers = [6, 7, 10, 4, 6]
stringOfList = list_to_str(listOfIntegers)

print(stringOfList)