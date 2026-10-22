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

    if (slides.length > 0) {
        setInterval(() => {
            showSlide((currentIndex + 1) % slides.length);
        }, 5000);

        dots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                showSlide(parseInt(e.target.getAttribute('data-index')));
            });
        });
    }

    // === NAPRAWIONE ROZSZERZANE OKNO MODALNE ===
    const modal = document.getElementById('projectModal');
    const modalCards = document.querySelectorAll('.open-modal');
    const closeModal = document.getElementById('closeModal');
    const closeModalBtn = document.getElementById('closeModalBtn');

    const modalTag = document.getElementById('modalTag');
    const modalTitle = document.getElementById('modalTitle');
    const modalDesc = document.getElementById('modalDesc');
    const mockupHeading = document.getElementById('mockupHeading');
    const modalFullLink = document.getElementById('modalFullLink');
    const modalUrlText = document.getElementById('modalUrlText');

    if (modal && modalCards.length > 0) {
        modalCards.forEach(card => {
            card.addEventListener('click', (e) => {
                e.preventDefault();
                const title = card.getAttribute('data-title');
                const desc = card.getAttribute('data-desc');
                const link = card.getAttribute('data-link');
                const tag = card.getAttribute('data-tag');

                modalTag.textContent = tag;
                modalTitle.textContent = title;
                modalDesc.textContent = desc;
                mockupHeading.textContent = title;
                modalFullLink.setAttribute('href', link);
                modalUrlText.textContent = `https://webcraft-studio.ovh/${link}`;

                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        function closeProjectModal() {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        if (closeModal) closeModal.addEventListener('click', closeProjectModal);
        if (closeModalBtn) closeModalBtn.addEventListener('click', closeProjectModal);

        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeProjectModal();
            }
        });
    }

    // Zmiana motywu koloru
    const colorSelect = document.getElementById('colorSelect');
    if (colorSelect) {
        colorSelect.addEventListener('change', (e) => {
            document.documentElement.setAttribute('data-theme', e.target.value);
        });
    }

    // Płynne przewijanie
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if(targetId.startsWith && targetId.startsWith('#')) {
                e.preventDefault();
                document.querySelector(targetId)?.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
