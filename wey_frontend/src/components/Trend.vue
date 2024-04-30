<template>
  <!--trending tweet section-->
  <div class="max-w-sm rounded-lg bg-dim-700 overflow-hidden shadow-lg m-4">
    <div class="flex">
      <div class="flex-1 m-2">
        <h2 class="px-4 py-2 lg:text-xlw-48 font-semibold text-white ">World Trends</h2>
      </div>
      <div class="flex-1 px-4 py-2 m-2">
        <a
          href=""
          class="text-2xl rounded-full text-white hover:bg-gray-800 hover:text-blue-300 float-right"
        >
          <svg
            class="m-2 h-6 w-6"
            fill="none"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
            ></path>
            <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
          </svg>
        </a>
      </div>
    </div>

    <hr class="border-gray-800" />

    <div class="flex" v-for="trend in trends">
      <div class="flex-1">
        <!-- <p class="px-4 ml-2 mt-3 w-48 text-xs text-gray-400">1 . Trending</p> -->
        <h2 class="px-4 ml-2 w-48 font-bold text-white">#{{ trend?.hashtag }}</h2>
        <p class="px-4 ml-2 mb-3 w-48 text-xs text-gray-400">
          {{ trend?.occurences }} Posts
        </p>
      </div>
      <div class="flex-1 px-4 py-2 m-2">
        <RouterLink
          :to="{name:'search',params:{keyword:trend?.hashtag}}"
          href=""
          class="text-2xl rounded-full text-gray-400 hover:bg-gray-800 hover:text-blue-300 float-right"
        >
          <p
            class=" text-xs	 bg-transparent hover:bg-gray-800 text-white font-semibold hover:text-white py-2 px-4 border border-white hover:border-transparent rounded-full"
          >
            Explore
          </p>
        </RouterLink>
      </div>
    </div>
    <hr class="border-gray-800" />

    <!--show more-->

    <div class="flex">
      <div class="flex-1 p-4">
        <h2 class="px-4 ml-2 w-48 font-bold text-blue-400">Show more</h2>
      </div>
    </div>
  </div>
</template>

<script>
import PostService from "@/service/postService";
import { onMounted, ref } from "vue";

export default {
  setup() {
    const trends = ref([]);

    onMounted(async () => {
      // Utilisation de try-catch pour gérer les erreurs de l'appel de service
      try {
        const response = await PostService.get_trends();

        trends.value = response.data.trends;
        // trends.value = data; // Mettre à jour la référence trends avec les données retournées
      } catch (error) {
        console.error("Erreur lors de la récupération des tendances :", error);
      }
    });

    return { trends };
  },
};
</script>
