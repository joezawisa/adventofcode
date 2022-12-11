# https://adventofcode.com/2022/day/4#part2

import sys

# Check for proper invocation
if len(sys.argv) != 2:

    print(f'Usage: {sys.argv[0]} <filename>', file=sys.stderr)
    sys.exit(1)

# Keep a running total of how many assignment pairs have overlapping ranges
overlapping = 0

# Read input file
with open(sys.argv[1], 'r') as file:

    for line in file:

        # Get the starting and ending section for each elf in the pair
        first_elf, second_elf = line.strip().split(',')
        first_elf_start, first_elf_end = first_elf.split('-')
        first_elf_start, first_elf_end = int(first_elf_start), int(first_elf_end)
        second_elf_start, second_elf_end = second_elf.split('-')
        second_elf_start, second_elf_end = int(second_elf_start), int(second_elf_end)

        # Check if the ranges overlap
        if (
            ((first_elf_start <= second_elf_start) and (second_elf_start <= first_elf_end)) or
            ((second_elf_start <= first_elf_start) and (first_elf_start <= second_elf_end))
        ):

            overlapping += 1
    
# Present the result!
print(overlapping, file=sys.stdout)