def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"The sum is: {add_numbers(x, y)}")
    print(f"The product is: {multiply_numbers(x, y)}")
