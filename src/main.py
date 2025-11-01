from .calculator import Calculator

def hello_world():
    """Базовая функция Hello World"""
    return "Hello, World!"

def add_numbers(a, b):
    """Функция сложения двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a + b

def multiply_numbers(a, b):
    """Функция умножения двух чисел"""
    return a * b

def main():
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"4 * 5 = {multiply_numbers(4, 5)}")
    
    # Демонстрация исправления
    try:
        result = add_numbers(5, "3")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Демонстрация нового класса Calculator
    calc = Calculator()
    print(f"Using Calculator: 10 + 15 = {calc.add(10, 15)}")
    print(f"Using Calculator: 6 * 7 = {calc.multiply(6, 7)}")
    print("Calculation history:", calc.get_history())

if __name__ == "__main__":
    main()