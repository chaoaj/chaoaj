#Lab - Haiku lab

<a href="https://commons.wikimedia.org/wiki/File:Haiku-dikt.jpg" title="Östasiatiska museet, CC BY 4.0 via Wikimedia Commons"><img alt="Haiku-dikt" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Haiku-dikt.jpg/128px-Haiku-dikt.jpg" width="128"></a>

## Background
Haiku's are a form of Japanese poetry.  They consist of 3 lines of text.  The first line of the haiku must contain 5 syllables.  The second line must have 7 syllables.  Finally, the third line again contains 5 syllables.
Here is an example of a valid haiku:

An old silent pond

A frog jumps into the pond—

Splash! Silence again.

by Matsuo Basho
 
============

## Objectives

- Practice if-else and conditionals.
- Practice with functions
- Practice using a helper function
- Practice with loops
- More practice with lists


## Program the Solution - First Function:

Write a program called **haiku_checker.py** that contains two functions.
The first function will be a helper function that is called check_n_syllables.  This function must take input of a list of words on a line and an int number of syllables to validate.  You may use the pysyllables library to make this easier https://pypi.org/project/pysyllables/](https://pypi.org/project/pysyllables/). You will need to install the pysyllables  package through the Thonny package manager. Make sure you also do an import at the top of your file:

<pre>from pysyllables import get_syllable_count</pre>

You can then use the get_syllable_count(word) function to get the number of syllables in a word.
The return value of the function should be as follows:

- This function should return either a -1 if the total syllables is less than the given number n to validate,
    
- 0 if the total syllables is equal to the number n,
    
- and 1 if the total syllables is greater than n.


## Second Function:

The second function should be called validate_haiku.  It will take a single parameter of a list of lists. The list will contain 3 lines for the haiku.  Each line will be a sub list of the words in the line. The function will return a String value. 

The return values should follow these rules:

- It should be set to "Valid haiku." if this is a valid haiku that has a first line with 5 syllables, second line with 7 syllables, and third line with 5 syllables. 
    
- If it has more or less than 3 lines it should return: "Invalid haiku, not 3 lines.". 
    
- Otherwise it will return a message with the type of error for each line.  For example: if the first line has 7 syllables it would return: "Line 1 too short. "[note the space after the period].  If the second line has 3 syllables it would return "Line 2 too short. ".  If the third line is too long it would return: "Line 3 too long. ". 

Your program should allow multiple comments, for instance 1 for each line that is wrong.  The overall message should be on a single line of output.  Do not return an error if a line is valid.  Note: You should have a return at the end of each error message and only return one continuous String with all error messages as the final return String.

## Submission:
Submit your program called haiku_checker.py to [https://gradescope.com](https://gradescope.com) by tomorrow evening.