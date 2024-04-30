<style scoped>
.fill-red {
  fill: red;
}
</style>

<template>
  <div class="bg-white w-full h-full my-2 flex items-center justify-center">
    <div class="bg-white p-4 rounded-lg shadow-md max-w-md w-full">

      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center space-x-2">
          <img
            src="https://cdn.icon-icons.com/icons2/2030/PNG/512/user_icon_124042.png"
            alt="User Avatar"
            class="w-9 h-9 rounded-full"
          />
          <div>
            <p class="text-gray-800 font-semibold">{{ post.created_by?.name }}</p>
            <p class="text-gray-500 text-sm">{{ post.created_at_formatted }} ago</p>
          </div>
        </div>
        <div class="text-gray-500 cursor-pointer">
          <!-- Three-dot menu icon -->
          <button class="hover:bg-gray-50 rounded-full p-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="12" cy="7" r="1" />
              <circle cx="12" cy="12" r="1" />
              <circle cx="12" cy="17" r="1" />
            </svg>
          </button>
        </div>
      </div>
      <!-- Message -->
      <div class="mb-4">
        <p class="text-gray-800">
          {{ post.body }} <a href="" class="text-blue-600">#everyone</a>
        </p>
      </div>
      <!-- Image -->
      <div class="mb-4" v-if="post?.attachments" v-for="attachment in post?.attachments">
        <img
          :src="attachment.get_image"
          alt="Post Image"
          class="w-full h-48 object-cover rounded-md"
        />
      </div>
      <!-- Like and Comment Section -->
      <div class="flex items-center justify-between text-gray-500">
        <div class="flex items-center space-x-2">
          <button
            class="flex justify-center items-center gap-2 px-2 hover:bg-gray-50 rounded-full p-1">
            <svg  v-show="!is_like_post()"
            @click="like_post(post.id)"
              class="w-5 h-5 fill-current"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
            >
              <path
                d="M12 21.35l-1.45-1.32C6.11 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-4.11 6.86-8.55 11.54L12 21.35z"
              />
            </svg>
            <svg
              class="text-red-500 w-6 h-6"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              v-show="is_like_post()"
              @click="like_post(post.id)"
            >
              <path
                fill-rule="evenodd"
                d="M10 18l-1.22-1.12C4.42 12.36 2 10.11 2 7.5 2 5.42 3.42 4 5.5 4c1.54 0 3.04.99 4 2.38C10.46 4.99 11.96 4 13.5 4 15.58 4 17 5.42 17 7.5c0 2.61-2.42 4.86-6.78 9.38L10 18z"
                clip-rule="evenodd"
              />
            </svg>

            <span>{{ post?.likes_count }} Likes</span>
          </button>
        </div>
        <button
          class="flex justify-center items-center gap-2 px-2 hover:bg-gray-50 rounded-full p-1"
          @click="toggleComments">
          <svg
            width="22px"
            height="22px"
            viewBox="0 0 24 24"
            class="w-5 h-5 fill-current"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 13.5997 2.37562 15.1116 3.04346 16.4525C3.22094 16.8088 3.28001 17.2161 3.17712 17.6006L2.58151 19.8267C2.32295 20.793 3.20701 21.677 4.17335 21.4185L6.39939 20.8229C6.78393 20.72 7.19121 20.7791 7.54753 20.9565C8.88837 21.6244 10.4003 22 12 22ZM8 13.25C7.58579 13.25 7.25 13.5858 7.25 14C7.25 14.4142 7.58579 14.75 8 14.75H13.5C13.9142 14.75 14.25 14.4142 14.25 14C14.25 13.5858 13.9142 13.25 13.5 13.25H8ZM7.25 10.5C7.25 10.0858 7.58579 9.75 8 9.75H16C16.4142 9.75 16.75 10.0858 16.75 10.5C16.75 10.9142 16.4142 11.25 16 11.25H8C7.58579 11.25 7.25 10.9142 7.25 10.5Z"
              ></path>
            </g>
          </svg>
          <span>{{ post?.comments_count }} Comment</span>
        </button>
      </div>
      <hr class="mt-2 mb-2" />
      <p class="text-gray-800 font-semibold">Comment</p>
      <hr class="mt-2 mb-2" />
      <div class="mt-4" v-if="showComments">
        <!-- Comment 1 -->
        <div class="flex items-center space-x-2" v-for="comment in post.comments">
          <img
            src="https://placekitten.com/32/32"
            alt="User Avatar"
            class="w-6 h-6 rounded-full"
          />
          <div>
            <p class="text-gray-800 font-semibold">{{ comment?.created_by?.name }}</p>
            <p class="text-gray-500 text-sm">{{ comment.comment }}</p>
          </div>
        </div>
     
      </div>

      <form v-on:submit.prevent="submitComment">
        <div
          class="relative flex items-center self-center w-full max-w-xl p-4 overflow-hidden text-gray-600 focus-within:text-gray-400"
        >
          <img
            class="w-10 h-10 object-cover rounded-full shadow mr-2 cursor-pointer"
            alt="User avatar"
            src="https://static.vecteezy.com/system/resources/previews/009/292/244/original/default-avatar-icon-of-social-media-user-vector.jpg"
          />
          <span class="absolute inset-y-0 right-0 flex items-center pr-6">
            <button
              type="submit"
              class="p-1 focus:outline-none focus:shadow-none hover:text-blue-500"
            >
              <svg
                class="w-6 h-6 transition ease-out duration-300 hover:text-blue-500 text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
            </button>
          </span>
          <input
            type="search"
            v-model="form.comment"
            class="w-full py-2 pl-4 pr-10 text-sm bg-gray-100 border border-transparent appearance-none rounded-tg placeholder-gray-400"
            style="border-radius: 25px"
            placeholder="Post a comment..."
            autocomplete="off"
          />
        </div>
      </form>
    </div>
  </div>
</template>



<script>
import { createToaster } from "@meforma/vue-toaster";

import { useUserStore } from "@/stores/user";
import { ref } from "vue";

import PostService from "./../service/postService";

export default {
  props: {
    post: Object,
    posts: {
      type: Array,
      required: true,
    },
  },



  setup(props) {
    const toaster = createToaster();

    const user = useUserStore();

    const showComments = ref(false);

    const form = {
      comment: "",
    };

    const like_post = async (post_key) => {
      const return_post = await PostService.like_post(post_key);

      console.log(return_post.post);

      const index = props.posts.findIndex((obj) => obj.id === return_post.post.id);

      console.log(index);

      if (index !== -1) {
        props.posts.splice(index, 1, return_post.post);
      }

      console.log(props.posts);
    };

    const is_like_post = () => {
      if (
        props.post.like &&
        props.post.like.findIndex((item) => item.created_by == user.user.id) >= 0
      ) {
        return true;
        // console.log(props.post)
      } else {
        return false;
      }
    };


    const toggleComments = () => {
      showComments.value = !showComments.value;
    };


    const submitComment = async () => {
      const return_post = await PostService.commentPost(form, props.post.id);

      if (return_post) {
        const index = props.posts.findIndex((obj) => obj.id === return_post.id);

        if (index !== -1) {
          props.posts.splice(index, 1, return_post);
        }
      }
    };

    return { like_post, is_like_post, submitComment, form,  showComments, toggleComments };
  },
};
</script>
