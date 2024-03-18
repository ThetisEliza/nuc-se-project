<!--
 * @Date: 2024-03-18 14:38:26
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2024-03-18 16:04:31
 * @FilePath: \nuc-se-front\src\views\GroupList.vue
-->
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
                        <v-btn v-bind="props" color="indigo-lighten-1">查看</v-btn>
                    </template>
                    <span v-for="member in item.members">{{ member.name }}, </span>
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
            { title: '团队名称', key: 'name', align: 'head'},
            { title: '分数', key: 'score', align: 'end' },
            { title: '平时分', key: 'regularScore', align: 'end' },
            { title: '修改时间', key: 'modifyTimestamp', align: 'end' },
            { title: '查看成员', key: 'members', align: 'end' },
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
                    this.$data.groups.forEach(group => {
                        group.regularScore = parseInt(group.regularScore)
                        group.modifyTimestamp = new Date(group.modifyTimestamp*1000).toLocaleString()
                    });
                    this.$data.totalGroups = res.data.total
                    this.$data.loading = false
                })
        },
    }
})

</script>

<style>
</style>