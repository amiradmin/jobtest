

function StickyCheck(){
    if($(window).width()>975){
    var sidebar = new StickySidebar('.sidebar2', {
    topSpacing: 75,
    bottomSpacing: 0,
    containerSelector: '.main-content',
    innerWrapperSelector: '.sidebar__inner2',
    });
    var sidebar = new StickySidebar('.sidebar', {
        topSpacing: 75,
        bottomSpacing: 0,
        containerSelector: '.main-content',
        innerWrapperSelector: '.sidebar__inner',
        });
    }
}
//main nav active
$(function(){
    $('.navbar-toggle').click(function(){
         
            $('#mynav > ul ').slideToggle(300);
            $(this).toggleClass('active')
        })

      $('#search').click(function(){
          $('.search-bar').addClass('search-bar-open');
          $('.input-search').addClass('search-open').focus();
          $('#closeSearch').show();
          $(this).hide();
      })
      $('#closeSearch').click(function(){
            $('.search-bar').removeClass('search-bar-open');
          $('.input-search').removeClass('search-open');
          $('#search').show();
          $(this).hide();
      })

      $('#mynav  ul  li.has-dropdown').each(function(){
        $(this).children('a').append("<i class='fa fa-caret-down'></i>")
    }) 
    initializeNav()
$(window).resize(function(){
    initializeNav()
})

   
      //hide dropdown if click anywhere
    $(document).click(function(e){

        if($(window).width()>975){
       if($(e.target).closest('#mynav').length != 0){
       if(e.target.getAttribute("href")!="javascript:void(0);"){
        }else{
        return false;}}
        $('#mynav  ul  li.has-dropdown').children('ul').removeClass('fadeUp');
        $('#mynav  ul  li').children('a').children('i').removeClass('open-dropdown');
        $('#mynav  ul  li').children('a').removeClass('active');
         }
        });

    //hide dropdown if click anywhere
    //handle dropdown click
    $('#mynav > ul > li > ul > li.has-dropdown').click(function(){
        if($(window).width()>975){
        $(this).siblings('#mynav > ul > li > ul > li.has-dropdown').children('ul').removeClass('fadeUp');
        $(this).siblings('li').children('a').children('i').removeClass('open-dropdown');

        $(this).children('a').children('i').toggleClass('open-dropdown');
        if($(this).children('ul').hasClass('fadeDown') || $(this).children('ul').hasClass('fadeUp'))
           $(this).children('ul').toggleClass('fadeDown fadeUp')
           else
           $(this).children('ul').addClass('fadeUp')
        }
        else{
            $(this).children('a').toggleClass('active');
            $(this).children('a').children('i').toggleClass('open-dropdown');
            $(this).children('ul').slideToggle(300);
        }
        return false
    })
    $('#mynav > ul > li.has-dropdown').click(function(){
        if($(window).width()>975){
        $(this).siblings('#mynav > ul > li.has-dropdown').children('ul').removeClass('fadeUp');
        $(this).siblings('li').children('a').children('i').removeClass('open-dropdown');
        $(this).siblings('li').children('a').removeClass('active')

        $(this).children('a').children('i').toggleClass('open-dropdown');
        $(this).children('a').toggleClass('active');
        if($(this).children('ul').hasClass('fadeDown') || $(this).children('ul').hasClass('fadeUp'))
           $(this).children('ul').toggleClass('fadeDown fadeUp')
           else
           $(this).children('ul').addClass('fadeUp')
        }
        else{
            $(this).children('a').toggleClass('active');
            $(this).children('a').children('i').toggleClass('open-dropdown');
            $(this).children('ul').slideToggle(300);
        }
    })
    
    //handle dropdown click
})


  function initializeNav(){

    $('.navbar-toggle').removeClass('active')
    $('#mynav > ul  li.has-dropdown').children('a').removeClass('active');
    $('#mynav > ul  li.has-dropdown').children('ul').removeClass('fadeUp fadeDown').removeAttr('style');
    $('#mynav > ul').removeAttr('style');
    $('#mynav > ul  li.has-dropdown').children('ul').removeClass('fadeUp');
    $('#mynav > ul  li').children('a').children('i').removeClass('open-dropdown');
}
//main nav

