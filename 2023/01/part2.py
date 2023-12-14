import sys
import os
import re

# Check for correct command line arguments
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>", sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

# Make sure the input file is valid
if not os.path.isfile(filename):
    print("Error: Input file does not exist.", file=sys.stderr)
    sys.exit(1)

sum = 0

# Mapping from words to integers (These will count toward the  sum now)
words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# Add up the first and last numbers on each line
with open(filename, 'r') as input_file:
    for line in input_file:
        # The syntax of this regular expression is super important. Overlapping
        # matches won't count without the innermost set of parentheses.
        numbers = re.findall(r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", line)

        cal_value = (int(numbers[0]) if numbers[0].isdigit() else words[numbers[0]]) * 10
        cal_value += (int(numbers[-1]) if numbers[-1].isdigit() else words[numbers[-1]])
        sum += cal_value

print(sum, file=sys.stdout)