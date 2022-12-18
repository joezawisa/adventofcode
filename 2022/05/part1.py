# https://adventofcode.com/2022/day/5

import sys
import collections

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Read input file
with open(sys.argv[1], 'r') as file:

    # Read the first line
    line = file.readline()
    # Then use it to figure out how many stacks we have
    stacks = [collections.deque() for _ in range(len(line) // 4)]

    # Read in all the stacks, stopping when there are no more crates
    while line.find('[') != -1:

        # Isolate the letter for each crate
        for c in range(len(line) // 4):

            # Ignore stacks that don't have a crate at this level
            if line[(c * 4) + 1] != ' ':
                
                stacks[c].appendleft(line[(c * 4) + 1])
        
        line = file.readline()

    # Skip the empty line between the stacks and rearrangement procedure
    file.readline()

    # Read in all the instructions
    for line in file:

        instruction = line.strip().split()

        for i in range(int(instruction[1])):

            stacks[int(instruction[5]) - 1].append(stacks[int(instruction[3]) - 1].pop())

    # Print the top crate from each stack
    print(*[stack.pop() for stack in stacks], sep='')