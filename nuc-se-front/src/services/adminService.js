import service from '../utils/request'

const login = (username, password) => {
    return service.post('admin/login',  {username:username, password:password})
}

export default {
    login
}