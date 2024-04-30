import axios from 'axios'

const BASE_DIR = '/api/'

export default {

    async sendFriendRequest(user_id){

        try{
            const response = await axios.post(`${BASE_DIR}friends/request/${user_id}/`)
            return {'resquest':response.data}
        }catch(error){
            console.log(error)
        }
       
    },
    async handleFriendRequest(friendship_id,status){
        try{
            const response = await axios.post(`${BASE_DIR}friends/${friendship_id}/${status}/`)          
            return response.data
        }catch(error){
            console.log(error)
        }
    },


    async getFriendRequest(){
        try{
            const response = await axios.get(`${BASE_DIR}friends/all_request/`)          
            return {'resquest':response.data}
        }catch(error){
            console.log(error)
        }        
    },


    async getFriendRequestSend(){
        
    },


    async getFriends(user_id){

        try{
            return await axios.get(`${BASE_DIR}friends/${user_id}/`)  

        }catch(error){
            throw error
        }

    }
    















}