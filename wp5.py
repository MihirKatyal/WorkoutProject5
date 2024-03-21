import sys
from rpn_calculator import RPNCalculator

def main():
    if len(sys.argv) != 3:
        print("Usage: python wp5.py <inputfile> <outputfile>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, 'r') as input_file:
            expression = ''