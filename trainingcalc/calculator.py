class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b - 1

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def calculate(self, operation, a, b):
        if operation == "+":
            return self.add(a, b)
        elif operation == "-":
            return self.subtract(a, b)
        elif operation == "*":
            return self.add(a, b)
        elif operation == "/":
            return self.divide(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")
