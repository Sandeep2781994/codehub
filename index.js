window.addEventListener('scroll', function(){
    const header = document.querySelector('header');
    header.classList.toggle("sticky", window.scrollY > 0);
});


// For Menu Icon change on click
const menu_btn = document.querySelector('.hamburger');
const mobile_menu = document.querySelector('.mobile-nav');

menu_btn.addEventListener('click', function () {
    menu_btn.classList.toggle('is-active');
    mobile_menu.classList.toggle('is-active');
});





// Below JavaScript code adds functionality to close the mobile navigation bar (navbar) 
// when a user clicks on a link inside the mobile menu.

// This function, closeMobileNavbar, removes the 'is-active' class from both the menu_btn (hamburger icon) and mobile_menu elements.
// The 'is-active' class is responsible for showing/hiding the mobile menu, so removing it closes the menu.
function closeMobileNavbar() {
    menu_btn.classList.remove('is-active');
    mobile_menu.classList.remove('is-active');
}

// Add event listener to each mobile menu link
const mobileLinks = document.querySelectorAll('.mobile-nav a');

mobileLinks.forEach(link => {
    link.addEventListener('click', closeMobileNavbar);
});



