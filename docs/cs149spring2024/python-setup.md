## CS149 Python Setup

<p>The purpose of this document is to walk you through the process of setting up your computer for Python development and code submission in CS 149.</p>
<h2 id="downloading-and-installing-thonny">Downloading and Installing Thonny</h2>
<p>The officially supported Integrated Development Environment (IDE) for this semester will be Thonny.</p>
<p>Download and run the appropriate installer for your operating system from <a class="uri" href="https://thonny.org/">https://thonny.org/</a>. You should accept all of the default options during installation.</p>
<h2 id="revealing-file-extensions">Revealing File Extensions</h2>
<p>When naming files, there is a longstanding convention of using <em>file extensions</em> to indicate the type of information that the file contains. For example, a Windows executable might be named <code>installer.exe</code>, while a Word document might be named <code>FinalReport.docx</code>. In this case <code>.exe</code> and <code>.docx</code> are the file extensions indicating the file types.</p>
<p>In the good old days, these file exertions were visible by default, and they were often helpful in figuring out file types. Unfortunately, file extensions could also be confusing and intimidating for non-technical users. For example, <code>.avi</code>, <code>.mp4</code>, <code>.mpg</code>, <code>.divx</code>, <code>.mov</code> (among many others) are all file extensions that represent different kinds of video files. Understanding the differences between them is crucial to someone involved in video production, but irrelevant to someone who just wants to watch the video. In the interest of not confusing people, modern operating systems generally hide file extensions by default.</p>
<p>Now that you are a computer scientist, you have become the kind of person who needs to pay attention to file extensions. Congratulation! This means that you should modify the settings on your computer to show file extensions by default. Follow the instructions in the following links to change the appropriate settings on your computer:</p>
<ul>
<li>Windows: <a class="uri" href="https://fileinfo.com/help/windows_10_show_file_extensions">https://fileinfo.com/help/windows_10_show_file_extensions</a></li>
<li>OSX: <a class="uri" href="https://www.howtogeek.com/714021/how-to-show-all-filename-extensions-on-the-mac/">https://www.howtogeek.com/714021/how-to-show-all-filename-extensions-on-the-mac/</a></li>
</ul>
<h2 id="saving-files-in-thonny-and-submitting-through-gradescope">Saving Files in Thonny and Submitting Through Gradescope</h2>
<p>You will save yourself some trouble this semester if you get into the habit of organizing your Python files into folders organized by assignment. I suggest creating a top-level folder named <code>CS149</code> that you can use to store each individual assignment folder. Watch the video below for an example of how this can be accomplished.</p>
<h2 id="pep8---python-style">PEP8 - Python Style</h2>
<p>When writing in English, readability can be impacted by the way the text is laid out on the page. We use conventions, like indenting the first sentence of a paragraph, to make it easier to understand written text. Programming languages are the same. Programs are easier to read if we agree on a set of conventions for how the code should be formatted. <a href="https://www.python.org/dev/peps/pep-0008/">PEP 8</a> is the official document that describes the standard formatting conventions for Python code. (Here is a prettier version: <a class="uri" href="https://pep8.org/">https://pep8.org/</a>.) You don’t need to read and understand the full PEP 8 document now, but you may want to look it over to get a feel for the issues that it addresses.</p>
<p>When you submit homework assignments for CS 149 they will automatically be checked against the PEP 8 formatting requirements using a tool named <code>flake8</code>. You will only receive full credit if you pass all of these automated style checks. You can install <code>flake8</code> in Thonny by selecting <em>Tools -&gt; Manage Packages…</em> and then finding and installing <code>flake8</code> as well as <code>pep8-naming</code>. After installation, you should be able to check your file by typing the following into the Thonny shell:</p>
<pre><code>&gt;&gt;&gt; !flake8 hello_world.py</code></pre>
<p>The exclamation point tells the Python interpreter the command should not be interpreted as Python code.</p>
<p>Note that the Gradescope autograder is configured to be slightly more lenient than the default settings for <code>flake8</code>. We allow line lengths up to 100 and disable checks for some errors and warnings. If you want to run <code>flake8</code> with exactly the same settings as Gradescope, you can copy the following file into the same directory as your python code:</p>
<ul>
<li><a href="https://w3.cs.jmu.edu/spragunr/CS149_S22/www/lab/thonny/setup.cfg">setup.cfg</a></li>
</ul>
<h2 id="video">Video</h2>
<p>Watch this short video for a demonstration of the steps required to create a new Python file, store it in a reasonable location, and submit it through Gradescope.</p>
<h2><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" data-mce-fragment="1" frameborder="0" height="315" src="https://www.youtube.com/embed/jsek3DnsI4k" title="YouTube video player" width="560"></iframe></h2>
