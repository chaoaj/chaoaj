# Programming Assignment(PA) 1: Poker Dice
![Poker dice](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Dice%2C_game_%28AM_2015.20.16-2%29_%28cropped%29.jpg/290px-Dice%2C_game_%28AM_2015.20.16-2%29_%28cropped%29.jpg)


## Introduction
Poker dice is a dice game similar to Yahtzee played with 5 six sided dice with face values
9, 10, J, Q, K , A.

<!--A playable online version for understanding the problem is located here:
* <a href="http://the-chaos.com/cgi-bin/chuck-a-luck.cgi">Chuck-a-Luck online</a>
-->

The following table represents a summary of the rules for Poker Dice scores:

Type# | Category         | Description                                    | Scoring
----- | ---------------- | -----------------------------------------------|--------------
1     |  One Pair        | A pair of the same face value 9, 9, 10, J, K   | Sum of Matched Values
2     |  Two Pair        | Two unique pairs of face values 9, 9, 10, 10 K | Sum of both pair values
3     |  Three of a Kind | At least Three of the same face value          | Sum of three Similar Dice + 10)
4     |  Four of a Kind  | At least Four of the same face value           | Sum of four similar Dice + 20
5     |  Five of a Kind  | All five face values are the same              | 100 points
6     |  Full House      | 3 of a kind and a pair 9, 9, 9, A, A (unique face values)   | 50 points + sum of dice face values
7     |  Small Straight  | 4 or more face values in a row                 | 70 points
8     |  Large Straight  | All 5 dice sequential 9,10,J,Q,K or 10, J, Q, K, A  |  95 points
9     |  Chance          | Any roll                                       | Sum of dice face values

The final column in the table describes the score if the player chooses the corresponding score type. For example, if a player selects one pair and the roll is ['9', '9', 'J','Q','A'], the score will be 18 because score is twice the pair value. If the dice rolled are ['9', '9', 'Q', 'A', '9'], then the payout will still be 18, because no extra points are given for a three of a kind because one pair was the selected score type.

Your goal for this assignment is to create a `dice` module and develop and test a function for determining scoring in Poker Dice.


## Provided Code
Start with the following source files:

* dice.py -- NEED TO CREATE
* [poker_dice.py](pa1/poker_dice.py) -- DO NOT EDIT
* [score_dice.py](pa1/score_dice.py) -- UNFINISHED
* [test_score_dice.py](pa1/test_score_dice.py) -- UNFINISHED

### dice.py

The `dice` module will work with a list of 5 string die face values.  This module will need to work with not just our Poker Dice number of dice (5) but with any number from 1--10 dice.  The module will contain five functions:

1. `roll_dice` -- This function will take two parameters.  The first will be an int for the number of dice in the list.  The second parameter will be a random seed integer, with a default value of 0. Note it is possible to pass None as a parameter, which should result in a random seed value.  This function will return a list of n dice values (each die has a string face value between '9' - 'A'). If the number of dice is out of range 1--10 then a single die of value '9' will be returned as a list of 1 item. If no parameters are provided, then a list of 5 dice values should be returned (having been generated using a seed of 0).

2. `are_valid` -- This function takes a dice parameter which is a list of from 1--10 dice rolls.  This function will check the length of the list to make sure it is between 1 and 10 and check if the values of all dice in the list are between '9' and 'A'.  Return `True` if all these conditions are met, `False` otherwise.

3. `get_value` -- This function takes a string argument and gets the scoring numerical point value of a die face value.
Face values are: 9 and 10 for the numerical string values, 10 for 'J', 'Q', 'K', and 11 for 'A'.

4. `num_faces` -- This function takes a dice_list parameter which is a list of from 1--10 dice rolls.  It will also take a second parameter for the face value being counted, with a default of None.  The function returns a count of the number of times a particular face value shows on the dice in the list. For example, if the dice are ['9', '9','9', 'A', 'K'], `dice.num_faces(dice, 9)` will return 3 (since the value '9' occurs three times). If no parameter is passed (i.e., None) then count should return 0.  Also, if an invalid list or face value of None is passed the function should return -1.

