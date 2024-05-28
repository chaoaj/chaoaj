#Lab11 - While loops - Magic 8-Ball

<img alt="Magic 8 ball" src="http://the-chaos.com/alvin/cs149spring2023/labs/lab-13-eight-ball/EightBall.jpg"></a>

## Background
We have already worked with if statements to detect invalid input. But in some cases users will repeatedly enter the wrong value. In addition, some problems lend themselves to executing the program repeatedly. This lab will explore these uses of loops in Python.

## Obectives
- Use a loop structure for error correction.
- Use a loop structure for execution control.

## Part 1: The Magic 8-Ball

The [Magic 8-Ball](http://en.wikipedia.org/wiki/Magic_8-Ball) is a toy produced by Tyco Toys (now Mattel) and consists of a ball filled with a blue fluid. Suspended in the fluid is a icosahedron (a 20-sided polyhedron with each side consisting of an equilateral triangle). Each face has an answer to a yes/no question. 

1. Download the [eightball.py](https://w3.cs.jmu.edu/chaoaj/cs149/eightball.py) program then implement the required helper functions:

- input_yes_no(prompt)

This function is simpler than the previous input functions you have written. Display the prompt (followed by "[yes/no]: "), read the next line of user input, and return true if it's "y" or "yes" ignoring case.


- get_question(prompt)

This function should keep prompting the user to enter a question until they enter a valid one. Question strings must be between 1 and 60 characters, and they must end with a question mark. If the question is invalid, display the applicable error message:
- "Your question is blank"
- "Your question is too long"
- "Your question must end with a ?"

After completing the helper functions, be sure to test the program multiple times with different inputs. Here is an example of what it will look like:

<pre>
Magic 8-Ball

Do you want to ask a question? [yes/no]: yes
What is your question? Will I win the lottery
Your question must end with a ?
What is your question? Will I win the lottery?

Question: Will I win the lottery?
  Answer: Signs point to yes.

Do you want to ask a question? [yes/no]: no
Goodbye!
</pre>

Your final version should allow you to keep asking questions until you enter the word no, and it should verify that each question is at most 60 chars ending with a question mark.


============


## Submission
Submit your completed eightball.py file to https://gradescope.com [https://gradescope.com](https://gradescope.com) by tomorrow evening.