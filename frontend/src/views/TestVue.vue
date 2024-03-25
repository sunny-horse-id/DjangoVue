<!-- ParentComponent.vue -->
<template>
  <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
    <el-tab-pane v-for="(item, index) in address" :key="index" :label="`File ${index}`" :name="`file_${index}`">
      <div class="button-download">
        <button @click="download">下载</button>
      </div>
      <div class="button-wrapper">
        <button @click="toggleAnimation">{{ isPlaying ? '暂停动画' : '播放动画' }}</button>
      </div>
      {{ item }}
    </el-tab-pane>
  </el-tabs>
</template>

<script setup>
import {ref, watch} from 'vue'
import {PlayMulAddress} from "@/apis/play.js";
import * as THREE from "three";
import {OrbitControls} from "three/addons/controls/OrbitControls.js";
import {FBXLoader} from "three/addons/loaders/FBXLoader.js";
const activeName = ref('file_0')
const address = ref([])
//调用接口
const getAddress = async () => {
  address.value = (await PlayMulAddress()).data
}
getAddress()
const isPlaying = ref(false);
const selectedFile = ref(0)
// eslint-disable-next-line no-unused-vars
const handleClick = (tab, event) => {

}

watch(activeName, (newValue) => {
  selectedFile.value = newValue.split('_')[1]
})

watch(selectedFile, (newValue) => {
  //console.log(selectedFile)
  setupAnimation(address.value[newValue][0], address.value[newValue][1]);
  isPlaying.value = false
});



function setupAnimation(fbxPath, wavPath) {
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

  initRenderer();
  initScene();
  initAxesHelper();
  initCamera();
  initLight();
  initMeshes();
  initControls();
  initBackgroundMusic();
  animate();

}

function toggleAnimation() {
  isPlaying.value = !isPlaying.value;
}

watch(address, (newValue) => {
  setupAnimation(newValue[0][0], newValue[0][1]);
});


function download() {
  const url = address.value[selectedFile.value][2]; // 文件的下载链接
  const link = document.createElement('a');
  link.href = url;
  link.download = address.value[selectedFile.value][3]; // 设置下载的文件名
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
</script>

<style>
.demo-tabs {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
.button-download {
  position: fixed;
  top: 20px;
  right: 150px; /* 将右侧间距调整为适当的距离 */
  z-index: 999;
}

.button-wrapper {
  position: fixed;
  top: 20px;
  right: 20px; /* 将右侧间距调整为适当的距离 */
  z-index: 999;
}

/* 下载按钮样式 */
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  outline: none;
  margin-right: 10px; /* 添加右侧间距，使其与播放按钮有一定的距离 */
}

/* 鼠标悬停时的样式 */
button:hover {
  background-color: #0056b3;
}
</style>