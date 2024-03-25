/*
 * @Date: 2024-03-25 11:31:41
 * @LastEditors: ThetisEliza wxf199601@gmail.com
 * @LastEditTime: 2024-03-25 14:40:04
 * @FilePath: \nuc-se-front\src\services\storageService.js
 */
import Vuex from 'vuex'

const PREFIX="USER"

//save
const set = (key, data) => {
    console.log(key, data)
    return localStorage.setItem(key, data)
}

//load
const get = (key) => localStorage.getItem(key)

const remove = (key) => localStorage.removeItem(key)

const actions = {

}

const mutations = {

}

const state = {

}

const store = new Vuex.Store({
    actions, mutations, state
})

export default {
    PREFIX,
    set,
    get,
    remove,
    store
}