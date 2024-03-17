<template>
    <v-app>
        
        <v-footer
            class="bg-indigo-lighten-1 text-center d-flex flex-column"
        >
            <div>
            <v-btn
                v-for="icon in icons"
                :key="icon"
                :icon="icon"
                class="mx-4"
                variant="text"
            ></v-btn>
            </div>

            <div class="pt-0">
             asdkaskdaskdadkakdka
            </div>

            <v-divider></v-divider>

            <div>
            {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
            </div>
        </v-footer>
    </v-app>
</template>

<script lang="js">

import { defineComponent } from 'vue'

export default defineComponent({
    setup () {
        
    }, 

    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
})

</script>

<style>

</style>