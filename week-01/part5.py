'''import time
from utilities import list_average 

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def fibonacci_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

numbers = [1, 2, 3, 4, 5]
try:
    average = list_average(numbers)
    print(f"The average is: {average}")
except Exception as e:
    print(f"Error: {e}") 

def calculate_average(numbers):
    return list_average(numbers)

@execution_time
def calculate_average(numbers):
    return list_average(numbers)

numbers = [1, 2, 3, 4, 5]
calculate_average(numbers)

for num in fibonacci_gen(10):
    print(num) ''' 


import time
from utilities import list_average, execution_time, fibonacci_gen

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate and print the average with error handling
try:
    average = list_average(numbers)
    print(f"The average is: {average:.2f}")  # Use {:.2f} to format the average with 2 decimal places
except Exception as e:
    print(f"Error: {e}")

# Calculate and print the average with the execution_time decorator
@execution_time
def calculate_average(numbers):
    return list_average(numbers)

calculate_average(numbers)

# Generate and print the Fibonacci sequence up to the 10th number
n = 10
print(f"Fibonacci sequence up to the {n}th number:")
for num in fibonacci_gen(n):
    print(num)
