print("Hello")

# Task: Rendu values-ah variables-la vachiko (e.g., a = 5, b = 10)
# Third variable (temp variable) use pannaama, andha rendu values-ah swap panni paaru!

a = 5
b = 10

# Write your code here to swap (Hint: Python-la single line-la panna mudiyum)
a, b = b, a

print("After Swapping:")
print(f"a = {a}, b = {b}") # Expected Output: a = 10, b = 5


# Un python file-la idha type panni paaru:
import sys

# 1. Immutable Overhead
text = "Chennai"
print(f"Original ID: {id(text)}")

text = text + " Data Lab" 
print(f"New ID: {id(text)}") # ID maaridum! Memory-la puthu string object allocate aairuchu.

# 2. Heavy Data Analytics Problem (Pass-by-Reference Pitfall)
original_dataset = [10, 20, 30, 40]
processed_dataset = original_dataset # Reference assigned!

processed_dataset.append(50)

print(f"Processed: {processed_dataset}")
print(f"Original: {original_dataset}") # Original-um [10, 20, 30, 40, 50] nu maarirukum!

import sys

my_list = [1, 2]
my_tuple = (1, 2)

# Size-ah check panni paarunga RAM memory byte usage allocation details:
print(sys.getsizeof(my_list))   # Heavy size kaatum
print(sys.getsizeof(my_tuple))  # Low size allocations optimization