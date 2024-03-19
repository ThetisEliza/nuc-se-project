<template>
    <div>
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
                :items="groups"
                :items-length="totalGroups"
                :loading="loading"
                :headers="headers"
                item-value="name"
                items-per-page-text="每页"
                @update:options="loadItems"
            >

                <template v-slot:item.members="{ item }">
                    <v-chip v-for="member in item.members" color="primary">{{ member.name }}</v-chip>
                </template>

                <template v-slot:item.edit="{ item }">
                    <v-btn v-bind="props" color="red"
                    @click="dialogOpen(item)"
                    >编辑
                    </v-btn>
                </template>
        
            </v-data-table-server>

        </v-card>
       

        <v-dialog
        v-model="editing"
        max-width="600"
        >

            <v-card>
                <v-card-text>编辑团队信息</v-card-text>
                <v-card-text>
                    
                    <v-row dense>
                        <v-col
                            cols="12"
                            md="4"
                            sm="6"
                        >
                        <v-text-field
                            variant="outlined"
                            v-model="editingAddScore"
                            label="添加分数"
                        ></v-text-field>

                        <text>分数预览：{{ parseInt(editingGroup.score) + parseInt(editingAddScore) }}</text>
                        </v-col>
                    </v-row>
                    
                </v-card-text>

                <v-divider></v-divider>

                
                <!-- <v-card-actions>
                    <v-chip-group>                     
                        <v-flex>
                            <v-chip 
                                v-for="member in editingGroup.members"
                                closable
                            >
                                {{ member.name }}
                            </v-chip>
                        </v-flex>
                    </v-chip-group>
                </v-card-actions>

                <v-card-actions>
                    <v-btn>
                        添加成员
                    </v-btn>

                    <v-btn>
                        解散团队
                    </v-btn>
                </v-card-actions> -->


                <v-divider></v-divider>


                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                    color="red"
                    @click="dialogConfirm()"
                    >
                    确认
                    </v-btn>
                    <v-btn
                    color="green"
                    @click="dialogCancel()"
                    >
                    取消
                    </v-btn>

                </v-card-actions>
            </v-card>
            
            
           

        </v-dialog>
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
            { title: '分数', key: 'score', align: 'gead' },
            { title: '平时分', key: 'regularScore', align: 'gead' },
            { title: '修改时间', key: 'modifyTimestamp', align: 'gead' },
            { title: '查看成员', key: 'members', align: 'head' },
            { title: '', key: 'edit', align: 'end' },
        ],
        groups: [],
        totalGroups: 30,
        loading: true,

        editing: false,
        editingAddScore: 0,
        editingGroup: null,    
        search: "",    
    }),

    mounted() {
        this.loadItems({page: 1, itemsPerPage: this.$data.itemsPerPage, sortBy: ""})
    },

    methods: {

        loadItems({ page, itemsPerPage, sortBy, search }) {
            groupService.getPageGroups({pageNum: page, groupsPerPage: itemsPerPage, sortBy: sortBy})
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


        dialogOpen(group) {
            this.$data.editing = true
            this.$data.editingScore = group.score
            this.$data.editingGroup = group
        },

        dialogConfirm() { 
            if (this.$data.editingGroup.score != this.$data.editingScore) {
                
                groupService.modifyGroupScore({groupId:this.$data.editingGroup._id, score:this.$data.editingScore, type:"score"})
                    .then(res=>{
                        if (res.data.status == 0) {
                            this.$data.editingGroup.score =  this.$data.editingScore
                            this.$data.editing = false
                            this.loadItems({ page, itemsPerPage, sortBy })
                        }
                    })
            }
        },

        dialogCancel() { 
            this.$data.editing = false
        }
    }
})

</script>

<style>
</style>