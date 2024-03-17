const adminRoutes = [
    {
        path: '/login',
        name: "login",
        component: () => import('@/views/AdminLogin.vue')
    },
    {
        path: '/edit',
        name: "edit",
        component: () => import('@/views/AdminEdit.vue')
    },
]

export default adminRoutes;