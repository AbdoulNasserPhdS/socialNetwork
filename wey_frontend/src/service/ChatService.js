import axios from 'axios';

const BASE_DIR = '/api/conversion'


export default {

    async send_message(conversion_id,messages){

        try{
            const response = await axios.post(`${BASE_DIR}/${conversion_id}/send/`,messages);
            return response.data
        }catch(error){
            throw error
        }


    },

    async conversion_list(){
        const response = await axios.get(`${BASE_DIR}/`);
        return response.data
      
    },

    async conversion_detail(user_id){
        const response = await axios.get(`${BASE_DIR}/${user_id}/`);
        return {'conversion':response.data.conversion,'messages':response.data.messages}

    }


    // async conversion_detail_per_user_id(user_id){
    //     const response = await axios.get(`${BASE_DIR}/${user_id}/user/`);
    //     return {'conversion':response.data.conversion,'messages':response.data.messages}

    // }









}