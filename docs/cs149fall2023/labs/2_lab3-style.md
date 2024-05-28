##Lab03: Style guide and pep8

![Code Quality](../labs/lab03/code_quality.png "I honestly didn't think you could even USE emoji in variable names. Or that there were so many different crying ones.")   
Source: [https://xkcd.com/1513/](https://xkcd.com/1513/)

### Background

PEP8 - Python Style
-------------------

When writing in English, readability can be impacted by the way the text is laid out on the page. We use conventions, like indenting the first sentence of a paragraph, to make it easier to understand written text. Programming languages are the same. Programs are easier to read if we agree on a set of conventions for how the code should be formatted. [PEP 8](https://www.python.org/dev/peps/pep-0008/) is the official document that describes the standard formatting conventions for Python code. (Here is a prettier version: [https://pep8.org/](https://pep8.org/).) You don’t need to read and understand the full PEP 8 document now, but you may want to look it over to get a feel for the issues that it addresses. Instructions for [installing Thonny and flake8 configuration](https://w3.cs.jmu.edu/cs149/info/thonny/)

Comments
--------

When writing your programs it is helpful for us if you include the assignment name, a description of the assignment, your name, the due date and an Honor Code statement to let us know where you got help from on the assignment.  These should be done in a block at the top of your program that looks like this:
<pre>
"""  
Lab 03- Style lab - fixing styles and testing online grading tool submission.  
Author: Alvin Chao  
Version: 1-26-22  
Honor Code: I got help on the output statements for the lab from TA John  
""" 
</pre>

### Part 1

### Running flake8 Through Thonny

When you submit homework assignments for CS 149 they will automatically be checked against the PEP 8 formatting requirements using a tool named `flake8`. You will only receive full credit if you pass all of these automated style checks. You can install `flake8` in Thonny by selecting _Tools -> Manage Packages…_ and then finding and installing `flake8` as well as `pep8-naming`. After installation, you should be able to check your file by typing the following into the Thonny shell:

    >>> !flake8 payroll.py

The exclamation point tells the Python interpreter the command should not be interpreted as Python code.

Note that the Gradescope autograder is configured to be slightly more lenient than the default settings for `flake8`. We allow line lengths up to 100 and disable checks for some errors and warnings. If you want to run `flake8` with exactly the same settings as Gradescope, you can copy the following file into the same directory as your python code:

*   [setup.cfg](https://w3.cs.jmu.edu/cs149/info/setup.cfg)

### Part 2

### Example Program

If you haven't already, you should create a top-level `CS149` folder to organize all your labs and other assignments for the semester. Then create a `lab03` folder for today's lab. (If you logged in as `student` today, please log out and log back in with your own account.)

1.  Download: [payroll.py](https://w3.cs.jmu.edu/chaoaj/cs149/labs/lab03/payroll.py)
    \>>> !flake8 payroll.py
3.  You should see the following errors:

<pre>
payroll.py:1:27: E231 missing whitespace after ','  
payroll.py:5:43: E251 unexpected spaces around keyword / parameter equals  
payroll.py:6:2: N816 variable 'payRate' in global scope should not be mixedCase  
payroll.py:7:2: N816 variable 'grossPay' in global scope should not be mixedCase  
payroll.py:9:2: N816 variable 'grossPay' in global scope should not be mixedCase  
payroll.py:9:9: E225 missing whitespace around operator  
payroll.py:11:39: W292 no newline at end of file
</pre>
Fix all style errors by repeatedly running flake8 and submit to Gradescope when your file checks all style issues.

_Submission:_ At the end of class today, or by 11:00 PM tomorrow if you would like more time, submit a corrected version of payroll.py via [Gradescope](https://www.gradescope.com/) . Your code must pass flake8 style without any warnings **AND** meet all the requirements outlined below. (It must also compile and run correctly; don't change the program's behavior.)  If you cannot get this working in Gradescope you may upload to Canvas, but points will be deducted.

_Collaboration:_ You are encouraged to work with another student to complete this lab. Each of you should submit your own copy of the program. It's okay if your files are similar or identical, as long as both of your names are present at the top.

#### A. Comments

\# An inline comment must contain only one # and a space after it.

"""
 \*Block comments should end with the closing statement on its own line.
"""

#### B. Names

1.  All names should be descriptive and readable. (`sub_total` rather than `s`,  `grade` rather than `grd`)
2.  Multiple-word names should use underscores to separate words. (`sub_total` not `subTotal`)
3.  Variable and method names should begin with a lowercase letter, and:
    *   Variable names should be nouns or noun phrases. (`student_name` or `sub_total`)
    *   Function names should be verbs or verb phrases. (`print_line` or `add_column`)
4.  Class names should begin with a capital letter and use title or CapWords case. (`HelloWorld`)
5.  Constant names should be all caps with an underscore separator. (`PI` or `INTEREST_RATE`)

#### C. Declarations
<pre>
CENTIMETERS\_PER\_INCH = 2.54
centimeters = inches \* CENTIMETERS\_PER\_INCH    // NOT inches \* 2.54
</pre>
1.  1.  All constants should be named and initialized at the top of the function in which they are used.
    2.  All variables should also be declared at the top of the function, directly after any constant declaraions.

#### D. Literals

1.  Numeric literals should be of the correct type for the context in which they are used.

\# integer expressions should use integer literals like a
a = 2  
\# double expressions should use double literals like b  
b = 2.0

<pre>average = (x + y) / 2.0    # NOT 2, which is an integer</pre>

#### E. Indentation

1.  Subsections of code should be indented consistently with four spaces per Python requirements.
2.  Always use four space characters, not tab characters, for indentation.
3.  Statements too long for one line should be indented on subsequent lines.

#### F. Whitespace

1.  There should be a space after commas, and #'s.
2.  Use whitespace to separate logical segments of code. There should be a blank line after variable declarations.
3.  Lines should be kept to a short length (< 80 - 100 chars). You should be able to see the full line in your text editor.
4.  Binary operators should be separated from their operands by a single space. (`sum = my_grade + your_grade`)
5.  Unary operators should not be separated by a space. (`my_grade++`)
