function scrollLeftCarousel() {
    const carousel = document.getElementById('carousel');
    const scrollAmount = carousel.querySelector('.item').offsetWidth + 20;
    carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
}

function scrollRightCarousel() {
    const carousel = document.getElementById('carousel');
    const scrollAmount = carousel.querySelector('.item').offsetWidth + 20;
    carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
}
