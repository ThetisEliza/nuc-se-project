<script setup>
import HelloWorld from './components/HelloWorld.vue'
import GroupList  from './views/GroupList.vue';
import NavBar  from './views/layout/NavBar.vue';
</script>

<template>
  <!-- <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" /> -->
  <div>
    <v-icon icon="mdi-home" />
    <NavBar />
    <GroupList />
  </div>
  
</template>

<script>

export default {
  components: {
    NavBar,
  }
}
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
