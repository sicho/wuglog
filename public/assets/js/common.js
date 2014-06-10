$(document).ready(function(){

        $(".navbar-nav > li > .scroll-nav").click(function(){
                var speed = 500;
                var href= $(this).attr("href");
                var target = $(href == "#" || href == "" ? 'html' : href);
                var position = target.offset().top;
                $("html, body").animate({scrollTop:position}, speed, "swing");
                return false;
        });

        var have_show = false;

        $("#have-show").click(function(){
                if (have_show) {
                    $(this).children("span").css("background-color", "#5cb85c");
                    $(".have").fadeTo('normal', 1.0);
                } else {
                    $(this).children("span").css("background-color", "#999");
                    $(".have").fadeTo('normal', 0.3);
                }

                have_show = !have_show;
                return false;
        });

        var not_have_show = false;

        $("#not-have-show").click(function(){
                if (not_have_show) {
                    $(this).children("span").css("background-color", "#f0ad4e");
                    $(".not-have").fadeTo('normal', 1.0);
                } else {
                    $(this).children("span").css("background-color", "#999");
                    $(".not-have").fadeTo('normal', 0.3);
                }

                not_have_show = !not_have_show;
                return false;
        });

        $(".item-have") .hover(function(){
                $(this).fadeTo("4000", 0.3);
            },function(){
                $(this).fadeTo("4000", 0.85);
        });

});
