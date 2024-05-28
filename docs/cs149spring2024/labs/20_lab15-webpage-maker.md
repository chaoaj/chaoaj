# Lab15 - Web Page Maker

## Introduction
<a href="https://www.w3schools.com/html/default.asp" title = "W3 Schools HTML page">HTML</a> is a markup language used to create web pages.

The goal for today’s lab is to practice working with loading info from a file then writing out an html page.

A basic HTML page will start with a doctype, then html and body tags.  Inside the body tag is the content of the webpage. Heading tags are used for large headings and paragraph tags are used for page content.  The strong tag is used to indicate bolded text.
Here is a sample HTML page:
<pre>
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
</pre>

## File Loading / Reading in the data

Download the following file:

[tags.txt](http://w3.cs.jmu.edu/chaoaj/cs149/tags.txt)

This file will contain a tag then a comma to separate the tag from the content inside the tag.

Your first step is to load in the content The next step is to add functionality to bounce.py enabling it to read a file containing ball descriptions. The name of the file will be provided as a command line argument. For, example, the file [three_balls.dat](../lab15/three_balls.dat) contains the following three lines:

File contents:
<pre>
h1, This is a Heading
p, This is a paragraph
strong, This is a bolded sentence.
link, http://wwww.jmu.edu/
</pre>


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