$(document).ready(function(){
    //preloader
    StickyCheck();
})
$(document).ready(function(){


    //close/open modal
    $(".open-modal").click(function(){
        $(".modal-login").css("display","flex");
        $(".modal-login").show();
    })
    $("#close-modal").click(function(){
        $(".modal-login").fadeOut(200);
    })
    //
    setTimeout(function(){
        $("#loading").fadeOut(200);
    },1000)

    //dont remember
    $(".dontRem").click(function(){
        $("#dontRemember").trigger("click");
    })

    

    //gotop
    $(window).scroll(function(){
        if($(this).scrollTop()>200){
            $('.gotop').addClass('gotop-show');
        }
        else
        $('.gotop').removeClass('gotop-show');

    })

    //hash clicks
    $('a.gotop[href^="#"]').on('click', function (event) {
        var target = this.hash; // gets the #hash
        $target = $(target); //
        event.preventDefault();
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top -100 // scrolls to the link
        }, 1500, 'swing', function () {
            $(document).on("easeInOut", onScroll());
        });
    });

    //owl carousel
    $('#owl-carousel').owlCarousel({
        rtl:true,
        loop:true,
        autoplay:true,
        autoplayTimeout:5000,
        // animateOut:'fadeOut',
        autoplayHoverPause: true,
        stagePadding: 0,
        margin:10,
        nav:true,
        items:1,
        touchDrag:true,
        freeDrag:true,
    })
    var owl1 =  $('#owl-carousel1');
    owl1.owlCarousel({
        stagePadding: 0,
                nav: true,
                rtl: true,
                loop: true,
                margin: 20,
                autoplay: true,
                autoplayHoverPause: true,
                autoplayTimeout: 5000,
                responsiveClass: true,
                dots: false,
                responsive: {
                    0: {
                        items: 1,
                        nav: false,
                    },
                    600: {
                        items: 2,
                        nav: false
                    },
                    768: {
                        items: 3,
                        nav: false
                    },
                    992: {
                        items: 4,
                        nav: false
                    }
                }
    })
    $('.next1').click(function () {
        owl1.trigger('next.owl');
    })
    $('.next1').mouseover(function () {
        owl1.trigger('stop.owl.autoplay')
    })
    $('.next1').mouseleave(function () {
        owl1.trigger('play.owl.autoplay')
    })
    $('.prev1').click(function () {
        owl1.trigger('prev.owl');
    })
    $('.prev1').mouseover(function(){
        owl1.trigger('stop.owl.autoplay')
    })
    $('.prev1').mouseleave(function () {
        owl1.trigger('play.owl.autoplay')
    })
    var owl2 = $('#owl-carousel2');
    owl2.owlCarousel({
            stagePadding: 0,
            nav: true,
            rtl: true,
            loop: true,
            margin: 20,
            autoplay: true,
            autoplayHoverPause: true,
            animateOut: 'fadeOut',
            autoplayTimeout: 5000,
            responsiveClass: true,
            dots: false,
            responsive: {
                0: {
                    items: 1,
                    nav: false,
                },
                600: {
                    items: 2,
                    nav: false
                },
                768: {
                    items: 2,
                    nav: false
                },
                992: {
                    items: 3,
                    nav: false
                }
            }
        })
        $('.next').click(function () {
            owl2.trigger('next.owl');
        })
        $('.next').mouseover(function () {
            owl2.trigger('stop.owl.autoplay')
        })
        $('.next').mouseleave(function () {
            owl2.trigger('play.owl.autoplay')
        })
        $('.prev').click(function () {
            owl2.trigger('prev.owl');
        })
        $('.prev').mouseover(function(){
            owl2.trigger('stop.owl.autoplay')
        })
        $('.prev').mouseleave(function () {
            owl2.trigger('play.owl.autoplay')
        })
        //toures
        var owl3 = $('#owl-carousel3');
        owl3.owlCarousel({
                stagePadding: 0,
                nav: true,
                rtl: true,
                loop: true,
                margin: 20,
                autoplay: true,
                autoplayHoverPause: true,
                animateOut: 'fadeOut',
                autoplayTimeout: 5000,
                responsiveClass: true,
                dots: false,
                responsive: {
                    0: {
                        items: 1,
                        nav: false,
                    },
                    600: {
                        items: 2,
                        nav: false
                    },
                    768: {
                        items: 3,
                        nav: false
                    },
                    992: {
                        items: 4,
                        nav: false
                    }
                }
            })
            $('.next3').click(function () {
                owl3.trigger('next.owl');
            })
            $('.next3').mouseover(function () {
                owl3.trigger('stop.owl.autoplay')
            })
            $('.next3').mouseleave(function () {
                owl2.trigger('play.owl.autoplay')
            })
            $('.prev3').click(function () {
                owl3.trigger('prev.owl');
            })
            $('.prev3').mouseover(function(){
                owl3.trigger('stop.owl.autoplay')
            })
            $('.prevv').mouseleave(function () {
                owl3.trigger('play.owl.autoplay')
            })
    });

    // left side image size check
    $(function(){
        $(".left-side-card-image").each(function () {
            var h1 = $(this).parent().parent().css('height');
            h1 = 'calc(' + h1 + ' - 26px)';
            $(this).css({ 'max-height': h1 });
        })
    })

    //side nav
    $(function(){
        $('#side-nav > ul li.has-dropdown').each(function(){
            $(this).children('a').append("<i class='fa fa-caret-down'></i>")
        })
        initializeNav()
        //hide dropdown if click anywhere
        //handle dropdown 
        $('#side-nav > ul > li > ul > li.has-dropdown').click(function(){       
                $(this).first().children('a').toggleClass('active');
                $(this).first().children('a').children('i').toggleClass('open-dropdown');
                $(this).first().children('ul').slideToggle(300);
            return false;
        })
        $('#side-nav > ul > li.has-dropdown').click(function(){
            if($(this).children('a').hasClass('active')){
           hideAll();
            }
            else{
                hideAll()
                $(this).first().children('a').toggleClass('active');
            $(this).first().children('a').children('i').toggleClass('open-dropdown');
            $(this).first().children('ul').slideToggle(300);
            } 
    })
       
        //handle dropdown click
    })
    
      function initializeNav(){
        $('#side-nav > ul > li.has-dropdown a.active').each(function(){
            $(this).children('i').toggleClass('open-dropdown');
           $(this).parent('li.has-dropdown').children('ul').slideToggle(300);
        })
    }
    
        function hideAll(){
            $('#side-nav ul li.has-dropdown a.active').each(function(){
                $(this).toggleClass('active');
                $(this).children('i').toggleClass('open-dropdown');
                $(this).parent('li.has-dropdown').children('ul').slideToggle(300);
            })
        }