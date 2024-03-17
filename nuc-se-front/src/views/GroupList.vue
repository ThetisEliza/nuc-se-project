<template>
    <div>
        <v-data-table-server
            v-model:items-per-page="groupsPerPage"
            :items="groups"
            :items-length="totalGroups"
            :loading="loading"
            :headers="headers"
            item-value="name"
            @update:options="loadItems"
        >
            <template v-slot:item.members="{ item }">
                <v-tooltip>
                    <template v-slot:activator="{ props }">
                        <v-btn v-bind="props" color="indigo-lighten-1">View</v-btn>
                    </template>
                    <span v-for="member in item.members">{{ member.name }}</span>
                </v-tooltip>
            </template>
    
        </v-data-table-server>
    </div>
</template>

<script lang="js">
import groupService from '../services/postService'
import { defineComponent } from 'vue'


export default defineComponent({
    
    data: () => ({
        itemsPerPage: 5,
        headers: [
            { title: 'Name', key: 'name', align: 'head'},
            { title: 'Score', key: 'score', align: 'end' },
            { title: 'Regular Score', key: 'regularScore', align: 'end' },
            { title: 'Last Modify Timestamp', key: 'modifyTimestamp', align: 'end' },
            { title: 'ViewMembers', key: 'members', align: 'end' },
        ],
        groups: [],
        totalGroups: 30,
        loading: true,
    }),

    methods: {

        loadItems({ page, itemsPerPage, sortBy }) {
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