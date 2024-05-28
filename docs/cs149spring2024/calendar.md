#CS149 Section 003 Calendar
<h2><!--<p><a href="#Week1" title="Current Week">Current Week</a></p>--></h2>
<p>
<script type="text/javascript">// <![CDATA[
dttest1 = new Date(2024,0,16);
dttest2 = new Date(2024,4,24);

function diff_weeks(dt2, dt1)
 {
  var diff =(dt2.getTime() - dt1.getTime()) / 1000; // diff in secs
  diff /= (60 * 60 * 24 * 7); // convert seconds to weeks
  return Math.abs(Math.round(diff));

 }
// Start of semester - remember JS date month is one less than current.
var dt1 = new Date(2024, 0, 12); // new Date(2023, 7, 17); // January 1 = (2021, 0, 1)
// document.write("dt1" + dt1);
var dt2 = new Date();
// document.write("d2" + dt2);
wk = diff_weeks(dt2,dt1);
// document.write("Week: " + wk);
if (wk >= 16) {
    wk = 16;
}
else if (wk <= 0) {
    wk = 1;
}
document.write("<a href=\"#Week"+wk+"\">Current Week</a>");
document.write("<!-- wk " + wk + "-->");
// ]]></script>

</p>
<p>Python and Config Resources:</p>
<ul>
<li><a href="https://docs.python.org/3/library/index.html" title="Java 10 API">Python 3 Standard Library</a>&#160; &#160;<a href="https://pythontutor.com/visualize.html#mode=edit#mode=edit" title="Java Virtualizer">Python Tutor</a>&#160; <a href="https://w3.cs.jmu.edu/bernstdh/web/SMYC/index.html">Show Me Your Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Unicode_characters" title="Unicode character list">Unicode Character List</a>&#160;&#160;<a href="https://docs.python.org/3/library/string.html#format-specification-mini-language">print formatting reference</a>&#160;&#160;<a href="https://docs.python.org/3/library/math.html">Math Module</a><br /><a href="https://w3.cs.jmu.edu/cs149/info/thonny/" title="Thonny/pep8">Thonny-Pep8</a></li></li>
<li><a href="https://docs.python.org/3/tutorial/datastructures.html">List Methods</a>&#160;&#160;<a href="https://www.w3schools.com/python/python_ref_dictionary.asp">Dictionary Methods</a>.&#160; <a href="https://www.w3schools.com/python/python_ref_set.asp">Set Methods</a></li>
<li><a href="https://w3.cs.jmu.edu/cs149/info/docstyle/">Docstring Style Guide</a></li>
<li>Main program: <br/>if __name__ == "__main__":</li>
</ul>

<div>(<strong>Note: This schedule is tentative and is subject to change during the semester</strong>) <br /><br /><a href="/cs149spring2022/labs/lab-02/index" title="Lab 2A+B"></a></div>


