// postService.js

import axios from 'axios';

const BASE_DIR = '/api/posts/'

export default {

    async get_posts_list() {
        try {
            const response = await axios.get(BASE_DIR)
            return response.data
        } catch (error) {
            console.log('Get Data Error.')
            throw error
        };
    },


    async add_post(values) {
        return await axios.post(BASE_DIR + 'add/', values,{
            headers: {
                "Content-Type": "multipart/form-data",
            }})
    },


    async like_post(post_id) {
        console.log("like Post Service");
        try {
            const result = await axios.post(BASE_DIR + `like/${post_id}`);
            console.log(result)
            return { 'post': result.data.post }
        } catch (error) {
            throw error
        }
    },


    async get_list_posts_by_user(user_id) {
        try {
            const response = await axios.get(BASE_DIR + `profile/${user_id}/`);
            console.log('data', response.data.data)
            console.log('user', response.data.user)
            return { 'data': response.data.data, 'user': response.data.user }

        } catch (error) {
            throw error
        }
    },


    async commentPost(values, post_id) {
        const response = await axios.post(BASE_DIR + `comment/${post_id}/`, values)
        return response.data.post
    },


    async searchPostAndUsers(values) {

        console.log(values)
        try {
            const response = await axios.post("/api/search/", values);
            console.log(response.data);
            return { 'users': response.data.users, 'posts': response.data.posts }
        } catch (error) {
            throw error
        }
    },


    async get_trends(){
        return await axios.get(`${BASE_DIR}trends/`)
    }







}