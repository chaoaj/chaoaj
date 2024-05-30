"""Produce star patterns demonstrating nested for loops.

Adapted from Lewis and Loftus by Nancy and Arch Harris.
Converted to Python by Alvin Chao
Author: YOUR NAME
Version: DATE
"""


def example(max_rows):
    """First example.

    prints example.

    Args:
        max_rows (int): max rows to print

    Returns:
        pattern(str): string pattern
    """
    pattern = ""
    for row in range(1, max_rows + 2):
        star_count = row
        for col in range(1, star_count):
            pattern += "*"
        pattern += "\n"
    return pattern


def pattern_a(max_rows):
    pass  # Finish this function


def pattern_b(max_rows):
    pass  # Finish this function


def pattern_c(max_rows):
    pass  # Finish this function


if __name__ == "__main__":
    """Main method."""
    max_rows = 0     # maximum number of rows
    star_count = 0   # number of stars per row
    blank_count = 0  # blanks preceding stars
    max_rows = int(input("Enter a positive integer for the number of rows: "))
    while (max_rows <= 0):
        print("\nYou did not enter a POSITIVE number.")
        print(f"You entered {max_rows}!\n")
        max_rows = input("Enter a positive number",
                         "for the number of rows: ")
    # first example: stars per row goes from 1 to max_rows
    print("First Example")
    print()
    print(example(max_rows))
    print()  # space between patterns
    print(pattern_a(max_rows))
    print()  # space between patterns
    print(pattern_b(max_rows))
    print()  # space between patterns
    print(pattern_c(max_rows))

