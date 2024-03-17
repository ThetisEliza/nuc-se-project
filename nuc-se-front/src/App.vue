<script setup>
// import HelloWorld from './components/HelloWorld.vue'
import GroupList  from './views/GroupList.vue';
import NavBar  from './views/layout/NavBar.vue';
import LayoutFooter from './views/layout/LayoutFooter.vue';
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
    <v-app>
      <NavBar />
      <v-main>
        <v-container>
          <div id="router-view">
            <router-view />
          </div>
        </v-container>
      
      </v-main>
      <LayoutFooter />
    </v-app>
      
  </div>
  
</template>

<script>

export default {
  components: {
    NavBar,
    GroupList,
    LayoutFooter,
  }
}
</script>

<style scoped>
</style>
