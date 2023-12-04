"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
import os

file_path = os.path.join("3", "source.txt")
with open(file_path, "r") as file:
    schematic = file.readlines()


def find_nums():
    nums = {}
    for i, row in enumerate(schematic):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                k = 1
                while j + k < len(row) and row[j + k].isdigit():
                    k += 1
                num = row[j : j + k]
                nums[num] = {"row": i, "col_start": j, "col_end": j + k}
                j += k
            else:
                j += 1
    print(f"all nums: {nums}")
    return nums


def is_symbol(char):
    return not char.isdigit() and char != "."


def valid_num(row, start, stop):
    coordinates = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(start, stop):
        for c_row, c_col in coordinates:
            if (
                (0 < row + c_row < len(schematic))
                and i + c_col < len(schematic[row])
                and is_symbol(schematic[row + c_row][i + c_col])
            ):
                return True
    return False


def part_1():
    valid_values = []
    coordinates = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for num, coordinates in find_nums().items():
        row = coordinates["row"]
        start = coordinates["col_start"]
        stop = coordinates["col_end"]
        if valid_num(row, start, stop):
            valid_values.append(num)
    print(sum(map(int, valid_values)))


part_1()
# # find_nums()
# 304925 too low
