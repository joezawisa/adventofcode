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

# Limits on the number of cubes of each color set by the elf
LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0

# Check whether each game could have been played with the number of cubes
# the elf limited us at
with open(filename, 'r') as input_file:
    for line in input_file:
        id = re.findall("Game (.*):", line)[0]

        exceeds_limit = False

        for color in LIMITS:
            for amount in re.findall(f"([0-9]*) {color}", line):
                if int(amount) > LIMITS[color]:
                    exceeds_limit = True
        
        if not exceeds_limit:
            sum += int(id)

print(sum, file=sys.stdout)