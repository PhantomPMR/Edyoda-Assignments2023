class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculate(self, operation):
        operations = {
            'add': self.num1 + self.num2,
            'subtract': self.num2 - self.num1,
            'multiply': self.num1 * self.num2,
            'divide': self.num2 / self.num1 if self.num1 != 0 else "Cannot divide by zero"
        }
        result = operations.get(operation, "Invalid operation")
        return result

# Example usage with user input:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

obj = Calculator(num1, num2)
print(obj.calculate(operation))
