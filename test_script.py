from rpn_calculator import RPNCalculator

def main():
    # Create an instance of the RPNCalculator class
    calculator = RPNCalculator()

    # Define a test expression in Reverse Polish Notation
    expression = "3 4 +"

    # Use the calculator to evaluate the expression
    result = calculator.evaluate_expression(expression)

    # Print the result
    print(f"The result of the expression '{expression}' is: {result}")

if __name__ == "__main__":
    main()