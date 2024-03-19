const PREFIX="USER"

//save
const set = (key, data) => {
    console.log(key, data)
    return localStorage.setItem(key, data)
}

//load
const get = (key) => localStorage.getItem(key)

const remove = (key) => localStorage.removeItem(key)

export default {
    PREFIX,
    set,
    get,
    remove
}