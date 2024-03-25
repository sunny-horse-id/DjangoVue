import request from "@/utils/request.js"

export const PlayAddress = () => {
    return request.get('/address')
}