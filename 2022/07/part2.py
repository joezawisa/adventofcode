# https://adventofcode.com/2022/day/7#part2

import sys
import collections

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

filesystem = {
    'type': 'directory',
    'contents': {},
    'size': 0
}

path = collections.deque()
working_directory = filesystem

# Read input file
with open(sys.argv[1], 'r') as file:

    # Learn the file system
    for line in file:

        # Break each line into individual words
        words = line.strip().split()

        # Check if the line is a command
        if words[0] == '$':

            # Check if it is a change directory command
            if words[1] == 'cd':

                # Return to the root directory
                if words[2] == '/':

                    path.clear()

                # Return to the parent directory
                elif words[2] == '..':

                    path.pop()

                # Or navigate to a child directory
                else:

                    path.append(words[2])

            # Check if it is a list command
            elif words[1] == 'ls':

                # Start at the root directory
                working_directory = filesystem

                # Navigate to the working directory as specified by the previous
                # 'cd' commands
                for directory in path:

                    if directory not in working_directory['contents']:

                        working_directory['contents'][directory] = {
                            'type': 'directory',
                            'contents': {},
                            'size': 0
                        }

                    working_directory = working_directory['contents'][directory]
        
        # If the line is not a command, it must be a listing of contents as a
        # response to an 'ls' command
        else:

            # If this is a directory we have not seen before, add it to the file
            # system as an empty directory
            if words[0] == 'dir':

                if words[1] not in working_directory['contents']:

                    working_directory['contents'][words[1]] = {
                        'type': 'directory',
                        'contents': {},
                        'size': 0
                    }
            
            # If it is a file, add the file to the file system and include its
            # size in every parent directory
            else:

                working_directory['contents'][words[1]] = {
                    'type': 'file',
                    'size': int(words[0])
                }

                tracing_directory = filesystem
                tracing_directory['size'] += int(words[0])

                for directory in path:

                    tracing_directory = tracing_directory['contents'][directory]
                    tracing_directory['size'] += int(words[0])

    # So... what is the minimum size directory that we need to delete to make
    # space for the update?
    minimum = 30000000 - (70000000 - filesystem['size'])

    # Now that we know the file system and how big of a directory we need to
    # delete, let's find the smallest directory we can delete to make space
    def delete(fs: dict):

        smallest = fs['size'] if fs['size'] >= minimum else float('inf')

        for child in fs['contents']:

            if fs['contents'][child]['type'] == 'directory':

                smallest = min(smallest, delete(fs['contents'][child]))
        
        return smallest
    
    # Print the result!
    print(delete(filesystem))