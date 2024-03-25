import service from '../utils/request'

const getAllGroups = () => {
    return service.get("groups/all")
}

const getPageGroups = ({pageNum, groupsPerPage, sortBy, order}) => {
    return service.get("groups/page", {params: {pageNum: pageNum, pageSize: groupsPerPage, sortBy: sortBy, order: order}})
}

const modifyGroupScore = ({groupId, score, type}) => {
    return service.get("group/modifyscore", {params: {groupId: groupId, score: score, type: type}})
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
    dismissGroup,
    createGroup,
    getSpareMembers
}