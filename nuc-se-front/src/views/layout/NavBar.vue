<template>
    <v-app>
      <v-container>
        <v-app-bar :elevation="10" rounded>
          <template v-slot:prepend>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
          </template>
        
          <v-app-bar-title>Application Bar</v-app-bar-title>
        
          <template v-slot:append>
            <v-btn icon="mdi-heart"></v-btn>
        
            <v-btn icon="mdi-magnify"></v-btn>
        
            <v-btn icon="mdi-dots-vertical"></v-btn>
          </template>
        </v-app-bar>
      </v-container>
    </v-app>
  </template>

<script lang="js">

import { defineComponent } from 'vue'

export default defineComponent({
    setup () {
        
    }, 
})

</script>

<style>

</style>