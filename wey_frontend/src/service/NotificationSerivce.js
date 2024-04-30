import axios from 'axios'
const BASE_DIR='api/notification'
export default {
    async get_list_notifications(){
        return await axios.get(`${BASE_DIR}/`)
    }






}