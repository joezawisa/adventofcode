# https://adventofcode.com/2022/day/9#part2

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Keep track of the head's and tail's current location
knots = [[0, 0] for _ in range(10)]
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
            knots[0][0] += direction[0]
            knots[0][1] += direction[1]

            # Then move each knot, one at a time
            for k in range(1, len(knots)):

                # Calculate the horizontal and vertical distances between this
                # knot and the previous knot
                horizontal = knots[k - 1][0] - knots[k][0]
                vertical = knots[k - 1][1] - knots[k][1]

                # Is this knot going to move?
                if (
                    (abs(horizontal) > 1) or
                    (abs(vertical) > 1)
                ):
                    # Move it horizontally if necessary
                    if (abs(horizontal) > 0):

                        knots[k][0] += horizontal // abs(horizontal)
                    
                    # Move it vertically if necessary
                    if (abs(vertical) > 0):

                        knots[k][1] += vertical // abs(vertical)
                
            # Mark the tail's location as visited
            visited.add(tuple(knots[len(knots) - 1]))

    # Print how many locations the tail visited at least once
    print(len(visited))