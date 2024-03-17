<template>
    <div>
        <v-data-table-server
            v-model:items-per-page="groupsPerPage"
            :headers="headers"
            :items="groups"
            :items-length="totalGroups"
            :loading="loading"
            :hover
            item-value="name"
            @update:options="loadItems"
        ></v-data-table-server>
    </div>
</template>

<script lang="js">
import groupService from '../services/postService'
import { defineComponent } from 'vue'


export default defineComponent({
    
    data: () => ({
        itemsPerPage: 5,
        headers: [
            { title: 'Name', key: 'name', align: 'end'},
            { title: 'Score', key: 'score', align: 'end' },],
        groups: [],
        totalGroups: 30,
        loading: true,
    }),

    methods: {

        loadItems({ page, itemsPerPage, sortBy }) {
            console.log({pageNum: page, groupsPerPage: itemsPerPage, sortBy: sortBy})
            groupService.getPageGroups({pageNum: page, groupsPerPage: itemsPerPage, sortBy: sortBy})
                .then(res=>{
                    this.$data.groups = res.data.groups
                    this.$data.totalGroups = res.data.total
                    this.$data.loading = false
                })
        },
    }
})

</script>

<style>
</style>