document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('carouselTrack');
    if (!track) return;

    // Sklonowanie elementów, aby uzyskać płynny efekt nieskończonej karuzeli
    const cards = Array.from(track.children);
    cards.forEach(card => {
        const clone = card.cloneNode(true);
        track.appendChild(clone);
    });

    let scrollPos = 0;
    const speed = 0.8; // Prędkość przewijania
    let isPaused = false;

    function step() {
        if (!isPaused) {
            scrollPos += speed;
            // Gdy przesuniemy się o szerokość oryginalnego zestawu kart, resetujemy pozycję
            if (scrollPos >= track.scrollWidth / 2) {
                scrollPos = 0;
            }
            track.style.transform = `translateX(-${scrollPos}px)`;
        }
        requestAnimationFrame(step);
    }

    track.addEventListener('mouseenter', () => { isPaused = true; });
    track.addEventListener('mouseleave', () => { isPaused = false; });

    requestAnimationFrame(step);
});
