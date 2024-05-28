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
