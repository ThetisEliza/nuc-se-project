<template>
    <div>
        <v-list lines="one">
            <v-table>
                <thead>
                <tr>
                    <th class="text-left">
                    Name
                    </th>
                    <th class="text-left">
                    Score
                    </th>
                    <th class="text-left">
                    Regular Score
                    </th>
                    <th class="text-left">
                    Members
                    </th>
                    <th class="text-left">
                    Opt
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
                    <td>{{ 0 }}</td>
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
                        >Edit</v-btn>
                        <v-dialog
                        v-model="editDialog"
                        width="auto"
                        >
                            <v-container>
                                <v-card
                                min-width="500"
                                min-height="700"
                                text="Group Edit"
                                >
                                    <v-form>
                                        <v-text-field
                                            variant="outlined"
                                            v-model="editingScore"
                                            label="score"
                                        > 
                                            
                                        </v-text-field>
                                            
                                        <v-text-field
                                            variant="outlined"
                                            v-model="editingRegularScore"
                                            label="regular score"
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
                                                    AddMember
                                                </v-btn>

                                                <v-btn>
                                                    Dismiss Group
                                                </v-btn>
                                            </v-row>
                                        </v-container>
                                        
                                        
                                        
                                        <v-divider class="border-opacity-75" color="info"
                                        ></v-divider>
                                        
                                        <v-container>
                                            <v-btn
                                            @click="dialogConfirm()"
                                            >
                                                Confirm
                                            </v-btn>
                                            <v-btn
                                            @click="dialogCancel()"
                                            >
                                                Cancel
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
        editingRegularScore: 0,
        editingGroup: null,

        itemsPerPage: 5,
        groups: [],
        totalGroups: 30,
        loading: true,
    }),

    mounted() {
        this.loadItems({page: 1, itemsPerPage: this.$data.itemsPerPage, sortBy: ""})
    },

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


        dialogOpen({ group }) {
            this.$data.editDialog = true
            this.$data.editingScore = group.score
            this.$data.editingRegularScore = group.score
            this.$data.editingGroup = group
        },

        dialogConfirm() { 
            this.$data.editDialog = false
            this.$data.editingGroup.score =  this.$data.editingScore
        },

        dialogCancel() { 
            this.$data.editDialog = false
        }
    }
})

</script>

<style>
</style>