5. `add_values` -- This function takes a dice parameter which is a list of from 1--10 dice rolls. It will calculate and return the sum of the face values of the dice in the list.  Make sure you use the validation function for dice and return a -1 for an invalid list of dice.


### poker_dice.py

This module contains a simple terminal-based Poker Dice game. Once you have completed `calculate_score.py` you can use this driver to try out your code.

This driver will call the `dice.py` module and use the `roll_dice` function to return dice rolls.  It may not be very useful for systematically testing your solution. The main mechanism for running your code for this project will be the `test_calculate_score.py` file described below.

### score_dice.py

Your main task for this assignment is to implement the `score_dice.calculate_score` function according to the provided documentation string. For full credit, your finished function must satisfy the following requirements:

* A nested conditional should be used to distinguish between the different scorign types
* Appropriate helper functions must be used to break the problem into smaller and more manageable pieces.
* The `add_values` and `num_faces` functions from the `dice` module should be used.
* Your code must make use of the named constants(FACES, FACES_LIST) declared at the top of the dice program. Avoid the use of hard-coded literal values in your solution.
* Your score_dice.calculate_score function must have only one return statement.

### test_score_dice.py

You must write unit tests for `score_dice.py`. Rather than writing one very long `test_score_dice` function, you should write several smaller tests to handle distinct cases. The provided file contains two testing functions to get you started.

Notice that the names of these functions describe the situations they are designed to test.
For example, the name `test_calculate_score_one_pair_no_match`:

* test - This makes it clear that this is a testing function
* calculate_score - this is the function being tested
* one_pair_no_match - this is the situation being tested.

You should properly document your tests and your `score_dice.py` file.
Docstrings for test functions are generally not required.

Categories that you should test include (this is a template for your `test_score_dice.py` file):

* Test score one pair no match
* Test score one pair one match
* Test score two pair no match
* Test score two pair one match
* Test score three of a kind match
* Test score three of a kind no match
* Test score four of a kind match
* Test score four of a kind no match
* Test score five of a kind match
* Test score five of a kind no match
* Test score small straight match
* Test score small straight no match
* Test score large straight match
* Test score large straight no match
* Test score chance match


## Part A - Readiness Quiz and dice.py (30 points)

1) Readiness Quiz (10 points) in Canvas.

Before the deadline for Part A you should read this document carefully, then look at the starter code provided above. Once you have a clear understanding of the expectations for this assignment, complete the readiness quiz in Canvas (10 points). The grading for this quiz will be all or nothing: your score on the quiz will be 0 if you miss any questions.

**If you do not successfully complete the readiness quiz, you cannot receive any credit for Part A or Part B.**

2) You should also complete the `dice.py` file (20 pts) and submit this to Gradescope by the deadline for your section.

Be sure to test your `dice` module carefully for correctness AND style before submitting into gradescope; **You will be limited to 10 submissions for Part A code.**


## Part B - Code (70 points)
Upload only your `score_dice.py` file to Gradescope.   You should not include `poker_dice.py` or `test_score_dice.py` in your submission.

Before uploading your submission to Gradescope, be sure to complete the following steps:

* Test your solution carefully.
* Make sure that `poker_dice.py` works as expected with your finished code.
* Review the course style guide to ensure that your code meets the style requirements.
* Run `flake8` and eliminate all warnings.
* Review and update comments as needed.

**You are limited to a maximum of 10 submissions into Gradescope for Part B.**


## Programming Assignment Attribution
Provide a short statement describing any assistance that you received on this assignment, either from another student, an online source, an AI-enabled tool, or any other source.


## Acknowledgments
This assignment was created by Alvin Chao.  Some parts of the Poker dice description above are borrowed from the Poker Dice Wikipedia page. The Wikipedia article, and this assignment page, are licensed under the Creative Commons Attribution-Share-Alike License 3.0.
