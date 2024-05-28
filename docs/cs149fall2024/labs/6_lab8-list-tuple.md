#Lab 8 - List-Tuple Lab

##Introduction

In this lab you will gain some practice with lists and tuples.
[Docstring Guide](https://w3.cs.jmu.edu/cs149/info/docstyle/)

============
##Problem: ASCII Art Roses

Long ago, before computers could display high resolution graphics on 4K monitors with 300 dpi pixel density and churn out stunning real-time 3D graphics at 60 frames per second, many people spent a lot of time making art on computers out of text using the ASCII character set.

Like this:
<pre>.........................................
...####...####....###...##..##...####....
..##.....##........##...##..##..##..##...
..##......###......##...######...#####...
..##........##.....##.......##......##...
...####..####.....####......##....###....
.........................................
</pre>

You are going to write a program to output five ASCII art roses. Like this:

<pre>     @--&gt;----&gt;---
      @-----&gt;-&gt;--
@-----&gt;-------&gt;--
  @-&gt;-&gt;----------
           @-&gt;-&gt;-
</pre>

Each rose starts with an @ followed by a section of dashes - before the first thorn >, followed by a second section of dashes to a second thorn, followed by a final section of dashes -.

For your first pass at this algorithm, you should have five variables: rose1, rose2, rose3, rose4, and rose5. Each variable should refer to a tuple with 3 integers denoting the number of dashes ('-') in each of the rose’s sections. For example, the first rose in the figure above has two dashes in the first section, four dashes in the second section, and three dashes in the final section, so its tuple representation is (2, 4, 3).

Your code should use the variables rose1, rose2, rose3, rose4, and rose5 to output each rose, one per line. The roses should be aligned so that their right-hand sides line up and the longest rose has no spaces before its petals (the '@'). Any rose shorter than the longest rose should have an appropriate number of spaces before the '@'.
Here is starter code:

<pre class="sourceCode python"><code class="sourceCode python"><a class="sourceLine" id="cb1-1" title="1"></a><span class="co">""" Rose Variables """</span>
<a class="sourceLine" id="cb1-2" title="2"></a>rose1 <span class="op">=</span> (<span class="dv">2</span>, <span class="dv">4</span>, <span class="dv">3</span>)
<a class="sourceLine" id="cb1-3" title="3"></a>rose2 <span class="op">=</span> (<span class="dv">5</span>, <span class="dv">1</span>, <span class="dv">2</span>)
<a class="sourceLine" id="cb1-4" title="4"></a>rose3 <span class="op">=</span> (<span class="dv">5</span>, <span class="dv">7</span>, <span class="dv">2</span>)
<a class="sourceLine" id="cb1-5" title="5"></a>rose4 <span class="op">=</span> (<span class="dv">1</span>, <span class="dv">1</span>, <span class="dv">10</span>)
<a class="sourceLine" id="cb1-6" title="6"></a>rose5 <span class="op">=</span> (<span class="dv">1</span>, <span class="dv">1</span>, <span class="dv">1</span>)
<a class="sourceLine" id="cb1-7" title="7"></a>
<a class="sourceLine" id="cb1-8" title="8"></a><span class="co">""" Your code here """</span></code></pre>

##Hints

- Can you calculate the length of rose 1 using the data in rose1?
- Can you put the lengths of all five roses into a list? If so, can you use list functions to find the length of the longest rose?
- Remember that you can multiply a string by an integer to duplicate it. So "abc" * 3 is "abcabcabc".
- To right justify a string you can use the rjust method.

Submit your roses.py file to Gradescope.

This lab was originally created by Nathan Sprague.
