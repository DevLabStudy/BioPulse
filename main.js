window.addEventListener('DOMContentLoaded', () => {
    // === AUTOMATYCZNA KARUZELA (5 SLAJDÓW) ===
    const slides = document.querySelectorAll('.carousel-slide');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;
    let slideInterval;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
            dots[i].classList.toggle('active', i === index);
        });
        currentIndex = index;
    }

    function nextSlide() {
        let nextIndex = (currentIndex + 1) % slides.length;
        showSlide(nextIndex);
    }

    // Zmiana slajdu co 5 sekund
    slideInterval = setInterval(nextSlide, 5000);

    // Obsługa kliknięcia w kropki nawigacyjne
    dots.forEach(dot => {
        dot.addEventListener('click', (e) => {
            clearInterval(slideInterval);
            const index = parseInt(e.target.getAttribute('data-index'));
            showSlide(index);
            slideInterval = setInterval(nextSlide, 5000);
        });
    });

    // === PŁYNNE PRZEWIJANIE (SMOOTH SCROLL) ===
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if(targetId.startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(targetId);
                if(targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
});
