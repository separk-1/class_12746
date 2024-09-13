# Seongeun Park / seongeup / 12-746 A1 / Homework 3-1

import random

def write_random_numbers_to_file(filename):
    with open(filename, 'w') as f:
        num_numbers = random.randint(1, 1e3)  # 1-1000
        for _ in range(num_numbers):
            f.write(f"{random.randint(1, 1e2)}\n")  # 1-100


write_random_numbers_to_file('random_numbers.txt')
    