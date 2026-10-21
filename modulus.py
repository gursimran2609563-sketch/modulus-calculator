def calculate_modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = calculate_modulus(num1, num2)
    print(f"The modulus of {num1} and {num2} is: {result}")

