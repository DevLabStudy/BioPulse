window.addEventListener('DOMContentLoaded', () => {
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
                
                const tag = card.getAttribute('data-tag') || 'Projekt';
                const title = card.getAttribute('data-title') || 'Wzór strony';
                const desc = card.getAttribute('data-desc') || 'Opis projektu...';
                const link = card.getAttribute('data-link') || '#';

                modalTag.textContent = tag;
                modalTitle.textContent = title;
                modalDesc.textContent = desc;
                mockupHeading.textContent = title;
                modalFullLink.setAttribute('href', link);
                modalUrlText.textContent = link;

                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        const closeMod = () => {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        };

        if (closeModal) closeModal.addEventListener('click', closeMod);
        if (closeModalBtn) closeModalBtn.addEventListener('click', closeMod);
        modal.addEventListener('click', (e) => { if (e.target === modal) closeMod(); });
    }
});
