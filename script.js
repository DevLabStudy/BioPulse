window.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('canvas3d-container');
    if (!container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Geometria pulsującego rdzenia (Data Node)
    const geometry = new THREE.IcosahedronGeometry(2, 2);
    const material = new THREE.MeshBasicMaterial({ 
        color: 0x38bdf8, 
        wireframe: true,
        transparent: true,
        opacity: 0.7
    });
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // Cząsteczki w tle
    const particlesGeo = new THREE.BufferGeometry();
    const count = 100;
    const positions = new Float32Array(count * 3);
    for(let i = 0; i < count * 3; i++) {
        positions[i] = (Math.random() - 0.5) * 12;
    }
    particlesGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const particlesMat = new THREE.PointsMaterial({ color: 0x0ea5e9, size: 0.05 });
    const particles = new THREE.Points(particlesGeo, particlesMat);
    scene.add(particles);

    camera.position.z = 5;

    let clock = new THREE.Clock();
    function animate() {
        requestAnimationFrame(animate);
        let elapsedTime = clock.getElapsedTime();
        
        sphere.rotation.x = elapsedTime * 0.15;
        sphere.rotation.y = elapsedTime * 0.25;
        
        // Efekt pulsowania BioPulse
        let scaleFactor = 1 + Math.sin(elapsedTime * 3) * 0.08;
        sphere.scale.set(scaleFactor, scaleFactor, scaleFactor);

        particles.rotation.y = elapsedTime * 0.03;

        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
        if (!container) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
});
