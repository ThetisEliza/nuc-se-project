import request from '../utils/request'

const getAllGroups = () => {
    return request.get("groups/all")
}

const getPageGroups = ({pageNum, pageSize}) => {
    return request.get("groups/page", {params: {pageNum: pageNum, pageSize: pageSize}})
}

export default {
    getAllGroups,
    getPageGroups,
}