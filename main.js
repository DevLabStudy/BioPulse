window.addEventListener('DOMContentLoaded', () => {
    // === 1. KARUZELA ARCHITEKTURY ===
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

    slideInterval = setInterval(nextSlide, 5000);

    dots.forEach(dot => {
        dot.addEventListener('click', (e) => {
            clearInterval(slideInterval);
            const index = parseInt(e.target.getAttribute('data-index'));
            showSlide(index);
            slideInterval = setInterval(nextSlide, 5000);
        });
    });

    // === 2. WIZUALIZACJA 3D KLASTRA (THREE.JS) ===
    const container = document.getElementById('canvas-container');
    if (!container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(50, container.clientWidth / container.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // Główna struktura klastra (wielościan z siatką korporacyjną)
    const geometry = new THREE.IcosahedronGeometry(1.5, 2);
    const material = new THREE.MeshStandardMaterial({
        color: 0x38bdf8,
        wireframe: true,
        roughness: 0.1,
        metalness: 0.9
    });
    const clusterCore = new THREE.Mesh(geometry, material);
    scene.add(clusterCore);

    // Wewnętrzny rdzeń energetyczny
    const innerGeometry = new THREE.SphereGeometry(0.7, 32, 32);
    const innerMaterial = new THREE.MeshBasicMaterial({ color: 0x818cf8 });
    const innerCore = new THREE.Mesh(innerGeometry, innerMaterial);
    scene.add(innerCore);

    // Oświetlenie sceny
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0x38bdf8, 4, 50);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);

    camera.position.z = 4.2;

    // Pętla animacji z płynnym obrotem
    function animate() {
        requestAnimationFrame(animate);
        
        clusterCore.rotation.x += 0.0015;
        clusterCore.rotation.y += 0.003;
        
        innerCore.rotation.y -= 0.005;

        renderer.render(scene, camera);
    }

    animate();

    // Skalowanie przy zmianie wielkości okna
    window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
});
