# Lab02: Python Comand Line and Thonny
## Introduction
The goal for this lab is to gain experience editing, compiling and executing Python programs in the terminal and through the Thonny IDE. You may work on this lab individually or in a group of no more than three people.

##Executing Python in the Terminal

<p>Each of the steps below should be completed&#160;<em>entirely inside the terminal</em>: no GUI applications allowed. Refer to the&#160;<a href="https://w3.cs.jmu.edu/spragunr/CS139/activities/unix_tutorial/index.html">Unix Tutorial for Beginners</a>&#160;if you need to learn more about Unix commands.</p>

1. Create a cs149 folder on your desktop<br /> mkdir cs149
2. Move into the cs149 directory:<br /> cd cs149
3. Create a folder inside your home directory named&#160;<code>lab02</code>.<br /> mkdir lab02
4. Move into the lab02 directory:<br /> cd lab02
5. Copy the file <a href="https://w3.cs.jmu.edu/chaoaj/cs149/labs/lab02/welcome.py">welcome.py</a>&#160;by doing a Right-Click Save-As and saving it to your lab02 folder.&#160;
OR here is the code:
<pre>
print ("Welcome to CS149!")
print("It's fun.")
</pre>
cut and paste this into a file called welcome.py and save it in the lab02 folder.
6. Run welcome.py:
  <pre class="cli">$ python3 welcome.py
  </pre>
7. Congratulations! You've successfully executed your first Python program.


## Editing Files in the Terminal
<p>Normally, we will be using an Integrated Development Environment (IDE) to edit and compile Python programs. However, it can sometimes be convenient to edit a file directly in the terminal. There are many terminal-based editors. Today we'll try&#160;<code>nano</code>&#160;because it is easy to use for beginners.</p>

1. Open&#160;<code>welcome.py</code>&#160;using&#160;<code>nano</code>:
<pre class="cli">$ nano welcome.py
</pre>
<p>You should see something like the following:</p>
<img alt="Nano Editor screenshot" height="311" src="../images/welcome.png" width="500" />
<p>The two lines of text at the bottom show the set of actions available in the editor. The "^" symbol indicates the "Ctrl" key. For example, pressing Ctrl-O will "WriteOut" (save) any changes you have made to the file.</p>
2. Edit the file so that the welcome message says&#160;<code>"It's REALLY fun."</code>&#160;instead of&#160;<code>"It's fun."</code>. Save your changes and exit.
3. Try executing your program again:
<pre class="cli">$ python3 welcome.py</pre>
4. You should see the following output
<pre>Welcome to CS149!
It's REALLY fun.
</pre>

## Thonny IDE
## Objectives
* Use an IDE (Integrated Development Environment).
* Edit, save, compile, and run a simple Python program.
* Recognize and correct syntax errors in a Python program.

## Key Terms
<dl>
<dt>source file</dt>
<dd>the Python program as written by the programmer</dd>
<dt>syntax error</dt>
<dd>mistake in the source code that prevents compilation</dd>
<dt>logic error</dt>
<dd>mistake in the program that causes incorrect behavior</dd>
<dt>execute</dt>
<dd>the process of running a program on a computer</dd>
</dl>
##Part 1: Thonny Editor
<p>Thonny&#160; is a text editor designed to simplify the process of editing, debugging and executing Python programs.</p>

1. Open Thonny and click "File &#8211;&gt; Open" from the menu and select your welcome.py file from above.<br /><br /><img alt="thonny editor " class="" height="455" src="../images/thonny.png" width="500" />
2. Press the Green play button on the toolbar to execute the Python file(this is the same<br />thing as running the &gt;&gt;python welcome.py in the terminal.
3. &nbsp;<pre class="java">&gt;&gt;&gt; %Run welcome.py<br />Welcome to CS149!<br />It's REALLY fun.
</pre>
4. Edit the file in Thonny to print another line that prints<br />I have edited a file in Thonny.&#160;
5. Save your results by pressing the Floppy disk icon then run the program again by pressing the Green play button.
6. You have just run and edited a program using Thonny.
## Submission for Lab2
* Via&#160;<a href="https://www.gradescope.com/">https://www.gradescope.com</a>&#160;submit&#160;the Word of the Day in Canvas and your welcome.py file to Gradescope.</li>
<p class="p2"><span class="s1"><strong>Acknowledgments</strong></span></p>
<p class="p3"><span class="s1">This activity is based on a lab developed by Nathan Sprague based on a&#160;lab originally developed by Chris Mayfield.</span></p>
<p class="p1">&#160;</p>