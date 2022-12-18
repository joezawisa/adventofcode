# https://adventofcode.com/2022/day/7

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

    # Now that we know the file system, total the sizes of all directories with
    # a size of 100000 or less with some good ol' recursion
    def total(fs: dict):

        sum = fs['size'] if fs['size'] <= 100000 else 0

        for child in fs['contents']:

            if fs['contents'][child]['type'] == 'directory':

                sum += total(fs['contents'][child])
        
        return sum
    
    # Print the result!
    print(total(filesystem))