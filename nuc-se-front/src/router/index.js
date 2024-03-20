import GroupList from "@/views/GroupList.vue"
import adminRoutes from "./admin";
import storageService from "../services/storageService";
import { createRouter, createWebHistory  } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: "home",
            component: GroupList
        },
        ...adminRoutes,
    ]
})

router.beforeEach((to, from, next) => {
    if (to.meta.auth) {
        if (storageService.get(storageService.PREFIX) != null) {
            next()
        } else {
            router.push({name: 'login'})
        }
    } else {
        next()
    }
    
})

export default router;