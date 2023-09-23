import time

def list_average(numbers):
    try:
        # Filter out any non-numeric elements and calculate the average
        numeric_numbers = [float(num) for num in numbers]
        if len(numeric_numbers) == 0:
            raise ValueError("No valid numbers in the list")
        return sum(numeric_numbers) / len(numeric_numbers)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Generator function for Fibonacci sequence
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
