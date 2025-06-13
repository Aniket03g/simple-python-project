def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def delete_number(a, b):
    """Return None to simulate deleting a number (for demo purposes)."""
    return None

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"The sum is: {add_numbers(x, y)}")
    print(f"Delete result: {delete_number(x, y)}")
