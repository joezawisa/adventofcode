# https://adventofcode.com/2022/day/2#part2

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Moves for my opponent
moves = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

# Points for each move
points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

# Keep a total of all the points I've earned
total = 0

# Read input file
with open(sys.argv[1], 'r') as file:

    # Calculate the points for each round and add them to the total
    for line in file:

        # Turn these useless letters into rocks, papers, and scissors, and outcomes
        opponent, outcome = line.strip().split()
        opponent = moves[opponent]

        # If I lose, I don't get any extra points :(
        if outcome == 'X':

            # Map of what to play, with my opponent's move on the left and my
            # move on the right
            strategy = {
                'Rock': 'Scissors',
                'Paper': 'Rock',
                'Scissors': 'Paper'
            }

            total += points[strategy[opponent]]
        
        # If we tie, I get 3 extra points :)
        elif outcome == 'Y':

            total += points[opponent] + 3
        
        # If I win, I get 6 extra points!
        elif outcome == 'Z':

            # Map of what to play, with my opponent's move on the left and my
            # move on the right
            strategy = {
                'Rock': 'Paper',
                'Paper': 'Scissors',
                'Scissors': 'Rock'
            }

            total += points[strategy[opponent]] + 6

# Present the result!
print(total, file=sys.stdout)