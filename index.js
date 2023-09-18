// Mobile menu JS script
var menu = document.getElementById('menu');
menu.style.maxHeight = "0px";
function menutoggle() {
    if (menu.style.maxHeight == "0px") {
        menu.style.maxHeight = "200px";
    }else {
        menu.style.maxHeight = "0px";
    }
}

// window.addEventListener("scroll",function () {
//     var header = document.querySelector("header");
//     header.classList.toggle("sticky", window.scrollY > 0);
// });


// make a header element "sticky" when the user scrolls down the page.
$(window).on('scroll',function(){
    if ($(window).scrollTop()) {
        $('header').addClass('sticky');
    }
    else{
        $('header').removeClass('sticky');
    }
})












