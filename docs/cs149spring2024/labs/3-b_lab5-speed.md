# Lab 5 - Average Speed

## Introduction

============

This activity will help you continue to prepare for homework this week and next week.

Concepts you will practice:

*   Converting user input to either a floating point number (float), like 3.14159, or an integer (int), like 314159.
*   Using floating point division (/), integer division (//), and the remainder, or mod, operator (%) in the appropriate situations.

============

## Average Speed Calculator

For this problem you will write a program named `bike_speed.py` that asks the user for the length of a bike race in miles (entered as a floating point number) and their finishing time for the race in hours, minutes, and seconds and then output their average speed in both miles per hour and kilometers per hour. (1 mile = 1.60934 kilometers). When you output the speed you should show exactly 2 digits past the decimal place.

Here is an example run of the program:
<pre>
= Bike Race Average Speed Calculator =

How many miles did you race? 18.66
How much time did that take you in hours, minutes, and seconds?
  Hours: 0
  Minutes: 43
  Seconds: 49

Your speed was 25.55 mph, which is 41.12 kph.
</pre>

Hint 1: Figure out how to calculate it by hand on paper before you try to code anything. You can’t code what you can’t solve with a pen and paper.

Hint 2: You’ll want to get your time into one unit. Dealing with 3 separate units is not good for computation. At the end of the day, we need to do distance / time in hours to solve the problem, so what is the total time in hours and how do you calculate it? Note that 0 hours, 43 minutes, and 49 seconds is ~0.7303 hours. How do you calculate this? I calculated it by, so how can you do this for other numbers of hours, minutes, and seconds?

Hint 3: Section 2.4 in the reading introduces f-strings for formatting output to a number of decimal places. If you don’t remember how to do it, get it working with any number of decimal places and then fix it when you’ve got the rest working.
## Submission:
Submit this to [https://canvas.jmu.edu](canvas/gradescope)
