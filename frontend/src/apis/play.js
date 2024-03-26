import request from "@/utils/request.js"

export const getAddressAPI = () => {
    return request.get('/mulAddress')
}