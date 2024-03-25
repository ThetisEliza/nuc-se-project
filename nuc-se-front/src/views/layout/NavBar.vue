<!--
 * @Date: 2024-03-18 14:38:26
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2024-03-18 15:58:26
 * @FilePath: \nuc-se-front\src\views\layout\NavBar.vue
-->
<template>
    <!-- <v-app> -->
      <v-container>
        <v-app-bar :elevation="10" rounded scroll-threshold="5" scroll-behavior="hide">
          <template v-slot:prepend>
            <v-btn icon="mdi-home" @click="onHomeIcon"></v-btn>
          </template>
        
          <v-app-bar-title>NUC-SE-Project</v-app-bar-title>
        
          <template v-slot:append>
            <!-- <v-btn icon="mdi-magnify"></v-btn> -->
            <v-btn v-if="user != null">{{ user }}</v-btn>
            <v-btn @click="$router.push({name: 'login'})"> 登录 </v-btn>
          </template>
        </v-app-bar>
      </v-container>
    <!-- </v-app> -->
  </template>

<script lang="js">

import { defineComponent } from 'vue'

export default defineComponent({
  data: () => ({
    user: "A",
  }),

  methods: {
    onHomeIcon() {
      this.$router.push({name: 'home'})
    },

    
  }
})

</script>

<style>

</style>