import math_utils

def main():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /, **, %): ")
        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod
        }
        if op in operations:
            result = operations[op](x, y)
            print("Result:", result)
        else:
            print("Invalid operator")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
