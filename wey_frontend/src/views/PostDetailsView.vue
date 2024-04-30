<template>
  <MobileHeader title="Chat" redirect_url="/chat" class="md:hidden"></MobileHeader>

  <PostListItem :post="post" :posts="posts"  />
</template>

<script>
import MobileHeader from "@/components/MobileHeader.vue";
import PostService from "./../service/postService";
import { useRoute } from "vue-router";
import { onMounted, ref } from "vue";
import PostListItem from '@/components/PostListItem.vue'

export default {
  components: {
    MobileHeader,
    PostListItem
  },

  setup() {
    const route = useRoute();
    const posts = ref({
      type: Array,
    });
    const post=ref({})

    

    const get_all_posts = async () => {
      try {
        const response = await PostService.get_posts_list();
        posts.value = response.data;
      } catch (error) {
        console.log(error);
      }
    };

  
    onMounted(async() => {
        await get_all_posts();
        console.log("________________");
        console.log(route.params.id)
        post.value = posts.value.find(({ id }) => id === route.params.id);
    });

    return {post,posts}
  },



};
</script>
