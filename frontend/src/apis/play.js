import request from "@/utils/request.js"

// 获取fbx和wav的地址
export const getAddressAPI = () => {
    return request.get('/mulAddress')
}

// fbx下载
export const downloadAPI = (arr) => {
    return request.get('/export', arr)
}