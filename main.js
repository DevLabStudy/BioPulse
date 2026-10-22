window.addEventListener('DOMContentLoaded', () => {
    // Karuzela
    const slides = document.querySelectorAll('.carousel-slide');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
            dots[i].classList.toggle('active', i === index);
        });
        currentIndex = index;
    }

    setInterval(() => {
        showSlide((currentIndex + 1) % slides.length);
    }, 5000);

    dots.forEach(dot => {
        dot.addEventListener('click', (e) => {
            showSlide(parseInt(e.target.getAttribute('data-index')));
        });
    });

    // Płynne przewijanie
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if(targetId.startsWith('#')) {
                e.preventDefault();
                document.querySelector(targetId)?.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
