def greet(name):
    print(f"Hello, {name}!")

def calculate_area(length, width):
    return length * width

def is_even(number):
    return number % 2 == 0

def calculate_volume(length, width, height):
    base_area = calculate_area(length, width)
    return base_area * height

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


greet("John")

# Function invocation for calculate_area
length = 5
width = 3
area = calculate_area(length, width)
print("Area of the rectangle:", area)

# Function invocation for is_even
numbers = [4, 7, 10, 15, 22]
for num in numbers:
    result = is_even(num)
    print(f"{num} is even: {result}")

# Function invocation for calculate_volume
length = 4
width = 3
height = 2
volume = calculate_volume(length, width, height)
print("Volume of the rectangular prism:", volume)

# Function invocation for factorial
numbers = [5, 7, 10]
for num in numbers:
    result = factorial(num)
    print(f"Factorial of {num}: {result}")

def get_average(numbers):
    return sum(numbers) / len(numbers)

def get_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle = n // 2
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        middle = n // 2
        return sorted_numbers[middle]

# Function invocation for get_average
num_list = [12, 16, 8, 20, 10]
average = get_average(num_list)
print("Average:", average)

# Function invocation for get_median
median_value = get_median(num_list)
print("Median:", median_value)
