#Lab 7 - Circle Lab - Writing and Calling functions

##Introduction

============

We will be expanding on the use of submissions and testing via https://gradescope.com.
Collaboration: You are encouraged to work with another student to complete this lab. Each of you should submit your own copy of the code. It's okay if your files are similar or identical, as long as both of your names are present at the top.

##Objectives
- Create a program with only functions.
- Stub out so the functions can be written and tested incrementally.
- Become more familiar with the math module in Python.
- Document return types

##Key Terms
**return type**
The data type the function returns.

**return value**
The value that the function returns via the return statement.

**function stub**
An empty or incomplete function that returns 0, "", false, etc.


##Part 1: Creating Stubs
We are going to create a small program to carry out some geometric operations. Note that Python is a loosely typed language so return value types should be specified in :return docstring comments.  It will include a couple of utility functions to make input and printing easier, as well as the calculation of the area of a circle and the volume of a sphere. (Normally, you would design one program to do the geometry and another one to deal with the utility functions, but for today's lab we are putting them together in one program.)

1. Download and open the [circle_driver.py](https://w3.cs.jmu.edu/chaoaj/cs149/circle_driver.py) program. Do not be concerned with what it contains just yet.
2. Create a new source file, circle_play.py.  Create the top level docstring comment including your name and today's date and honor code statement.
3. Define each of the following functions:
    - print_greeting will simply print some lines to greet the user upon running the application. 
    Create a function stub using the following header:
    def print_greeting()
    This header says that the function is named print_greeting, and accepts no parameters.
    Create function documentation. In this case you only need to describe what this function will 
    do.

    - enter_radius - create a function header that looks like this:
    def enter_radius()
    This header says the function is named enter_radius, and accepts no parameters.
    Add function documentation for this function as follows: (note the use of the :return label)
```
    """
     Displays a prompt to the user, then reads in a float value
     that the user has entered.
 
     Returns:
     (float): a float value representing a radius
    """     
```

- Create the function block, and add in a single return statement, return -999.0 This is a
"stubbed" return statement that returns a value of the correct type, but is not the value we 
will eventually need.

- calculate_area - This function will calculate the area of a circle with a given radius.
    Create a function header named calculate_area and has a single parameter, a float value
    representing a radius.
    
    Create the function block with a return statement to return the value -888.0. (These ar 
    meaningless values, but if we call the function and its not done, we'll know that by the return
    value.) Add your documentation including a :param tag.

- calculate_volume - This function will calculate the volume of a sphere with a given radius.
    Create a function header, function block, return statement, and documentation. The stubbed
    return value should be -777.0.

4. Save your work at this point, *before implementing any of the functions*. You should not have any errors. If you do, check to make sure that each function in circle_play is created exactly as described above.

5. Run circle_driver from Thonny or using the command line. What output do you see? Does it make any sense?

Now we will begin to fill in our stubbed functions.

============

##Part 2: Creating a Void function With No Parameters

Begin with print_greeting, which should print the following. (Note that < blank line > just means that you should print a newline there.)

Welcome to the CS149 Circle Calculator

< blank line >

This application will calculate the area of a circle and/or volume of a sphere.

< blank line >

1. Create the code to print these four lines. Run it from the command line.
2. You are currently testing the 1st function, so pass the argument 1 to the main function as follows:
3. python3 circle_driver.py 1
4. Does your greeting print correctly? Make any corrections that you need before moving on.

*Explanation*: The circle_driver is designed to let you test each of your functions separately. In this case, you have built a single function, so you are testing just that function. The function stubs enable you to run the entire program, but then just fill in the parts that you are ready to complete and test. By testing individual functions, you can focus on getting that function written correctly before moving on to the next one.

##Part 3: Creating a Value Returning function With No Parameters

Next you'll fill in the enter_radius function. This function displays a standard prompt, "Enter the radius: " and then reads in the radius from the user input.

1. Output the prompt "Enter the radius: ". The cursor should remain on the same line, one space to the right of the colon and read the value the user enters into a radius variable.
2. Change the return statement to return the value that the user enters.
3. Test your program on the command line running python3 circle_driver.py 2. This time enter the number 2 as the command line argument. What happens?

##Part 4: Creating Value-Returning functions With Parameters
Finally, you will fill in each of the calculation functions. You are going to calculate the area of a circle and the volume of a sphere. The area of a circle is defined as A = π r 2. The volume of a sphere is V = 4/3 π r 3. Use these formulas to come up with a few test cases for each function.

1. Write down your examples on a piece of paper, so you can be sure your code works as expected.
2. Begin with the calculate_area function. You may find that the math module is helpful for this step. First, there is a constant defined in that module called pi. Since the constant is in another module, we must use the qualified name math.pi to access it.
3. Define the variables that you will need.
4. Create the calculation, using math.pi for π.
5. Instead of the stub value in your return statement, return the area that you calculate.
6. Test your work passing the number 3 in for the command line argument.
7. Check your area values against the ones that you calculated by hand. Work with your function until it runs correctly.
8. Create the calculate_volume function and test as before using command line argument 4 to test your volume function.
9. Finally, test the entire application running the application with no arguments. It should run each function in turn.

Upload your completed circle_play.py program to [Gradescope](https://gradescope.com). To receive full credit for this assignment, all 4 functions must work correctly. You will not receive full credit for this lab unless your code passes all of the automated formatting tests.

```
Testing Greeting
Welcome to the CS149 Circle Calculator

This application will calculate the area of a circle and/or volume of a sphere.

Testing Input
Enter the radius: 5
Enter the radius: 10
Enter the radius: 15
The values you entered were: 
5.0 	
10.0 	
15.0 	
A circle of radius 5.0 has area of 78.53981633974483
A circle of radius 10.0 has area of 314.1592653589793
A circle of radius 15.0 has area of 706.8583470577034
A sphere of radius 5.0 has volume of 523.5987755982989
A sphere of radius 10.0 has volume of 4188.790204786391
A sphere of radius 15.0 has volume of 14137.166941154068    
```
This lab was originally created by Nancy Harris and modified by Nathan Sprague.
