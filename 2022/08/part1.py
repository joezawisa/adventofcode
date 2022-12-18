# https://adventofcode.com/2022/day/8

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Read input file
with open(sys.argv[1], 'r') as file:

    # Make a 2D array to represent the map
    grid = [list(map(int, line.strip())) for line in file]
    transposed_grid = list(map(list, zip(*grid)))

    # Keep track of how many trees are visible
    visible = 0

    # Check whether each tree is visible
    for row in range(len(grid)):

        for column in range(len(grid[row])):

            if (
                ( # Is it in the first row or the first column?
                    (row == 0) or
                    (column == 0)
                ) or ( # Are all the trees to its left shorter?
                    (grid[row][column] not in grid[row][:column]) and
                    (grid[row][column] == max(grid[row][:column + 1]))
                ) or ( # Are all the trees to its right shorter?
                    (grid[row][column] not in grid[row][column + 1:]) and
                    (grid[row][column] == max(grid[row][column:]))
                ) or ( # Are all the trees above/below (not sure which, since transposing is confusing) it shorter?
                    (transposed_grid[column][row] not in transposed_grid[column][:row]) and
                    (transposed_grid[column][row] == max(transposed_grid[column][:row + 1]))
                ) or ( # Are all the trees above/below (not sure which, since transposing is confusing) it shorter?
                    (transposed_grid[column][row] not in transposed_grid[column][row + 1:]) and
                    (transposed_grid[column][row] == max(transposed_grid[column][row:]))
                )
            ):

                visible += 1
    
    # Print the result!
    print(visible)