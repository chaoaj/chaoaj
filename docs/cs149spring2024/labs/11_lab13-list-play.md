# Lab13 - List Play - Processing list elements

<img src="http://the-chaos.com/alvin/cs149spring2023/labs/lab-14-die/dice.png" alt="dice image">

## Background
You will write today's program from scratch. Create a new Python program named list_play with a main method. For each step below, you should add code to the program without replacing prior code. When you are finished, this program will provide you with a reference for working with lists/arrays including initializing, printing, and comparing.

## Objectives
    - Use a list to store a sequence of values.
    - Display the contents of an list with a loop.
    - Practice manipulating various types of lists.

## Key Terms
- initializer list
    list of values used to instantiate and initialize an array in one step
- len(list)
    Returns the number of elements in a list
    
- subscript
    integer value in brackets [ ] that specifies an element of an array/list

- ArrayIndexOutOfBoundsException
    error raised when trying to access A[i] where i < 0 or i >= A.length

## Part 1: Sequentially accessing an array
Whenever you are asked to do something to your array and then print it, you should finish the update step first and then have a separate loop to do the printing.
1. Create a function called part_one() that creates a single array of integers that is 6 elements long you can initialize zero values for the initial array.
2. Initialize each of the array elements to the value -1 using a loop of your choice.
3. In another loop, save each element of the array into a string with newlines at the end as shown:
   <pre>
    array[0] = -1
    array[1] = -1
    ...
   </pre>

4. Add code to change the value of each element of the array to its subscript. For example, array[3] should hold the value 3.
5. Store the new contents of the array into the return string. You may copy and paste the code from step 3. 
6. If you have not seen a list index out of range error, make one by causing a loop to read past the end of the array. What happens?
7. Fix the code that causes the list index out of range. Then add code to re-initialize
8. Your function should return the final return string value(see expected FINAL OUTPUT section below for how this will look if you print the contents of part_one return string.

## Part 2: Randomly accessing an array
1. Create a function called dice_roll(seed).  This function will take in a see value for the random module and return a dice roll value of 1-6. Don't forget to import random at the top of your program to use the random module. You should check that your seed is not None as well.
2. Create a function called part_two().  This should:
    1. Create an array of 6 int values [0, 0, 0, 0 ,0 , 0]
    2. Create a loop that will iterate at least 25 times. In the loop body:
    3. Roll the die. (using the dice_roll method in #1 above where the seed value sent is the index value of the loop for the 25 time 0-24)
    4. Based on the result of the roll, add up the corresponding cell of your array. The value of each array element should be the number of times that roll is made.

3. After the loop finishes, print the results of the simulation. For example, the final array should be: [2, 8, 4, 4, 4, 3] you would output:
<pre>
1 was rolled 2 times.
2 was rolled 8 times.
...
</pre>
see the FINAL OUTPUT below for how this should be formatted with double return statements at the end and return this output as a return string for the function.

## Part 3: Working with multiple arrays
For this exercise, you will need two arrays of double values.
Create a main section that sets up the two arrays like this:
<pre>
print("Before")
a1 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
a2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
print(store_array_values(a1, a2))
change_array(a1, a2)
print("After")
print(store_array_values(a1, a2))
</pre>
1. Write the first function store_array_values(a1, a2) which will take the two arrays as input then return an return string of the values of the arrays. See the FINAL OUTPUT section below for how this is formatted.
2. Write a second function change_array(a1, a2): This will change the values of the array as follows: 
    1. Write a loop to change all values of a2 to those in a1.
    2. Finally, change the index 0 element of the first array(a1) to 99.0 and the index 5 element of the second array(a2) to 99.0.

3. Check that the contents of the two arrays are indeed different after calling your change_array function. If not, make the appropriate corrections.  Check all output with the lab14.exp expected output below.
 
## FINAL OUTPUT
Here is the expected output file for [lab13.exp](../lab13/lab13.exp)
Submit your final list_play file to https://gradescope.com.