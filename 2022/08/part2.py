# https://adventofcode.com/2022/day/8#part2

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

    # Calculate the scenic score for a particular tree
    def scenic_score(row, column):

        # How many trees can we see to the left?
        left = column
        for c in range(column - 1, -1, -1):
            if (grid[row][c] >= grid[row][column]):
                left = column - c
                break
        
        # How many trees can we see to the right?
        right = len(grid[row]) - column - 1
        for c in range(column + 1, len(grid[row])):
            if (grid[row][c] >= grid[row][column]):
                right = c - column
                break
        
        # How many trees can we see up (at least I
        # think this is up - transposing is confusing)?
        up = row
        for r in range(row - 1, -1, -1):
            if (transposed_grid[column][r] >= transposed_grid[column][row]):
                up = row - r
                break
        
        # How many trees can we see down (at least I
        # think this is down - transposing is confusing)?
        down = len(transposed_grid[column]) - row - 1
        for r in range(row + 1, len(transposed_grid[column])):
            if (transposed_grid[column][r] >= transposed_grid[column][row]):
                down = r - row
                break

        # Multiply the number of trees we can see in each direction
        return left * right * up * down

    # Keep track of the highest scenic score
    highscore = 0

    # Calculate the scenic score for all the trees
    for row in range(len(grid)):

        for column in range(len(grid[row])):

            highscore = max(highscore, scenic_score(row, column))
    
    # Print the result!
    print(highscore)