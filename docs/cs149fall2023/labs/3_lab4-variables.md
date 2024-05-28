#Lab 4 - Variables 

##Introduction

============

This activity will help you practice some of the concepts from this week and prepare for the homework problems next week.

Specifically you will practice:

*   Converting user input to either a floating point number (float), like 3.14159, or an integer (int), like 314159.
*   Using floating point division (/), integer division (//), and the remainder, or mod, operator (%) in the appropriate situations.

##Problem: Splitting feet into miles, furlongs, and feet.

============

For this problem you are going to write a program called `feet_conversion.py` to use integer division and remainders to take a total number of feet and split it into miles, furlongs, and feet. 1 mile is 5280 feet and 1 furlong is 660 feet (it’s some old English measure nobody uses anymore, but let’s do it anyways!).

Enter a total number of feet: 12345  
  
12345 total feet is 2 mile(s), 2 furlong(s), and 465 feet.

+ **Hint 1:** Figure out how to solve the problem yourself by hand on paper. You can’t code something you don’t know how to solve.

+ **Hint 2:** You need to use integer division // and the mod/remainder % operators.

+ **Hint 3:** You probably want a variable for the remaining feet. For instance, before you’ve figured out the answer above, the remaining feet is 12345. But once you figure out that there are two full miles in 12345 feet (2 full miles is 10560 feet), then the remaining feet you have to deal with in your calculation is 1785 feet. Then how many full furlongs are in 1785 feet? Well, 2 again, since 660×2\=1320. And finally after we remove those 1320 from 1785 the remaining feet is 465.

+ **Hint 4:** Notice how close the words _remaining_ and _remainder_ are.

## Submission:
Submit this to [https://canvas.jmu.edu](canvas/gradescope)