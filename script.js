document.addEventListener('DOMContentLoaded', () => {
    const scroller = document.querySelector('.portfolio-scroller');
    
    if (scroller) {
        // Opcjonalne: płynne przewijanie kółkiem myszy w poziomie na komputerach
        scroller.addEventListener('wheel', (evt) => {
            if (window.innerWidth > 1024) {
                evt.preventDefault();
                scroller.scrollLeft += evt.deltaY;
            }
        });
    }
});
