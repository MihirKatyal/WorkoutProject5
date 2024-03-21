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