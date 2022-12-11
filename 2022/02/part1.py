# https://adventofcode.com/2022/day/2

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Moves for me and my opponent
moves = {

    # Opponent
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',

    # Me
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'

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

        # Turn these useless letters into rocks, papers, and scissors
        opponent, me = line.strip().split()
        opponent, me = moves[opponent], moves[me]

        # If we tie, I get 3 extra points
        if opponent == me:
            
            total += points[me] + 3
        
        # If I win, I get 6 extra points!
        elif (
            me == 'Rock' and opponent == 'Scissors' or
            me == 'Paper' and opponent == 'Rock' or
            me == 'Scissors' and opponent == 'Paper'
        ):

            total += points[me] + 6
        
        # If I lose, I get no extra points :(
        else:

            total += points[me]

# Present the result!
print(total, file=sys.stdout)