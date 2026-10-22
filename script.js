document.addEventListener('DOMContentLoaded', () => {
    ['trackLeft', 'trackRight'].forEach(id => {
        const track = document.getElementById(id);
        if (track) {
            const cards = Array.from(track.children);
            cards.forEach(card => {
                const clone = card.cloneNode(true);
                track.appendChild(clone);
            });
        }
    });
});
