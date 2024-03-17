import service from '../utils/request'

const getAllGroups = () => {
    return service.get("groups/all")
}

const getPageGroups = ({pageNum, groupsPerPage, sortBy}) => {
    return service.get("groups/page", {params: {pageNum: pageNum, pageSize: groupsPerPage, sortBy: sortBy}})
}

const modifyGroupScore = ({groupId, score, type}) => {
    return service.get("group/modifyscore", {params: {groupId: groupId, score: score, type: type}})
}

export default {
    getAllGroups,
    getPageGroups,
    modifyGroupScore,
}