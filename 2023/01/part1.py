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

# Add up the first and last numbers on each line
with open(filename, 'r') as input_file:
    for line in input_file:
        numbers = re.findall("[0-9]", line)
        cal_value = int(numbers[0]) * 10 + int(numbers[-1])
        sum += cal_value

print(sum, file=sys.stdout)