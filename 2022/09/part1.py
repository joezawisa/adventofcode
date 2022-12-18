# https://adventofcode.com/2022/day/9

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Keep track of the head's and tail's current location
head = [0, 0]
tail = [0, 0]
# And every location the tail has visited
visited = {(0, 0)}

# Conversions from letters to directions
directions = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0]
}

# Read input file
with open(sys.argv[1], 'r') as file:

    for line in file:

        # Interpret the movement
        direction, distance = line.strip().split()
        direction = directions[direction]
        distance = int(distance)

        # Move one step at a time
        for _ in range(distance):

            # Move the head
            head[0] += direction[0]
            head[1] += direction[1]

            # Calculate the horizontal and vertical distances between head and tail
            horizontal = head[0] - tail[0]
            vertical = head[1] - tail[1]

            # Is the tail going to move too?
            if (
                (abs(horizontal) > 1) or
                (abs(vertical) > 1)
            ):
                # Move it horizontally if necessary
                if (abs(horizontal) > 0):

                    tail[0] += horizontal // abs(horizontal)
                
                # Move it vertically if necessary
                if (abs(vertical) > 0):

                    tail[1] += vertical // abs(vertical)
                
                # Mark this location as visited
                visited.add(tuple(tail))

    # Print how many locations the tail visited at least once
    print(len(visited))