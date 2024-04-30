<style>
input[type="file"] {
    display: none;
}

</style>

<template>



  <form class="bg-white shadow rounded-lg mb-6 p-4" v-on:submit.prevent="add_post">
    <textarea
      name="message"
      placeholder="Type something..."
      v-model="body"
      class="w-full rounded-lg p-2 text-sm bg-gray-100 border border-transparent appearance-none rounded-tg placeholder-gray-400"
    ></textarea>
    <footer class="flex justify-between mt-2">
      <div class="flex gap-2">
  <label
    for="file-upload"
    class="flex items-center transition ease-out duration-300 hover:bg-blue-500 hover:text-white bg-blue-100 w-8 h-8 px-2 rounded-full text-blue-400 cursor-pointer"
  >
    <svg
      viewBox="0 0 24 24"
      width="24"
      height="24"
      stroke="currentColor"
      stroke-width="2"
      fill="none"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
      <circle cx="8.5" cy="8.5" r="1.5"></circle>
      <polyline points="21 15 16 10 5 21"></polyline>
    </svg>
    <!-- Input masqué pour la sélection de fichier -->
    <input
      id="file-upload"
      type="file"
      class="hidden"
      @change="handleImageUpload"
    />
  </label>
</div>

      <button
        class="flex items-center py-2 px-4 rounded-lg text-sm bg-blue-600 text-white shadow-lg"
      >
        Post
        <svg
          class="ml-1"
          viewBox="0 0 24 24"
          width="16"
          height="16"
          stroke="currentColor"
          stroke-width="2"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
      </button>
    </footer>
  </form>


</template>

<script>
import { createToaster } from "@meforma/vue-toaster";
import { ref } from "vue";
import PostService from "./../service/postService";

export default {
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },

  setup(props) {
    const toaster = createToaster();
    const imageURL = ref(null);
    let selectedFile = null;
    const body = ref("");
    const errors = [];


    const add_post = async () => {
      const formData = new FormData();
      if (selectedFile) {
        formData.append("image", selectedFile);
      }
      formData.append("body", body.value);

      if (body.value === "") {
        errors.push("The post value should not be empty !");
      }

      if (errors.length === 0) {
        try {
          const response = await PostService.add_post(formData);
          props.posts.unshift(response.data.post);
          toaster.success(`Post Succeful added !`);
        } catch (error) {
          console.log(error);
          toaster.error(`error during operation, please try again.`);
        }
      } else {
        errors.forEach((element) => {
          toaster.error(element);
        });
      }
    };

    const handleImageUpload = (event) => {
      selectedFile = event.target.files[0];
      if (selectedFile) {
        const reader = new FileReader();
        reader.onload = () => {
          imageURL.value = reader.result;
        };
        reader.readAsDataURL(selectedFile);
      }
    };

    return { add_post, body, errors, handleImageUpload, imageURL};
  },
};
</script>


