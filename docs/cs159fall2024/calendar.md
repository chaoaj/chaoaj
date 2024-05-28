#CS159 Chao Calendar
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
var dt1 = new Date(2024, 7, 20); // new Date(2023, 7, 17); // January 1 = (2021, 0, 1)
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
<p>Java and Config Resources:</p>


<div>(<strong>Note: This schedule is tentative and is subject to change during the semester</strong>) <br /><br />


| Week / Topic | Reading | Tue in class | Thu in class | HW / Programming Assignment | Events |
| --- | ---------- | --------- | ------- | -------------- | --------------------------- |
| 1 <a name="Week1"></a>  Intro | Obtain book | -        |  c1 8/22      |                             |        |
| 2 <a name="Week2"></a> Intro | Chp 1 | -         |    c1  8/29      |                             |        |
| 3 <a name="Week3"></a>Intro | Chp 2 | -            |    c1   9/5       |                             |        |
| 4 <a name="Week4"></a>  Intro | Chp 3 | -            |    Practice Quiz 1  9/12      |                             |        |
| 5 <a name="Week5"></a>  Intro | Chp 4 | -            |    Actual Quiz 1 9/19      |                             |        |
| 6 <a name="Week6"></a>  Intro | Chp 5 | -            |    Practice Quiz 2 c1 9/26      |                             |        |
| 7 <a name="Week7"></a>  Intro | Chp 6 | -            |    Actual Quiz 2 c1 10/3      |                             |        |
| 8 <a name="Week8"></a>  Intro | Chp 7 | -            |    Practice Quiz 3 c1 10/10     |                             |        |
| 9 <a name="Week9"></a> Intro | Chp 8 |  Actual Quiz 3 c        |    c1  10/17     |                             |  Fall Break 16-20      |
| 10 <a name="Week10"></a> Intro | Chp 9| -            |    Practice Quiz 4 c1 10/24    |                             |        |
| 11 <a name="Week11"></a>  Intro | Chp 10 | -            |  Actual Quiz 4  c1 10/31   |                             |        |
| 12 <a name="Week12"></a>   Intro | Chp 11 | -            | Practice Quiz 5   c1 11/7       |                             |        |
| 13 <a name="Week13"></a>   Intro | Chp 12 | -            | Actual Quiz 5 c1  11/14      |                             |        |
| 14 <a name="Week14"></a>   Intro | Chp 13 | -            | Practice Quiz 6   c1  11/21      |                             |        |
| 15 <a name="Week15"></a>   Intro | Thanksgiving break | -            |    c1  11/28      |                             |  Thanksgiving Break 11/25 to 11/29     |
| 16 <a name="Week16"></a>   Intro | Review | -            |  Actual Quiz 6  c1  12/5      |     | Dec 6 last day of class |
| 17 <a name="Week17"></a>   Exam week | Exam Schedule |               |    c1  12/12      |                             |        |



---



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
