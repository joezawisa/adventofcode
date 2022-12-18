# https://adventofcode.com/2022/day/5#part2

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

        # Break the instruction into words
        instruction = line.strip().split()

        # Start a temporary stack for the crates that will be moved
        moving = collections.deque()

        # Move the crates from the source stack into a temporary stack. This
        # doesn't really correspond to the physics of what's happening, but it
        # works to find the information we need
        for i in range(int(instruction[1])):

            moving.append(stacks[int(instruction[3]) - 1].pop())
        
        # Move the crates from the temporary stack to the destination stack
        for i in range(int(instruction[1])):

            stacks[int(instruction[5]) - 1].append(moving.pop())

    # Print the top crate from each stack
    print(*[stack.pop() for stack in stacks], sep='')