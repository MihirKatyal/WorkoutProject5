class RPNCalculator:
    def __init__(self):
        self.stack = []

    def evaluate_expression(self, expression): # Evaluate the RPN expression
        if not expression:
            raise ValueError("Empty expression provided")
        for part in expression.split():
            if part in '+-*/':
                self._perform_operation(part)
            else:
                try:
                    self.stack.append(float(part))  # Convert strings to floats and push onto the stack.
                except ValueError:
                    raise ValueError(f"Invalid operand: {part}")
        if len(self.stack) != 1:
            raise ValueError("The RPN expression is invalid")
        return self.stack.pop()
    
    def _perform_operation(self, operator): # Perform the operation using the last two operands on the stack
        if len(self.stack) < 2:
            raise ValueError("Insufficient values in the expression")
        b, a = self.stack.pop(), self.stack.pop()
        if operator == '+':
            self.stack.append(a + b)
        elif operator == '-':
            self.stack.append(a - b)
        elif operator == '*':
            self.stack.append(a * b)
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            self.stack.append(a / b)