# https://adventofcode.com/2022/day/3

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Keep a running total of the priorities of all the items that are packed incorrectly
total = 0

# Read input file
with open(sys.argv[1], 'r') as file:

    # Check each backpack
    for line in file:

        line = line.strip()

        # Grab each item from the first compartment
        for item in line[:len(line) // 2]:

            # And check whether it's in the second compartment
            if item in line[len(line) // 2:]:

                # When we find the item in both compartments, add its priority to the total
                total += ord(item) - 96 if item.islower() else ord(item) - 38
                break

# Present the result!
print(total, file=sys.stdout)