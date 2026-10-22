# BioPulse Enterprise 🧬

<div style="text-align: center; color: #94a3b8; font-size: 1.1rem; margin-bottom: 20px;">
    Autorski system klasy Data Pipeline & Real-Time Stream Validation
</div>

<!-- Kontener na interaktywną grafikę 3D z wymuszonymi wymiarami -->
<div id="canvas3d-container" style="width: 100%; min-height: 400px; height: 400px; background: #030712; border-radius: 16px; border: 1px solid #1e293b; position: relative; overflow: hidden; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
    <div style="position: absolute; top: 15px; left: 20px; font-family: monospace; font-size: 12px; color: #38bdf8; z-index: 10; background: rgba(15, 23, 42, 0.8); padding: 6px 12px; border-radius: 6px; border: 1px solid #334155;">
        STATUS: SYSTEM ONLINE [PULSE: ACTIVE]
    </div>
</div>

## 🚀 Architektura i Możliwości

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px;">
    <div style="background: #0f172a; border: 1px solid #1e293b; padding: 24px; border-radius: 12px;">
        <h3 style="color: #38bdf8; margin-top: 0;">⚡ Stream Ingest</h3>
        <p style="color: #94a3b8; font-size: 14px;">Błyskawiczny odczyt masowych strumieni danych z zewnętrznych źródeł biznesowych i API.</p>
    </div>
    <div style="background: #0f172a; border: 1px solid #1e293b; padding: 24px; border-radius: 12px;">
        <h3 style="color: #38bdf8; margin-top: 0;">🛡️ Anomaly Detection</h3>
        <p style="color: #94a3b8; font-size: 14px;">Automatyczna walidacja reguł rynkowych, odrzucanie błędów i ochrona struktur systemowych.</p>
    </div>
    <div style="background: #0f172a; border: 1px solid #1e293b; padding: 24px; border-radius: 12px;">
        <h3 style="color: #38bdf8; margin-top: 0;">📊 Enterprise Export</h3>
        <p style="color: #94a3b8; font-size: 14px;">Bezpieczny zapis zweryfikowanych raportów do formatów CSV oraz JSON dla systemów ERP.</p>
    </div>
</div>

<!-- Ładowanie Three.js i bezpieczny skrypt inicjalizujący -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    window.addEventListener('DOMContentLoaded', () => {
        const container = document.getElementById('canvas3d-container');
        if (!container) return;

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        // Geometria pulsującego rdzenia
        const geometry = new THREE.IcosahedronGeometry(2, 2);
        const material = new THREE.MeshBasicMaterial({ 
            color: 0x0ea5e9, 
            wireframe: true,
            transparent: true,
            opacity: 0.7
        });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        // Cząsteczki w tle
        const particlesGeo = new THREE.BufferGeometry();
        const count = 120;
        const positions = new Float32Array(count * 3);
        for(let i = 0; i < count * 3; i++) {
            positions[i] = (Math.random() - 0.5) * 12;
        }
        particlesGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const particlesMat = new THREE.PointsMaterial({ color: 0x38bdf8, size: 0.06 });
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
            let scaleFactor = 1 + Math.sin(elapsedTime * 3) * 0.07;
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
</script>
