# https://adventofcode.com/2022/day/6#part2

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
        for i in range(13, len(line)):

            # Keep track of whether any characters are repeated
            repetition = False

            # Go through the last 13 characters
            for j in range(13):
                # Check whether they are all different
                if line.find(line[i - j], i - 13, i - j) != -1:
                
                    repetition = True
                    break
            
            # If all 14 characters were different, we've found the start of a
            # new message!
            if not repetition:

                print(i + 1)
                break