<template>
    <div>
        <b-container >
            <b-list-group>
                <b-list-group-item v-for="item in groups">
                    <p>{{ item.name }}:{{ item.score }}</p>
                </b-list-group-item>
            </b-list-group>
        </b-container>
    </div>
</template>

<script>
import groupService from '../services/postService'

export default {
    components: {

    },

    data() {
        return {
            currentPage: 1,
            NumPerPage: 5,
            groups: []
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
                    this.$data.groups = res.data
                })
        },

        getPageGroups(pageNum) {
            groupService.getPageGroups({pageNum: pageNum, pageSize: this.$data.NumPerPage})
                .then(res=>{
                    this.$data.currentPage = pageNum
                    this.$data.groups = res.data.groups
                })
        }
    }
}

</script>

<style>
</style>