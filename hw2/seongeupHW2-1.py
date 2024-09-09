# Seongeun Park / seongeup / 12-746 A1 / Homework 2-1

def sum_even_integers(a, b):
    # First even number
    start = a+2 if a % 2 == 0 else a+1  
    
    # Last even number
    end = b-2 if b % 2 == 0 else b-1  
    
    # Number of even numbers
    n = (end - start) // 2 + 1  
    
    # Sum of even numbers = n * (first even number + last even number)
    even_sum = n * (start + end) // 2
    
    return even_sum

# Set the range
a, b = 0, 100

# Sum of even numbers between a and b
even_sum = sum_even_integers(a, b)

# Print the result with an explanation
print(f"Sum of the even integers between {a} and {b}: {even_sum}")