# https://adventofcode.com/2022/day/1#part2

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# This time, we're going to build an array where each element is the total
# number of calories a particular elf is carrying
elves = []

# Read input file
with open(sys.argv[1], 'r') as file:

    # As we inspect each elf's items, we're going to keep a total calorie count
    # for that elf
    calories = 0

    for line in file:

        if line == '\n':

            # When we see an empty line, that indicates that we are switching to
            # the next elf
            elves.append(calories)
            calories = 0

        else:

            # Otherwise, let's add to the total for the current elf
            calories += int(line)
    
    # Don't forget the last elf!
    elves.append(calories)

# Now we need to total all the calories held by the top three elves
elves.sort(reverse=True)
total = sum(elves[0:3])

# Present the result!
print(total, file=sys.stdout)