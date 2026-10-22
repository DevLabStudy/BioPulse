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
                modalTag.textContent = card.getAttribute('data-tag');
                modalTitle.textContent = card.getAttribute('data-title');
                modalDesc.textContent = card.getAttribute('data-desc');
                mockupHeading.textContent = card.getAttribute('data-title');
                const link = card.getAttribute('data-link');
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
