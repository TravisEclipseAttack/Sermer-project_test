class Calculator:
    """Класс калькулятора с расширенным функционалом"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Сложение двух чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Умножение двух чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self):
        """Получить историю вычислений"""
        return self.history.copy()
    
    def clear_history(self):
        """Очистить историю вычислений"""
        self.history.clear()