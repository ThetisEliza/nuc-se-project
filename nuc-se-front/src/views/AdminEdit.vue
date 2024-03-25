<!--
 * @Date: 2024-03-18 14:38:26
 * @LastEditors: ThetisEliza wxf199601@gmail.com
 * @LastEditTime: 2024-03-25 15:03:28
 * @FilePath: \nuc-se-front\src\views\AdminEdit.vue
-->
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
                <v-btn @click="dialogOpen()">
                    <template v-slot:prepend>
                        <v-icon color="success"  icon="mdi-plus"></v-icon>
                    </template>
                    添加团队
                </v-btn>
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
                    <v-btn color="red"
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
                    <v-text-field
                        variant="outlined"
                        v-model="editingAddScore"
                        label="添加分数"
                    ></v-text-field>

                    <text>分数预览：{{ previewScore() }}</text>
                </v-card-text>
                
                <v-card-text>
                    <v-text-field
                        variant="outlined"
                        v-model="editingTargetGroup.name"
                        label="团队名称"
                        :disabled="!newGroup"
                    ></v-text-field>
                </v-card-text>

                <v-divider></v-divider>

                <!-- <v-card-actions> -->
                <v-card-text>
                    
                    <v-select
                        :item-props="memberSelectProps"
                        :items="getAvailableMembers()"
                        v-model="editingTargetGroup.members"
                        label="成员"
                        chips
                        multiple
                    ></v-select>
                        
                        
                    <v-row justify="center">    
                        <v-btn 
                        v-if="!newGroup"
                        @click="revealConfirmDismiss = true"
                        color="red">
                            解散团队
                        </v-btn>
                    
                    </v-row>

                    
                </v-card-text>



                

                <v-expand-transition>
                    <v-card
                    v-if="revealConfirmDismiss"
                    class="v-card--reveal"
                    style="height: 100%;"
                    >
                        <v-card-text>
                            <p>
                                <strong  color="red">是否确认要解散团队?</strong>
                            </p>
                        </v-card-text>
                    </v-card>
                </v-expand-transition>

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
import groupService from '../services/groupService'
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
        editingTargetGroup: null,

        newGroup: false,
        revealConfirmDismiss: false,
        search: "",    

        editingMembers: [],
        spareMembers: [],
    }),

    mounted() {
        this.loadItems({page: 1, itemsPerPage: this.$data.itemsPerPage, sortBy: ""})
        this.getSpareMembers()
    },

    methods: {
        refreshGroups() {
            this.loadItems({page: 1, itemsPerPage: this.$data.itemsPerPage, sortBy: ""})
        },

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

        previewScore() {
            
            let a = parseInt( this.$data.editingAddScore );
            if(isNaN(a)) {
                a = 0
            }
            
            return a + this.$data.editingTargetGroup.score ;
        },

        dialogOpen(group) {
            this.$data.editingGroup = group
            this.$data.editingAddScore = 0
            this.getSpareMembers()

            if (group == null) {
                this.$data.editingTargetGroup = {name: "", score: 0, members: []}
                this.$data.newGroup = true                
            } else {
                this.$data.editingTargetGroup = JSON.parse(JSON.stringify(group))
                this.$data.newGroup = false
            }
            
            this.$data.editing = true
        },

        dialogConfirm() { 
            if (this.$data.newGroup) {
                groupService.createGroup({group: this.$data.editingTargetGroup}).then(res=>{
                    this.refreshGroups()
                })
            } else {
                if (this.$data.editingAddScore != 0) {
                    let newScore = this.previewScore()
                    this.$data.editingTargetGroup.score = newScore
                    groupService.modifyGroupScore({group: this.$data.editingTargetGroup})
                        .then(res=>{
                            if (res.data.status == 0) {
                                this.$data.editingGroup.score =  newScore
                                this.$data.editing = false
                            }
                            this.refreshGroups()
                        })
                }
                if (this.$data.revealConfirmDismiss) {
                    groupService.dismissGroup({group: this.$data.editingTargetGroup})
                        .then(res => {
                            this.refreshGroups()
                        })
                }
                if (JSON.stringify(this.$data.editingTargetGroup.members) != JSON.stringify(this.$data.editingGroup.members)) {
                    let targetMembers = this.$data.editingTargetGroup.members
                    let currentMembers = this.$data.editingGroup.members
                    let targetMemberNums = targetMembers.map(m_ => m_.num)
                    let currentMemberNums = currentMembers.map(m_ => m_.num)

                    groupService.modifyGroupMembers({group: this.$data.editingTargetGroup})
                        .then(res => {
                            this.refreshGroups()
                        })
                    // let shouldBeAddedMembers = targetMembers.filter(m => {
                    //     return !currentMemberNums.includes(m.num)
                    // })
                    // console.log("should be added", shouldBeAddedMembers)

                    // let shouldBeRemovedMembers = currentMembers.filter(m => {
                    //     return !targetMemberNums.includes(m.num)
                    // })
                    // console.log("should be removed", shouldBeRemovedMembers)
                }
            }
            this.$data.revealConfirmDismiss = false;
            this.$data.editing = false
        },

        dialogCancel() { 
            this.$data.editing = false
            this.$data.revealConfirmDismiss = false;
        },

        dismissGroup() {
            groupService.removeGroup({groupId: this.$data.editingGroup})
        },

        getAvailableMembers() {
            let members =  this.$data.editingGroup == null? []: this.$data.editingGroup.members
            let availableMembers = [...members, ...this.$data.spareMembers]
            return availableMembers
        },

        getSpareMembers() {
            groupService.getSpareMembers()
                .then(res => {
                    this.$data.spareMembers = res.data.spare_members
                })
        },

        memberSelectProps(item) {
            return {
                title: item.name,
                subtitle: item.num
            }
        }
    }
})

</script>

<style>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}
</style>