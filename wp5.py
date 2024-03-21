import sys
from rpn_calculator import RPNCalculator

def main():
    if len(sys.argv) != 3:
        print("Usage: python wp5.py <inputfile> <outputfile>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, 'r') as file:
            # Combine all lines into a single string of expressions, separated by spaces
            expressions = ' '.join(file.read().splitlines())
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
        sys.exit(1)

    # Process and write the results
    calculator = RPNCalculator()
    results = []
    for expression in expressions.split('/'):  # Assume each expression is separated by '/'
        try:
            result = calculator.evaluate_expression(expression)
            results.append(f"{expression} = {result}")
        except Exception as e:
            results.append(f"Error in expression '{expression}': {str(e)}")

    with open(output_filename, 'w') as file:
        file.write('\n'.join(results))

if __name__ == "__main__":
    main()
