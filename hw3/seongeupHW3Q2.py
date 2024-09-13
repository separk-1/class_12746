# Seongeun Park / seongeup / 12-746 A1 / Homework 3-2

import random
from seongeupHW3Q1 import write_random_numbers_to_file

def read_numbers_from_file(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    return numbers

'''
or 
from seongeupHW3Q1 import write_random_numbers_to_file
(may not work with automated grade system)
'''
def write_random_numbers_to_file(filename):
    with open(filename, 'w') as f:
        num_numbers = random.randint(1, 1e3)  # 1-1000
        for _ in range(num_numbers):
            f.write(f"{random.randint(1, 1e2)}\n")  # 1-100


filename = 'random_numbers.txt'
write_random_numbers_to_file(filename)
numbers = read_numbers_from_file(filename)

print(numbers)