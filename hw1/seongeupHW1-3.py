# Seongeun Park / seongeup / 12-746 A1 / Homework 1

family_name="Park"

asciisum=(sum(ord(char) for char in family_name))
 
print(f"numerical value of my family name: {asciisum}")
print((f"{asciisum} is the sum of the ASCII values for \
'{family_name[0]}({ord(family_name[0])})', '{family_name[1]}({ord(family_name[1])})', \
'{family_name[2]}({ord(family_name[2])})', '{family_name[3]}({ord(family_name[3])})'."))