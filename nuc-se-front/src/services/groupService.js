/*
 * @Date: 2024-03-25 11:31:41
 * @LastEditors: ThetisEliza wxf199601@gmail.com
 * @LastEditTime: 2024-03-25 14:57:27
 * @FilePath: \nuc-se-front\src\services\groupService.js
 */
import service from '../utils/request'

const getAllGroups = () => {
    return service.get("groups/all")
}

const getPageGroups = ({pageNum, groupsPerPage, sortBy, order}) => {
    return service.get("groups/page", {params: {pageNum: pageNum, pageSize: groupsPerPage, sortBy: sortBy, order: order}})
}

const modifyGroupScore = ({group}) => {
    return service.post("group/modifyscore", {group: group})
}

const modifyGroupMembers = ({group}) => {
    return service.post("group/modifymembers", {group: group})
}

const dismissGroup = ({group}) => {
    return service.post("group/dismiss", {group: group})
}

const createGroup = ({group}) => {
    return service.post("group/create", {group: group})
}

const getSpareMembers = () => {
    return service.get("group/spares")
}

export default {
    getAllGroups,
    getPageGroups,
    modifyGroupScore,
    modifyGroupMembers,
    dismissGroup,
    createGroup,
    getSpareMembers
}