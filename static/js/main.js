// Hamburger Menu

const hamburgerMenu = document.querySelector(".hamburger-menu");
let menuClicked = false;

hamburgerMenu.addEventListener('click', () => {
    if (!menuClicked) {
        hamburgerMenu.classList.add("clicked");
        menuClicked = true;
    } else {
        hamburgerMenu.classList.remove("clicked");
        menuClicked = false;
    }
});