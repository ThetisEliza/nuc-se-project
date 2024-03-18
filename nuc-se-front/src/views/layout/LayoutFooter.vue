<!--
 * @Date: 2024-03-18 14:38:26
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2024-03-18 16:02:38
 * @FilePath: \nuc-se-front\src\views\layout\LayoutFooter.vue
-->
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
                href="https://github.com/ThetisEliza/nuc-se-project"
            ></v-btn>
            </div>

            <div class="pt-0">
            软件工程课程作业    团队：软件工程学到死队  贡献者：马飞燕、安霞丽、赵悦涵、任世然、李志鹏、张程
            </div>

            <v-divider></v-divider>

            <div>
            {{ new Date().getFullYear() }} — <strong>NUC</strong>
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
        'mdi-github',
      ],
    }),
})

</script>

<style>

</style>