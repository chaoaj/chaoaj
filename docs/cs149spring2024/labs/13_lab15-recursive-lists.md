# Lab 15 - Recursion Lab

Your goal is to write a function that can add all integers in a list. Sounds simple enough, right?

Here's the catch: the list can contain integers, or other lists. Those lists can contain integers or other lists, and so on and so on.

**Hint:** Start by writing code to sum up integers in a regular list (using a loop). Then, think about what you need to do differently if an item is a list vs. an int.

```python
def add_all(nums):
    """Add all the integers in the given list, recursively.
    The list may contain ints and/or other lists containing ints/lists.

    Args:
        nums (list): A list of ints and/or other lists containing ints/lists.

    Returns:
        (int): The sum of all the integers in the given list.
    """
```

More Practice - code the following recursive algorithms:

## bunny_ears
We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

Example Test calls:

bunny_ears(0) → 0

bunny_ears(1) → 2

bunny_ears(2) → 4

## triangle
We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.

Example Test calls:

triangle(0) → 0

triangle(1) → 1

triangle(2) → 3

## sum_digits
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example Test calls:

sum_digits(126) → 9

sum_digits(49) → 13

sum_digits(12) → 3

## count8
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example Test calls:

count8(8) → 1

count8(818) → 2

count8(8818) → 4
