# Lab15 - Files

## Introduction
[Pygame](https://www.pygame.org/) is a Python library that makes it possible to program simple 2-D games and animations. In this lab we will modify a simple bouncing ball simulator to add file load and save functionality.  On your home computer you may need to install the module pygame via: python3 -m pip install pygame
 
A second goal for today’s lab is to practice working on the Linux command line. DON’T START THONNY. For today, we’ll be using nano as our text editor and we will run our code from the terminal.

## Bounce

Download the following file and open it in nano. (Pay close attention to where the file is being saved!)

[bounce.py](http://w3.cs.jmu.edu/chaoaj/cs149/bounce.py)

When you start nano, make sure to use the -ET4 flag. This tells nano to insert four spaces when you hit the tab key. Otherwise it will introduce tab characters into your Python code, which is bad. For example:

<pre>
spragunr@l25002:~/bounce_lab$ nano -ET4 bounce.py
</pre>

Take a few minutes to look over the existing code to get a feel for how it works. Assuming you are in the same folder, you should be able to execute bounce.py as follows:

<pre>
spragunr@l25002:~/bounce_lab$ python bounce.py
</pre>

Try editing the file to change the initial position, size or color of the bouncing ball.

## File Loading

The next step is to add functionality to bounce.py enabling it to read a file containing ball descriptions. The name of the file will be provided as a command line argument. For, example, the file [three_balls.dat](../lab15/three_balls.dat) contains the following three lines:

<pre>
100 20 5 100 0 0
200 20 10 0 150 0
400 20 15 0 0 200
</pre>

Each line describes a single ball with the format:

<pre>
x_position y_position radius red green blue
</pre>

You’ll need to complete the load_game method in the BounceGame class. That method should then be called from the existing main function.
In order to read the command line argument you’ll need to import the sys module from the Python standard libraries:

<pre>
import sys
</pre>

After the necessary modifications, it should be possible to execute bounce.py as follows:

<pre>
spragunr@l25002:~/bounce_lab$ python bounce.py three_balls.dat
</pre>

If everything is working correctly, three balls should appear on the screen with the appropriate sizes and colors. Here is another data file that you can try: [many_balls.dat](../lab15/many_balls.dat).

============

## File Save (If Time)
We also want to be able to save the state of the game so that when the program is restarted, all of the balls will appear at the same locations as they were when the game was saved. Add a save_gamemethod to BounceGame and modify the run method so that the save method will be called when the user presses s. By default, the file created should be named saved.dat.

Once this is working, modify the program so that saved.dat is opened by default if no command line argument is provided. In other words, this would open three_balls.dat:

<pre>
spragunr@l25002:~/bounce_lab$ python bounce.py three_balls.dat
</pre>

This would open saved.dat:

<pre>
spragunr@l25002:~/bounce_lab$ python bounce.py
</pre>

There is nothing to submit for this lab.