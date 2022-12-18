# https://adventofcode.com/2022/day/6

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Read input file
with open(sys.argv[1], 'r') as file:

    # We really only need to read one line because the entire datastream buffer
    # is on the first line, but I did it line by line so that I could test on
    # all the examples at once
    for line in file:

        # Go through each character in the datastream buffer
        for i in range(3, len(line)):

            # Check whether it is different from the previous three characters
            if (
                line[i] not in line[i - 3:i] and
                line[i - 1] not in line[i - 3:i - 1] and
                line [i - 2] not in line[i - 3:i - 2]
            ):

                # If it is, we're done. This is the start of a new packet!
                print(i + 1)
                break