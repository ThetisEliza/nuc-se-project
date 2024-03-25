const adminRoutes = [
    {
        path: '/login',
        name: "login",
        component: () => import('@/views/AdminLogin.vue')
    },
    {
        path: '/edit',
        name: "edit",
        meta: {
            auth: true
        },
        component: () => import('@/views/AdminEdit.vue')
    },
]

export default adminRoutes;