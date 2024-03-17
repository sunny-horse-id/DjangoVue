<template>
  <div ref="container"></div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';

export default {
  name: 'ThreeJsModelViewer',
  data() {
    return {
      scene: null,
      renderer: null,
      camera: null,
      mixer: null,
      clock: new THREE.Clock()
    };
  },
  mounted() {
    this.initRenderer();
    this.initScene();
    this.initAxesHelper();
    this.initCamera();
    this.initLight();
    this.initMeshes();
    this.initControls();
    this.animate();

    window.addEventListener('resize', this.onWindowResize);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.onWindowResize);
  },
  methods: {
    initRenderer() {
      this.renderer = new THREE.WebGLRenderer({ antialias: true });
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.$refs.container.appendChild(this.renderer.domElement);
    },
    initControls() {
      this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    },
    initScene() {
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0xa0a0a0);
    },
    initAxesHelper() {
      const axesHelper = new THREE.AxesHelper(1);
      this.scene.add(axesHelper);
    },
    initLight() {
      const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444);
      this.scene.add(hemiLight);
    },
    initMeshes() {
      const loader = new FBXLoader();
      loader.load('../assets/model/test.fbx', fbx => {
        fbx.scale.set(0.5, 0.5, 0.5);
        fbx.position.set(10, 10, 10);
        this.scene.add(fbx);
        this.mixer = new THREE.AnimationMixer(fbx);
        const action = this.mixer.clipAction(fbx.animations[0]);
        action.play();
      });
    },
    initCamera() {
      this.camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000);
      this.camera.position.set(1, 2, -3);
    },
    animate() {
      if (!this.mixer || !this.renderer || !this.scene || !this.camera) return;

      let delta = this.clock.getDelta();
      requestAnimationFrame(this.animate);
      this.mixer.update(delta);
      this.renderer.render(this.scene, this.camera);
    },
    onWindowResize() {
      this.camera.aspect = window.innerWidth / window.innerHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
  }
};
</script>

<style>
#container {
  width: 100%;
  height: 100%;
}
</style>