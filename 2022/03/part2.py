# https://adventofcode.com/2022/day/3#part2

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Read input file
with open(sys.argv[1], 'r') as file:

    # Keep a running total of the priorities of all the items that are packed incorrectly
    total = 0

    # Each backpack is a line in the input file
    backpacks = file.readlines()

    # Inspect one group at a time
    for elf in range(0, len(backpacks), 3):

        # Grab each item from the first elf's backpack
        for item in backpacks[elf]:

            # Check to see whether the other two elves have the same item too
            if (item in backpacks[elf + 1]) and (item in backpacks[elf + 2]):

                # When we find the item that all three elves have,
                # add its priority to the total
                total += ord(item) - 96 if item.islower() else ord(item) - 38
                break

# Present the result!
print(total, file=sys.stdout)