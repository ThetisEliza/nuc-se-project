import GroupList from "@/views/GroupList.vue"
import adminRoutes from "./admin";

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
    next()
})

export default router;