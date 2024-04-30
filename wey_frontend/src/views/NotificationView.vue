<template>
  <div class="min-h-screen bg-gradient-to-r from-sky-200 to-red-100 py-20">
    <div class="max-w-2xl mx-auto flex flex-col gap-10 px-5">
      <div v-for="notification in notifications" :key="notification?.id">
        <div
          class="flex flex-col md:flex-row bg-white rounded-xl shadow-lg hover:shadow-xl transition duration-300"
        >
          <div class="flex justify-center md:justify-end">
            <div
              class="w-20 h-20 bg-white shadow-lg rounded-full p-4 flex justify-center items-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                class="w-12 h-12 text-blue-900"
              >
                <path
                  fill-rule="evenodd"
                  d="M18.685 19.097A9.723 9.723 0 0021.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 003.065 7.097A9.716 9.716 0 0012 21.75a9.716 9.716 0 006.685-2.653zm-12.54-1.285A7.486 7.486 0 0112 15a7.486 7.486 0 015.855 2.812A8.224 8.224 0 0112 20.25a8.224 8.224 0 01-5.855-2.438zM15.75 9a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </div>
          </div>
          <div class="p-4">
            <h1 class="font-bold text-xl pb-4">{{ notification?.title }}</h1>
            <p class="text-gray-700">{{ notification?.body }}</p>

            <RouterLink
              :to="{name:'details', params:{'id':notification?.post?.id}}"
              class="text-blue-500 underline"
              >See
            </RouterLink>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NotificationService from "./../service/NotificationSerivce";
import { ref, onMounted } from "vue";

export default {
  setup() {
    const notifications = ref({
      type: Array,
    });

    onMounted(async () => {
      const response = await NotificationService.get_list_notifications();
      notifications.value = response.data.notifications;
      //   console.log(notifications.value)
    });

    return { notifications };
  },
};
</script>