| Week | Date | Reading | Topic | HW / Programming Assignment | Events |
| --- | ---------- | --------- | ------- | -------------- | --------------------------- |
| <a name="Week1"></a> Week 1  | 1/16/24 |  | [Intro to CS149](https://docs.google.com/presentation/d/1XN88WHhstYMgwv8I58yB8SMPG3h-DPBVO4y_3ZG2rYc/edit#slide=id.g3d9ea2233c_2_79)<br/><br/> [Intro Python Lecture 2](https://docs.google.com/presentation/d/1y_WXgiiCCwwXaPHo3yzyrolP4elLPxPaAht3h5993vU/edit#slide=id.g3d9d9f697f_2_75)<br/><br/>C1| Obtain Book assignment  |  |
|  | 1/18/24  |  | [Thonny Video](../python-setup)<br/><br/>[Lab 2 - Thonny](../labs/1_lab2-thonny) [lab2-video](https://youtu.be/9JHJ-TFBU5M) C2| |  |
| <a name="Week2"></a> Week 2  | 1/23/24  |  [Chp 1 Reading](https://canvas.jmu.edu/courses/1997080/assignments/18048537)<br/><br/>\(Canvas/Zybook\)Tue 11pm 1/23/24  |  [Lecture 3](https://docs.google.com/presentation/d/1nxYqiwGi21mULwtOvzI6ad2sE0jjM0vfqi1IB_8jDBg/edit#slide=id.g3d9e4ed754_2_75) HW1.1-1.2 in class <br /><br />[Lab 3 - Style](../labs/2_lab3-style).<br/><br/>[Lab 3 Video](https://youtu.be/yucPdF9Tbd0)  C2  |  Start [HW 1(due Wed 1-24-24 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw1/)
| | 1/25/24  |  | Statements: [Lecture 3B](https://docs.google.com/presentation/d/1cjF_sFkA042oJu9-GaJwAg--HGI60j6wQoz5xJLocIY/edit#slide=id.g3d9e4ed754_2_75)<br/><br/>[Lab 4](../labs/3_lab4-variables)<br/><br/> C3  |  |  |
| <a name="Week3"></a> Week 3  | 1/30/24  |   [Chp 2 Reading](https://canvas.jmu.edu/courses/1997080/assignments/18048541)<br/><br/>\(Canvas/Zybook\)Tue 11pm 1/30/24      | [Lecture 4](https://docs.google.com/presentation/d/1UgRAlPt4y2gw1Uz3BJTo302iPO5kYr_bl6K7BLhhsbo/edit#slide=id.g3d98fc13d0_2_110)<br/>[Interpret Gradescope errors video](https://youtu.be/rtnzmbBqVfI)<br/><br/>[Practice variables lab](https://w3.cs.jmu.edu/spragunr/CS149_S22/www/lab/variables/variables.shtml) referenced in Gradescope errors video C4  |  [HW 2(Wed 1-31-24 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw2/) |  |
|  | 2/2/24  |  | Expressions:<br/> [Lecture 6 Circle Math](https://docs.google.com/presentation/d/1EsxKMjWEaDzmBjp7E0nqbuMr_oFM-KxhfxQu324Ws7k/edit#slide=id.g3fead46c81_2_75)<br/><br/>[Conditionals Lecture 5](https://docs.google.com/presentation/d/10fhP79RaJ4yYvlo7Xut7i3-yd8sKDKD5QS2LimnZQ-s/edit#slide=id.g40b5ecb961_2_91)<br/><br/>**Practice Quiz1** - In Class C5  |  |  |
| <a name="Week4"></a> Week 4  | 2/6/24  |  Branching/Conditionals/Assert:<br/>[Chp  3 Reading](https://canvas.jmu.edu/courses/1997080/assignments/18048526)<br /><br/>\(Canvas/Zybook) Mon 11pm 2-5-24  |  Assessment Day<br />No Class C6 <br/>[Lab 6 If Then](../labs/4_lab6-if-then/)<br/>  | [HW3 (Wed 2-7-23 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw3/)  |  |
|  | 2/8/24  |  | [Conditionals Lecture 7](https://docs.google.com/presentation/d/1fhdL0KzGb995KnNQyddbvrP1qfGfVNkwcSujeT2Knlw/edit#slide=id.g414d39d8ee_2_75)<br/><br/> [Functions Lecture 8](https://docs.google.com/presentation/d/1tFpP7Gypuu2ypA6wKxSfiJYFHboT3SwLhJ3XaR-_tKc/edit#slide=id.g112a7302985_1_0)<br/><br/> **Actual Quiz1** <br/> <br/>C7  |  |  |
| <a name="Week5"></a> Week 5  | 2/13/24  |  [Chp 4 Reading](https://canvas.jmu.edu/courses/1997080/assignments/18048545) Tue 2-13-24 11pm <br/>[Time Management](/cs149spring2022/slides/time.pdf "Time Management")        |   Functions:<br/> [Lecture 9 Functions](https://docs.google.com/presentation/d/1SYf9ahhx6vOMKVATo0C23x_fOQMMKpIzcPkqtfQaWDM/edit#slide=id.g112ae690ed2_1_11) <br/> <br/> [Lab 7 Circle Lab](../labs/5_lab7-circle)<br/><br/> [Coding Bat logic1 practice](https://codingbat.com/python/Logic-1)<br/> C8  |  [HW4 (Wed 2-14-24 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw4/) |  |
|  | 2/15/24  | Chp 4  |  [Lecture 10 Containers](https://docs.google.com/presentation/d/1cf1UprjN2o9TpPFY_zIbImVgymIeXLjna38ZimH3dH4/edit#slide=id.g27b6321382d_0_305)<br/><br/> **Practice Quiz2**  <br/><br/> C9 <br/>  |  |  -  |
| <a name="Week6"></a> Week 6  | 2/20/24  | [Chp 5 Reading](https://canvas.jmu.edu/courses/1997080/assignments/18048546) <br/>due Tue 2-20-24 11pm  |  Types including lists, sets, dicts<br/>[Lecture 11 more containers](https://docs.google.com/presentation/d/1_NSJiIaQko76whBJWYsS6-NObZCWvf5JM6vbBUiCxM8/edit#slide=id.g27b6321382d_0_112)<br/><br/>[Lab 8 List - Tuples](../labs/6_lab8-list-tuple/)<br /><br/>C10  |  [HW5 (Wed 2-21-24 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw5/)  |  |
|  | 2/22/24  | [Honor Code Case Studies(pdf)](/cs149spring2022/labs/lab-04/honor-code-case-studies.pdf "Honor Code Case Studies")<br/>[Honor Code Videos](/cs149spring2022/honor-code-cases "Honor Code Videos")<br/><br/>[Honor Code Sheet](http://www.jmu.edu/honorcode/_files/Honor_Council_printable_6_2015.pdf "Honor Code")<br/>  | C11    **Actual Quiz 2** [Lecture 12 - For loops](https://docs.google.com/presentation/d/1QuymSW3SF_2z9EnU_2IWnVKXQKa3ru54vBp34V9Iw88/edit#slide=id.g43ea64391e_2_75)  |  |  |
| <a name="Week7"></a> Week 7  | 2/27/24 |    [Chp 6 Reading due Tue 2-27-24 11pm](https://canvas.jmu.edu/courses/1997080/assignments/18048547)   |  [Coding Bat Loops Lab recommend  first_last6 to sum3 - not graded](https://codingbat.com/python/List-1)<br/><br/>[Lab 9 Haiku Lab](../labs/7_lab9-haiku-lab/)<br /> C12 |  [HW6 (Wed 2-28-24 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw6/)  |  |
|  | 2/29/24 |    |  [Lecture 13 While loops](https://docs.google.com/presentation/d/1NE1sbDDRgSNolxjyIVXrUVNnmq9KfC0CsbszDa56E7Y/edit#slide=id.g40b5ee72a5_2_81) <br /><br/> C13 <br/> Practice Quiz 3  <br /><br />  |  |  |
| <a name="Week8"></a> Week 8  | 3/5/24 |   [Chp7 While Loops](https://learn.zybooks.com/zybook/JMUCS149Spring2024) due Tue 3-5-24 11pm     |   [Lecture Unit Testing](https://docs.google.com/presentation/d/1SthL4zN4J3CKKy12jJ1i0c42eozGuujmt83hyLOJ2hc/edit#slide=id.g43ea64391e_2_75)<br/>  [Lab 11 Eight Ball Lab](../labs/_lab11-8ball/)  C14  |  [HW7 (Wed 3-6-24 11pm)](https://w3.cs.jmu.edu/cs149/hw/hw7/)  |  |
|  | 3/7/24 |  | C15  [Lecture Modules](https://docs.google.com/presentation/d/1bElhg1Z8tfueDG15iobizDdeJPHj6FFAm5pmAoGHS58/edit#slide=id.g43ea64391e_2_75) **Actual Quiz 3**   |  |  |
| <a name="Week9"></a> Week 9  | 3/12/24 | -  | No class - Spring Break |  |  |
|  | 3/14/24 | - | No class Spring Break March 11-15 C17  |   |    |
| <a name="Week10"></a> Week 10 | 3/19/24 | [Chp8 Modules](https://canvas.jmu.edu/courses/1997080/assignments/18048543) reading due 3-19-24 11pm | [Tests for PA1](../labs/10_pa1-tests/) and [PyTest](https://w3.cs.jmu.edu/cs149/info/pytest/)<br/> |   [PA1-Readiness Quiz in Canvas due Thu 3/21/24](https://w3.cs.jmu.edu/cs149/pa/pa1/) [PA1A Dice due Sun 3/24/24](https://w3.cs.jmu.edu/cs149/pa/pa1/) | 3/22/24 Withdraw W deadline |
|  | 3/21/24  |  |[Lecture 16 - File IO](https://docs.google.com/presentation/d/1f5RMcU_o3PDQcNEKnJihdy8WrSPsXm66FmXuKX7pbv0/edit#slide=id.g43ea64391e_2_75) Practice Quiz 4 |  | - |
| <a name="Week11"></a> Week 11 | 3/26/24  | [Chp9 File I/O](https://canvas.jmu.edu/courses/1997080/assignments/18048544) reading due 3-26-24 11pm | [Lecture 17 Command line](https://docs.google.com/presentation/d/12zeyDczC4y4zEtCW4NFKZkwE8TND61ZsOnOkyEsr63A/edit#slide=id.g294999aca55_0_1) [Lab 13 List Play](../labs/11_lab13-list-play/) <br/>    |  [PA1B due 4-1-24](https://w3.cs.jmu.edu/cs149/pa/pa1/) |    |
|  | 3/28/24   |  | [Lecture Sequences/Strings](https://docs.google.com/presentation/d/1c9xQGESGEVm6x-KrcpbZcBJ4usMN7i0gTNU1o82btc8/edit#slide=id.g29557dcf7bb_0_34) Actual Quiz 4 |  |  |
| <a name="Week12"></a> Week 12 | 4/2/24 | [Chp10 Sequences](https://learn.zybooks.com/zybook/JMUCS149Spring2024)       | [Lab 14 FileI/O](../labs/12_lab15-files)  [VS Code](https://w3.cs.jmu.edu/cs149/info/vscode/) |  |   |
|  | 4/4/24   |  | Practice Quiz 5 |   |  |
| <a name="Week13"></a> Week 13 | 4/9/24 | [Chp 11  Nested Data](https://learn.zybooks.com/zybook/JMUCS149Spring2024) |[Lecture 19 Nested Loops](https://docs.google.com/presentation/d/1nRJsgvqaEL0yqBE0NIpyT7XuMwWL4IUslztIKfeiJ9Q/edit#slide=id.g43ea64391e_2_75) |  |  |
|  | 4/11/24  |  | Actual Quiz 5 <br/> [Recursion lecture](https://docs.google.com/presentation/d/1W8QIQMDltBTYMeS4KYcZd9ln9yalFNUENFypT4PC4FQ/edit#slide=id.g441b6e16ed_2_107) | [PA2 Readiness Quiz due 4/11 11pm](https://w3.cs.jmu.edu/cs149/pa/pa2/) |  |
| <a name="Week14"></a>Week 14  | 4/16/24 | [Chp 12 Recursion](https://learn.zybooks.com/zybook/JMUCS149Spring2024) | [Lab 15 - Recursion](../labs/13_lab15-recursive-lists)    |  [PA2A word_files due Sun 4/14 11pm](https://w3.cs.jmu.edu/cs149/pa/pa2/)   |
|  | 4/18/24  |  | [JSON examples](https://docs.google.com/presentation/d/1JMzKkJ2tN0drDZr3uI77iw07Trp51DH7gBZtRsYJJfU/edit#slide=id.g441b6e16ed_2_91)Practice Quiz 6 <br/><br/>C26  | [PA2B boxed.py due Tue 4/23 11pm](https://w3.cs.jmu.edu/cs149/pa/pa2/)   |   |
| <a name="Week15"></a>Week 15  | 4/23/24  |  | [Stars Lab](../labs/13_lab16-stars) | - |  |
|  | 4/25/24  |  | Actual Quiz 6 | - |  |
| <a name="Week16"></a>Week 16  | 4/30/24 |  | PA3 work day |  [PA3 due Tue 4/30](https://w3.cs.jmu.edu/cs149/pa/pa3/) |   |
|  | 5/2/24   |  | Final Review |  | Last day of classes |
| <a name="Week17"></a>Week 17 | 5/7/24 |  Exam Week  | [Exam Schedule](https://www.jmu.edu/registrar/wm_library/1241_spring_exam_schedule.pdf) |  | Exam Week |
|  | 5/9/24 |  | Final Exam - Thu 5/9 8-10am   |  | Exam Week |


<a href="#top"><span title="Back to Top"></span>Back to Top</a>
 <p id="back-top" style="display: block;"><a href="#top"><span title="Back to Top"></span>Back to Top</a></p>
<script type="text/javascript">
    // <![CDATA[
    $(window).load(function(){ // using window load function instead of document ready function

    /* Animated scroll to top by @NickLa, Web Designer Wall (http://webdesignerwall.com/tutorials/animated-scroll-to-top) with modifications by johns2ja */
        // hide #back-top first
        $("#back-top").hide();

        // fade in #back-top
        //$(function () { /* remove containing function to ensure it works cross-browser - johns2ja */
            $(window).scroll(function () {
                if ($(this).scrollTop() > 100) {
                    $('#back-top').fadeIn();
                } else {
                    $('#back-top').fadeOut();
                }
            });

            // scroll body to 0px on click
            $('#back-top a').click(function () {
                $('body,html').animate({
                    scrollTop: 0
                }, 800);
                return false;
            });
    // });       /* remove containing function to ensure it works cross-browser */
    });
    // ]]>
</script>

<style type="text/css">
<!--
#back-top {
  bottom: 130px;
  left: 5%; /* instead of margin-left - johns2ja */
  position: fixed;
}
#back-top a {
  color: #bbb !important;
  display: block;
  font-size: 11px;
  height: 75px;
  text-align: center;
  text-decoration: none !important;
  text-transform: uppercase;
  transition: all 1s ease 0s;
  width: 75px;
}
#back-top span {
  background: #ddd url("//www.jmu.edu/jmucmsfiles/images/up-arrow.png") no-repeat scroll center center;
  border-radius: 15px;
  display: block;
  height: 75px;
  margin-bottom: 7px;
  transition: all 1s ease 0s;
  width: 75px;
}
@media all and (max-width:768px){ /* RWD by johns2ja */
        #back-top {
                bottom: 3%;
                left: 1%;
        }
        #back-top a {
                height: 32px;
                width: 32px;
                font-size: 0px;
        }
        #back-top span {
                width: 32px;
                height: 32px;
                background-size: 32px;
        }
}
-->
</style>
