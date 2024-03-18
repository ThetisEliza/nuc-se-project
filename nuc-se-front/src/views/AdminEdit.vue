<template>
    <div>
        <v-list lines="one">
            <v-table>
                <thead>
                <tr>
                    <th class="text-left">
                    团队名称
                    </th>
                    <th class="text-left">
                    得分
                    </th>
                    <th class="text-left">
                    平时分
                    </th>
                    <th class="text-left">
                    修改时间
                    </th>
                    <th class="text-left">
                    成员
                    </th>
                    <th class="text-left">
                    操作
                    </th>
                </tr>
                </thead>

                <tbody>
                <tr
                    v-for="group in groups"
                    :key="group.name"
                >
                    <td>{{ group.name }}</td>
                    <td>{{ group.score }}</td>
                    <td>{{ group.regularScore }}</td>
                    <td>{{ group.modifyTimestamp }}</td>
                    <td>
                        <div>
                            <v-chip size="small" 
                            color="primary"
                            v-for="member in group.members" 
                            :key="member.name">{{ member.name }}</v-chip>
                        </div>
                    </td>
                    <td>
                        <v-btn size="small" 
                        color="red"
                        @click="dialogOpen({group: group})"
                        >编辑</v-btn>
                        <v-dialog
                        v-model="editDialog"
                        >
                            <v-container
                            widh="30%"
                            >
                                <v-card
                                text="Group Edit"
                                >
                                    <v-form>
                                        <v-text-field
                                            variant="outlined"
                                            v-model="editingScore"
                                            label="score"
                                        > 
                                            
                                        </v-text-field>
                                        
                                        <v-container>
                                            <v-row justify="center">
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
                                        </v-row>

                                        </v-container>
                                        
                                        

                                        <v-divider class="border-opacity-75" color="info"
                                        ></v-divider>


                                        <v-container>
                                            <v-row>
                                                <v-btn>
                                                    添加成员
                                                </v-btn>

                                                <v-btn>
                                                    解散团队
                                                </v-btn>
                                            </v-row>
                                        </v-container>
                                        
                                        
                                        
                                        <v-divider class="border-opacity-75" color="info"
                                        ></v-divider>
                                        
                                        <v-container>
                                            <v-btn
                                            @click="dialogConfirm()"
                                            >
                                                确认
                                            </v-btn>
                                            <v-btn
                                            @click="dialogCancel()"
                                            >
                                                取消
                                            </v-btn>
                                        </v-container>
                                        
                                        
                                    </v-form>

                                </v-card>
                                
                            </v-container>
                            

                        </v-dialog>
                    </td>
                </tr>
                </tbody>
            </v-table>
        </v-list>
    </div>
</template>

<script lang="js">
import groupService from '../services/postService'
import { defineComponent } from 'vue'


export default defineComponent({
    
    data: () => ({
        editDialog: false,
        editingScore: 0,
        editingGroup: null,

        groups: [],
        totalGroups: 30,
        loading: true,
    }),

    mounted() {
        this.loadItems({page: 1, itemsPerPage: this.$data.itemsPerPage, sortBy: ""})
    },

    methods: {

        loadItems() {
            groupService.getAllGroups()
                .then(res=>{
                    this.$data.groups = res.data.groups
                    this.$data.groups.forEach(group => {
                        group.regularScore = parseInt(group.regularScore)
                        group.modifyTimestamp = new Date(group.modifyTimestamp*1000).toLocaleString()
                    });
                    this.$data.loading = false
                })
        },


        dialogOpen({ group }) {
            this.$data.editDialog = true
            this.$data.editingScore = group.score
            this.$data.editingGroup = group
        },

        dialogConfirm() { 
            if (this.$data.editingGroup.score != this.$data.editingScore) {
                
                groupService.modifyGroupScore({groupId:this.$data.editingGroup._id, score:this.$data.editingScore, type:"score"})
                    .then(res=>{
                        if (res.data.status == 0) {
                            this.$data.editingGroup.score =  this.$data.editingScore
                            this.$data.editDialog = false
                            this.loadItems()
                        }
                    })
            }
        },

        dialogCancel() { 
            this.$data.editDialog = false
        }
    }
})

</script>

<style>
</style>