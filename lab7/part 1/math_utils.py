def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(4, 6))
    print(divide(10, 2))
    print(divide(5, 0))
    print(power(2, 3))
    print(mod(10, 3))
