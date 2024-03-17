<template>
    <v-app>
        <v-sheet class="mx-auto" width="300">
            <v-form 
                v-model="form"
                @submit.prevent="onSubmit"
            >
                <v-text-field
                    v-model="username"
                    :rules="[validEmpty]"
                    placeholder="username"
                    hint="Enter The Admin username"
                ></v-text-field>
                <v-text-field
                    v-model="password"
                    :rules="[validEmpty]"
                    placeholder="password"
                    hint="Enter password to access admin control"
                    type="password"
                ></v-text-field>
                <v-btn
                    :disabled="!form"
                    :loading="loading"
                    color="success"
                    size="large"
                    type="submit"
                    variant="elevated"
                    block
                    >
                    Sign In
                </v-btn>

            </v-form>
        </v-sheet>
    </v-app>
</template>

<script lang="js">
import adminService  from '../services/adminService'
import { defineComponent } from 'vue'

export default defineComponent({
    setup () {
        
    }, 

    data: () => ({
        form: false,
        username: null,
        password: null,
        loading: false,
        error_msg: null,
    }),

    methods: {
        validEmpty(value) {
            return !! value || 'Field is required'
        },

        onSubmit() {
            if (!this.form) return
            this.loading = true
            adminService.login(this.username, this.password)
                .then(res => {
                    this.loading = false 
                    console.log(res, res.data)
                    if (res.data.status == 0) {
                        this.$router.push({name: "edit"})
                    }
                    else {
                        this.err_msg = res.data.msg
                        setTimeout(() => (this.err_msg = ""), 2000)
                    }                    
                })
                .catch(err => {
                    this.loading = false      
                   
                })
        }
    }
})

</script>

<style>

</style>