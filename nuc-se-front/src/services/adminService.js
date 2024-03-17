import service from '../utils/request'

const login = (username, password) => {
    return service.get('admin/login',  {params:{username:username, password:password}})
}

export default {
    login
}