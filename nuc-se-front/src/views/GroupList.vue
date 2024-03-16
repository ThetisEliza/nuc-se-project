<template>
    <div>
        <v-container>
            <v-row justify="center">
            <v-col cols="auto">
                <v-btn size="x-small">Extra small Button</v-btn>
            </v-col>

            <v-col cols="auto">
                <v-btn size="small">Small Button</v-btn>
            </v-col>

            <v-col cols="auto">
                <v-btn>Regular Button</v-btn>
            </v-col>

            <v-col cols="auto">
                <v-btn size="large">Large Button</v-btn>
            </v-col>

            <v-col cols="auto">
                <v-btn size="x-large">X-Large Button</v-btn>
            </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script lang="js">
import groupService from '../services/postService'
import { NButton, useMessage } from 'naive-ui'
import { defineComponent } from 'vue'

const createColumns = () => {
  return [
    {
      title: 'Name',
      key: 'name'
    },
    {
      title: 'Score',
      key: 'score'
    },
  ]
}

export default defineComponent({
    setup () {
        return {
            groups: [],
            columns: createColumns(),
            currentPage: 1,
            NumPerPage: 5,
        }
    }, 


    mounted() {
        // this.getAllGroups()
        this.getPageGroups(1, 5)
    },

    methods: {
        getAllGroups() {
            groupService.getAllGroups()
                .then(res=>{
                    this.groups = res.data
                })
        },

        getPageGroups(pageNum) {
            groupService.getPageGroups({pageNum: pageNum, pageSize: this.NumPerPage})
                .then(res=>{
                    this.currentPage = pageNum
                    this.groups = res.data.groups
                })
        }
    }
})

</script>

<style>
</style>