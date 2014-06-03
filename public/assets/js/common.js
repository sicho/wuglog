$(document).ready(function(){

        $(".navbar-nav > li > a[href^=#]").click(function(){
                var speed = 500;
                var href= $(this).attr("href");
                var target = $(href == "#" || href == "" ? 'html' : href);
                var position = target.offset().top;
                $("html, body").animate({scrollTop:position}, speed, "swing");
                return false;
        });

        $(".item-have") .hover(function(){
                $(this).fadeTo("4000", 0.3);
            },function(){
                $(this).fadeTo("4000", 0.85);
        });

});
