# Final Data Structure
result_list = []

# (Mostly) Side-Effect-Free Function
def process_number(x, operation):
    return operation(x)

# Higher-Order Function with Anonymous Function
def apply_operation(numbers, operation_function):
    return [operation_function(num) for num in numbers]

# Anonymous Function (Lambda)
square = lambda x: x**2

# Function as Parameter and Return Value
def double(x):
    return x * 2

def triple(x):
    return x * 3

# Closures / Anonymous Functions
def create_multiplier(factor):
    return lambda x: x * factor

# Example Usage
numbers = [1, 2, 3, 4]

result_list = apply_operation(numbers, lambda x: x + 1)
result_list.extend(apply_operation(numbers, square))
result_list.append(process_number(5, double))
result_list.append(process_number(5, triple))
result_list.append(process_number(5, create_multiplier(4)))

print("Original Numbers:", numbers)
print("Processed Numbers:", result_list)
