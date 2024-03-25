<!--
 * @Date: 2024-03-18 14:38:26
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2024-03-18 16:04:31
 * @FilePath: \nuc-se-front\src\views\GroupList.vue
-->
<template>
    <v-card flat>
        <v-card-title class="d-flex align-center pe-2">
            <v-icon icon="mdi-account-multiple"></v-icon> &nbsp;
            团队

            <v-spacer></v-spacer>
            <v-text-field
                v-model="search"
                density="compact"
                label="查找团队"
                prepend-inner-icon="mdi-magnify"
                variant="solo-filled"
                flat
                hide-details
                single-line
            ></v-text-field>
        </v-card-title> 
        <v-divider></v-divider>
    
        <v-data-table-server
            v-model:items-per-page="itemsPerPage"
            
            :search="search"
            :items="groups"
            :items-length="totalGroups"
            :loading="loading"
            :headers="headers"
            item-value="name"
            items-per-page-text="每页"
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

    </v-card flat>
</template>

<script lang="js">
import groupService from '../services/groupService'
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
        search: "",
        page: 1,
    }),

    methods: {

        loadItems({ page, itemsPerPage, sortBy, search }) {
            let sort_key = ""
            let order = ""
            if(sortBy.length == 1){
                sort_key = sortBy[0].key
                order = sortBy[0].order
            } 
            groupService.getPageGroups({pageNum: page, groupsPerPage: itemsPerPage, sortBy: sort_key, order: order})
                .then(res=>{
                    res.data.groups.forEach(group => {
                        group.regularScore = parseInt(group.regularScore)
                        group.modifyTimestamp = new Date(group.modifyTimestamp*1000).toLocaleString()
                    })
                    let groups = res.data.groups.filter(group => {
                        if (search && !group.name.toLowerCase().includes(search.toLowerCase())) {
                            return false
                        }
                        return true;
                    })

                    this.$data.groups = groups;
                    this.$data.totalGroups = res.data.total
                    this.$data.loading = false
                })
        },

        pageCount () {
            return Math.ceil(this.$data.totalGroups / this.$data.itemsPerPage)
        },
    }
})

</script>

<style>
</style>