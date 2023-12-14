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

# Sum the powers of the minimum sets of cubes for each game
with open(filename, 'r') as input_file:
    for line in input_file:
        power = 1

        # Find the maximum cubes that were used (a.k.a. the minimum needed)
        # of each color
        for color in ['red', 'green', 'blue']:
            maximum = 0
            for amount in re.findall(f"([0-9]*) {color}", line):
                maximum = max(maximum, int(amount))
            
            power *= maximum
        
        sum += power

print(sum, file=sys.stdout)