<template>
  <div class="flex">
    <div class="flex-1 mx-2">
      <RouterLink :to="redirect_url" class="px-4 py-2 text-xl font-semibold text-white">
        <svg
          v-if="redirect_url == '/'"
          class="h-6 w-6 inline-block mr-2"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 12l9-9 9 9M5 10v10a1 1 0 001 1h3a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h3a1 1 0 001-1V10M9 21h6"
          ></path>
        </svg>
        {{ title }}
      </RouterLink>
    </div>

    <div class="flex-1 px-4 mx-2">
        <router-link
          v-if="userStore.user.id"
          :to="{ name: 'profil', params: { id: userStore.user.id } }"
           
        class="text-2xl font-medium rounded-full text-white hover:bg-gray-800 hover:text-blue-300 float-right"
      >
        <svg class="m-2 h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
          <path
            d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"
          />
        </svg>
      </router-link>

      <a
        href=""
        class="text-2xl font-medium rounded-full text-white hover:bg-gray-800 hover:text-blue-300 float-right"
      >
        <svg class="m-2 h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
          <path
            d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm8.096 10.803L6 6.707v2.768a.5.5 0 0 1-1 0V5.5a.5.5 0 0 1 .5-.5h3.975a.5.5 0 1 1 0 1H6.707l4.096 4.096a.5.5 0 1 1-.707.707"
          />
        </svg>
      </a>

      <router-link
              to="/notification"
        class="text-2xl font-medium rounded-full text-white hover:bg-gray-800 hover:text-blue-300 float-right"
      >
        <svg class="m-2 h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
          <path
            d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2m.995-14.901a1 1 0 1 0-1.99 0A5 5 0 0 0 3 6c0 1.098-.5 6-2 7h14c-1.5-1-2-5.902-2-7 0-2.42-1.72-4.44-4.005-4.901"
          />
        </svg>
      </router-link>
    </div>
  </div>
</template>

<script>

import { useUserStore } from "@/stores/user";

export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    redirect_url: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const userStore = useUserStore();

    return {
      userStore,

    };

  },
};
</script>
