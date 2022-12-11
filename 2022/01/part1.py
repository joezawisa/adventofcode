# https://adventofcode.com/2022/day/1

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# We're going to start by assuming zero is the least amount of calories an
# elf could possibly be carrying. I mean, what is a negative calorie anyway?
most = 0

# Read input file
with open(sys.argv[1], 'r') as file:

    # As we inspect each elf's items, we're going to keep a total calorie count
    # for that elf
    calories = 0

    for line in file:

        if line == '\n':

            # When we see an empty line, that indicates that we are switching to
            # the next elf
            most = max(calories, most)
            calories = 0

        else:

            # Otherwise, let's add to the total for the current elf
            calories += int(line)

# Present the result!
print(most, file=sys.stdout)