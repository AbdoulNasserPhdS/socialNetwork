<template>
  <!-- component -->
  <!-- This is an example component -->

  <MobileHeader title="Chat" redirect_url="/chat" class="md:hidden"></MobileHeader>

  <div
    class="container mx-auto shadow-lg bg-white rounded-lg h-screen flex justify-center items-center"
  >
    <div class="w-3/4 h-screen">
      <!-- header -->
      <!-- <div class="px-5 py-5 flex justify-between items-center bg-white border-b-2">
        <div class="font-semibold text-2xl">Chat</div>

        <div
          class="h-12 w-12 p-2 bg-yellow-500 rounded-full text-white font-semibold flex items-center justify-center"
        >
          RA
        </div>
      </div> -->
      <!-- end header -->
      <!-- Chatting -->
      <div class="flex flex-col bg-white">
        <!-- chat list -->
        <div class="flex flex-col border-r-2 overflow-y-auto">
          <!-- search chat -->
          <div class="border-b-2 py-4 px-2">
            <input
              type="text"
              placeholder="Rechercher une discussion"
              class="py-2 px-2 border-2 border-gray-200 rounded-2xl w-full"
            />
          </div>
          <!-- end search chat -->
          <!-- discussion list -->
          <div
            v-for="conversion in conversions"
            :key="index"
            class="flex flex-row py-4 px-2 items-center border-b-2 hover:bg-gray-50 cursor-pointer"
          >
            <div class="w-1/6">
              <img
                src="https://t3.ftcdn.net/jpg/05/53/79/60/360_F_553796090_XHrE6R9jwmBJUMo9HKl41hyHJ5gqt9oz.jpg"
                class="object-cover h-12 w-12 rounded-full"
                alt=""
              />
            </div>
            <RouterLink
              v-if="conversion?.created_by?.id !== undefined"
              class="w-full"
              :to="{ name: 'discussion', params: { id: conversion?.created_by?.id } }"
            >
              <div class="text-lg font-semibold">
                {{
                  userId.value == conversion?.created_by?.id
                    ? conversion?.with_user?.name
                    : conversion?.created_by?.name
                }}
              </div>
              <span class="text-gray-500">User</span>
            </RouterLink>
          </div>
          <!-- end discussion list -->
        </div>
        <!-- end chat list -->
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, ref, reactive } from "vue";
import { useUserStore } from "@/stores/user";

import ChatService from "@/service/ChatService";
import MobileHeader from "@/components/MobileHeader.vue";

export default {
  components: {
    MobileHeader,
  },
  setup() {
    const userStore = useUserStore();
    const userId = reactive({
      value: "",
    });
    const conversions = ref({});

    const get_list_conversions = async () => {
      const response = await ChatService.conversion_list();
      conversions.value = response.conversions;
    };

    onMounted(() => {
      get_list_conversions();
      if (userStore.user.id) userId.value = userStore.user.id;
    });

    return { conversions, userStore, userId };
  },
};
</script>
