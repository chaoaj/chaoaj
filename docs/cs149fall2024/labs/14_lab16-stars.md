# Lab16 - Nested Loops (Stars)

![stars](http://the-chaos.com/alvin/cs149spring2022/labs/lab-15/Stars.jpg)

## Background

In the good old days, we didn't have fancy computer graphics. So we had to rely on ASCII artLinks to an external site. and the user's imagination. Today's lab will take you back in time! Your task is to draw various pictures of stars (`'*'`) that require the creative use of iteration and decisions.

## Objectives

- Write nested for loops and decisions.
- Solve counting problems with loops.

## Instructions

- Download [stars.py](https://w3.cs.jmu.edu/chaoaj/cs149/stars.py) open it in Thonny.
- Write your name and today's date in the docstring comment.
- Run the program. What shape does this pattern produce?
- Notice the relationship between the row (outer loop) and the number of stars that are printed.
- Notice the relationship between the col (inner loop) and the place where we move to a new line.
- Add code to your program to create functions for Patterns A, B, and C as shown below.
- The functions should include a parameter max_rows that will give the number of rows to output.

### Pattern A
```
**********
*********
********
*******
******
*****
****
***
**
*
```

The leftmost stars are in the leftmost output column. Test your code with an odd number of stars and an even number of stars.

**HINT**: While developing the code, replace each space with another character that is visible.

### Pattern B
```

         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
```

The leftmost star of the last row is in the first position of the output column.

**HINT**: You used star_count in the original example and Pattern A. You should think about using a blank_count variable as well.

### Pattern C
```
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *
```

The top row, leftmost star is in the first position of the output.

**HINT**: It should be the same as Pattern B, except for the way you calculate blank_count and star_count.


## Generalization

Finish the functions patterns A, B, and C.
If you finish early, work on the following pattern D.

### Pattern D (challenge)
```
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
```
For an odd number of rows, you would only have one middle line. The middle row leftmost star is in the first position of the output.

**HINT**: Consider writing two loops: one for the top half, and another for the bottom half. You may also want to increment and decrement star_count and blank_count, rather than calculate them directly based on the row number.
