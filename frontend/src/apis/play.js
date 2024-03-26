import request from "@/utils/request.js"

export const PlayMulAddress = () => {
    return request.get('/mulAddress')
}