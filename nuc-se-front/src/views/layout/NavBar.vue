<template>
    <!-- <v-app> -->
      <v-container>
        <v-app-bar :elevation="10" rounded scroll-threshold="5" scroll-behavior="hide">
          <template v-slot:prepend>
            <v-btn icon="mdi-home" @click="onHomeIcon"></v-btn>
          </template>
        
          <v-app-bar-title>Application Bar</v-app-bar-title>
        
          <template v-slot:append>
            <v-btn icon="mdi-magnify"></v-btn>
            <v-btn @click="$router.push({name: 'login'})"> Admin Login </v-btn>
          </template>
        </v-app-bar>
      </v-container>
    <!-- </v-app> -->
  </template>

<script lang="js">

import { defineComponent } from 'vue'

export default defineComponent({
  methods: {
    onHomeIcon() {
      this.$router.push({name: 'home'})
    }
  }
})

</script>

<style>

</style>