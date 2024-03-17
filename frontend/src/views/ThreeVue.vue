<script setup>
import {onMounted} from "vue";
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js'; // 导入FBXLoader
onMounted(() => {
  let scene, renderer, camera;
  let mixer;

  let clock = new THREE.Clock();

  initRenderer();
  initScene();
  initAxesHelper();
  initCamera();
  initLight();
  initMeshes();
  initControls();
  animate();

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
    const loader = new FBXLoader(); // 使用FBXLoader加载FBX文件
    loader.load('model/fbx/test_BecauseYouAreBeautiful.fbx', function (fbx) { // 替换为你的FBX文件路径
      console.log(fbx);

      // 设置模型的缩放比例
      fbx.scale.set(0.1, 0.1, 0.1); // 替换为你希望的缩放比例

      // 设置模型的位置 R G B
      fbx.position.set(30, -15, 5); // 替换为你希望的位置坐标
      scene.add(fbx);

      // 查找动画
      mixer = new THREE.AnimationMixer(fbx);
      const action = mixer.clipAction(fbx.animations[0]); // 假设只有一个动画，选择第一个动画
      action.play(); // 播放动画
    });
  }

  function initCamera() {
    camera = new THREE.PerspectiveCamera(
        45, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(10, 20, 30);
  }

  function animate() {
    let delta = clock.getDelta();

    requestAnimationFrame(animate);
    if (mixer) {
      mixer.update(delta); // 更新动画
    }
    renderer.render(scene, camera);
  }
})
</script>

<template>
  <span></span>
</template>

<style scoped>

</style>