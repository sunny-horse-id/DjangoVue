<template>
  <div>
    <button @click="toggleAnimation">{{ isPlaying ? '暂停动画' : '播放动画' }}</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';

function setupAnimation(fbxPath, wavPath) {
  let isPlaying = ref(false);
  let scene, renderer, camera;
  let mixer;
  let clock = new THREE.Clock();
  let backgroundMusic;

  window.addEventListener('resize', function () {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  function initRenderer() {
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
  }

  function initControls() {
    // eslint-disable-next-line no-unused-vars
    const controls = new OrbitControls(camera, renderer.domElement);
  }

  function initScene() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xa0a0a0);
  }

  function initAxesHelper() {
    const axesHelper = new THREE.AxesHelper(1);
    scene.add(axesHelper);
  }

  function initLight() {
    const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444);
    scene.add(hemiLight);
  }

  function initMeshes() {
    const loader = new FBXLoader();
    loader.load(fbxPath, function (fbx) {
      fbx.scale.set(0.1, 0.1, 0.1);
      fbx.position.set(30, -15, 5);
      scene.add(fbx);
      mixer = new THREE.AnimationMixer(fbx);
      const action = mixer.clipAction(fbx.animations[0]);
      action.play();
    });
  }

  function initCamera() {
    camera = new THREE.PerspectiveCamera(
        45, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(10, 20, 30);
  }

  function initBackgroundMusic() {
    backgroundMusic = new Audio(wavPath);
    backgroundMusic.loop = true;
    backgroundMusic.volume = 0.5; // Adjust volume as needed
  }

  function animate() {
    let delta = clock.getDelta();
    requestAnimationFrame(animate);
    if (mixer && isPlaying.value) {
      mixer.update(delta);
      if (backgroundMusic.paused) {
        backgroundMusic.play();
      }
    } else {
      backgroundMusic.pause();
    }
    renderer.render(scene, camera);
  }

  function toggleAnimation() {
    isPlaying.value = !isPlaying.value;
  }

  initRenderer();
  initScene();
  initAxesHelper();
  initCamera();
  initLight();
  initMeshes();
  initControls();
  initBackgroundMusic();
  animate();

  return {
    toggleAnimation
  };
}

const { toggleAnimation } = setupAnimation('model/fbx/test_BecauseYouAreBeautiful.fbx', 'music/BecauseYouAreBeautiful.wav');
</script>


<style scoped>
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  outline: none;
}

button:hover {
  background-color: #0056b3;
}
</style>