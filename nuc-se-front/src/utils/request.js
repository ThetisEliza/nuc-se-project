import axios from "axios"

const service = axios.create({
    baseURL: "http://47.94.152.114:8080/api/",
    timeout: 5000
})

export default service