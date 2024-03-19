<!--
 * @Date: 2024-03-18 14:38:26
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2024-03-18 16:07:30
 * @FilePath: \nuc-se-front\src\views\AdminLogin.vue
-->
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
                    placeholder="管理员用户名"
                    hint="输入管理员用户名"
                ></v-text-field>
                <v-text-field
                    v-model="password"
                    :rules="[validEmpty]"
                    placeholder="密码"
                    hint="输入管理员用户密码"
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
                    登录
                </v-btn>

            </v-form>
        </v-sheet>
    </v-app>
</template>

<script lang="js">
import adminService  from '../services/adminService'
import storageService from '../services/storageService'
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
            return !! value || '输入不能为空'
        },

        onSubmit() {
            if (!this.form) return
            this.loading = true
            adminService.login(this.username, this.password)
                .then(res => {
                    this.loading = false 
                    if (res.data.status == 0) {
                        storageService.set(storageService.PREFIX, this.username)
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