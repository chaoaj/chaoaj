#Lab 6  If-then-else CSCard Lab

##Introduction

============

We will be expanding on the use of submissions and testing via https://gradescope.com.
Collaboration: You are encouraged to work with another student to complete this lab. Each of you should submit your own copy of the code. It's okay if your files are similar or identical, as long as both of your names are present at the top.

##Objectives
Practice validation and if-else-if statements.
More gradescope submission practice.


##Part 1: Understand the Problem
Write a program to prepare the monthly charge account statement for a customer of CS Card International, a credit card company. The program should take as input the previous balance on the account and the total amount of additional charges during the month. It should then compute the interest for the month, the total new balance (i.e., the previous balance plus additional charges plus interest), and the minimum payment due.

- The **interest** is $0 if the previous balance was $0.00 or less. If the previous balance was greater than $0, the interest is 2% of the total owed (i.e., previous balance plus additional charges).EXAMPLE: If the previous balance is $50.00 and the additional charges are $50.00, the interest would be $2.00. But if the previous balance is $0.00, the interest is $0 no matter what.

The **minimum payment** based on the table below:
             $0.00          for new balance less than $0
     new balance        for new balance between $0 and $49.99 (inclusive)
           $50.00          for new balance between $50 and $300 (inclusiive)
    20% of the new balance  for new balance over $300

EXAMPLE: If the new balance is $38.00 then the person must pay the whole $38.00; if the balance is $128 then the person must pay $50; if the balance is $350 the minimum payment is $70.

Make sure you understand the calculations before trying to program. Write the algorithm in pseudocode on paper, and test your algorithm with some examples to see how it works.

============
##Part 2: Program the Solution
Much of the solution including output formatting has already been done for you. Use the variables provided and keep all output statements exactly as they are.
Download a copy of [credit_card.py](https://w3.cs.jmu.edu/chaoaj/cs149/labs/lab06/credit_card.py) as a starting point. Fill in the Docstring comment for credit_card.py.

Get the provided code to run. Write  the calculation portion and min payment portion, returning bogus values for interest and minimum payments for now.

Using the variables provided, code the input statements as described in credit_card.py. You must ensure that the program will not crash if the user enters a bad value.(values must be greater than -5000 and less than 5000 or it should return a 0)

Code the rest of the program as if the two calculations were finished, and then test your program. You should see that the code properly reads in a value for the balance and additional charges and outputs the values in the correct format. (The numbers should be wrong until you finish your coding.)

For each calculation (interest and minimum payment), you should code the proper solution.

Think about test cases. Test the program with a variety of data. Include positive balance, negative balance, and 0 balance.

When you are sure that your code is working properly.  Make sure the output still looks okay.

