<template>
  <!-- component -->
  <MobileHeader
    title="Discussion"
    redirect_url="/discussion"
    class="md:hidden"
  ></MobileHeader>

  <div class="flex h-screen antialiased text-gray-800 pb-20 md:pb-0">
    <div class="flex flex-row h-full w-full overflow-x-hidden">
      <div
        class="flex flex-col py-8 pl-6 pr-2 w-64 bg-white flex-shrink-0 hidden md:block"
      >
        <div class="flex flex-row items-center justify-center h-12 w-full">
          <div
            class="flex items-center justify-center rounded-2xl text-indigo-700 bg-indigo-100 h-10 w-10"
          >
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
              ></path>
            </svg>
          </div>
          <div class="ml-2 font-bold text-2xl">QuickChat</div>
        </div>
        <div
          class="flex flex-col items-center bg-indigo-100 border border-gray-200 mt-4 w-full py-6 px-4 rounded-lg"
        >
          <div class="h-20 w-20 rounded-full border overflow-hidden">
            <img
              src="https://avatars3.githubusercontent.com/u/2763884?s=128"
              alt="Avatar"
              class="h-full w-full"
            />
          </div>
          <div class="text-sm font-semibold mt-2">Aminos Co.</div>
          <div class="text-xs text-gray-500">Lead UI/UX Designer</div>
          <div class="flex flex-row items-center mt-3">
            <div class="flex flex-col justify-center h-4 w-8 bg-indigo-500 rounded-full">
              <div class="h-3 w-3 bg-white rounded-full self-end mr-1"></div>
            </div>
            <div class="leading-none ml-1 text-xs">Active</div>
          </div>
        </div>
        <div class="flex flex-col mt-8">
          <div class="flex flex-row items-center justify-between text-xs">
            <span class="font-bold">Active Conversations</span>
            <span
              class="flex items-center justify-center bg-gray-300 h-4 w-4 rounded-full"
              >4</span
            >
          </div>
          <div class="flex flex-col space-y-1 mt-4 -mx-2 h-48 overflow-y-auto">
            <button class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
              <div
                class="flex items-center justify-center h-8 w-8 bg-indigo-200 rounded-full"
              >
                H
              </div>
              <div class="ml-2 text-sm font-semibold">Henry Boyd</div>
            </button>
            <button class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
              <div
                class="flex items-center justify-center h-8 w-8 bg-gray-200 rounded-full"
              >
                M
              </div>
              <div class="ml-2 text-sm font-semibold">Marta Curtis</div>
              <div
                class="flex items-center justify-center ml-auto text-xs text-white bg-red-500 h-4 w-4 rounded leading-none"
              >
                2
              </div>
            </button>
            <button class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
              <div
                class="flex items-center justify-center h-8 w-8 bg-orange-200 rounded-full"
              >
                P
              </div>
              <div class="ml-2 text-sm font-semibold">Philip Tucker</div>
            </button>
            <button class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
              <div
                class="flex items-center justify-center h-8 w-8 bg-pink-200 rounded-full"
              >
                C
              </div>
              <div class="ml-2 text-sm font-semibold">Christine Reid</div>
            </button>
            <button class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
              <div
                class="flex items-center justify-center h-8 w-8 bg-purple-200 rounded-full"
              >
                J
              </div>
              <div class="ml-2 text-sm font-semibold">Jerry Guzman</div>
            </button>
          </div>
          <div class="flex flex-row items-center justify-between text-xs mt-6">
            <span class="font-bold">Archivied</span>
            <span
              class="flex items-center justify-center bg-gray-300 h-4 w-4 rounded-full"
              >7</span
            >
          </div>
          <div class="flex flex-col space-y-1 mt-4 -mx-2">
            <button class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
              <div
                class="flex items-center justify-center h-8 w-8 bg-indigo-200 rounded-full"
              >
                H
              </div>
              <div class="ml-2 text-sm font-semibold">Henry Boyd</div>
            </button>
          </div>
        </div>
      </div>
      <div class="flex flex-col flex-auto h-full">
        <div class="flex flex-col flex-auto flex-shrink-0 bg-gray-100 h-screen">
          <div class="flex flex-col h-full overflow-x-auto mb-4">
            <div class="flex flex-col h-full">
              <div class="grid grid-cols-12 gap-y-2" v-for="message in messages">
                <DiscussionMessageLeft
                  v-if="message.sent_to.id != userStore.user.id"
                  :message="message.content"
                  :initial="getInitial(message.content)"
                ></DiscussionMessageLeft>
                <DicussionMessageRight
                  v-else
                  :message="message.content"
                  :initial="getInitial(message.content)"
                ></DicussionMessageRight>
              </div>
            </div>
          </div>
          <form
            v-on:submit.prevent="sendMessage"
            class="flex flex-row items-center h-16 rounded-xl bg-white w-full px-4"
          >
            <!-- <div>
              <button
                class="flex items-center justify-center text-gray-400 hover:text-gray-600"
              >
                <svg
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"
                  ></path>
                </svg>
              </button>
            </div> -->

            <div class="flex-grow ml-4">
              <div class="relative w-full">
                <input
                  v-model="form.content"
                  type="text"
                  class="flex w-full border rounded-xl focus:outline-none focus:border-indigo-300 pl-4 h-10"
                />
                <button
                  class="absolute flex items-center justify-center h-full w-12 right-0 top-0 text-gray-400 hover:text-gray-600"
                >
                  <svg
                    class="w-6 h-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    ></path>
                  </svg>
                </button>
              </div>
            </div>
            <div class="ml-4">
              <button
                type="submit"
                class="flex items-center justify-center bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white px-4 py-1 flex-shrink-0"
              >
                <span>Send</span>
                <span class="ml-2">
                  <svg
                    class="w-4 h-4 transform rotate-45 -mt-px"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                    ></path>
                  </svg>
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ChatService from "@/service/ChatService";
import { useRoute } from "vue-router";

import { onUnmounted, onMounted, ref } from "vue";
import { createToaster } from "@meforma/vue-toaster";

import DicussionMessageRight from "@/components/DicussionMessageRight.vue";
import DiscussionMessageLeft from "@/components/DiscussionMessageLeft.vue";
import MobileHeader from "@/components/MobileHeader.vue";

import { useUserStore } from "@/stores/user";

export default {
  components: {
    DiscussionMessageLeft,
    DicussionMessageRight,
    MobileHeader,
  },
  setup() {
    const conversion = ref({});
    const messages = ref({});
    const route = useRoute();
    const toaster = createToaster();
    const userStore = useUserStore();

    const autoReloadInterval = ref({
      type: Number,
    });

    const form = ref({
      content: "",
    });

    const get_or_create_Conversion = async () => {
      const response = await ChatService.conversion_detail(route.params.id);
      conversion.value = response.conversion;
      messages.value = response.messages;
    };

    const sendMessage = async () => {
      if (conversion.value) {
        const response = await ChatService.send_message(conversion.value.id, form.value);
        messages.value.unshift(response.conversionMessage);
      } else {
        toaster.error("Please try again later");
      }
    };

    const getInitial = (content) => {
      return content.charAt(0);
    };

    onMounted(() => {
      get_or_create_Conversion();
      autoReloadInterval.value = setInterval(get_or_create_Conversion, 1000);
    });

    onUnmounted(() => {
      clearInterval(autoReloadInterval.value);
    });

    return {
      get_or_create_Conversion,
      conversion,
      messages,
      form,
      sendMessage,
      getInitial,
      userStore,
      autoReloadInterval: null,
    };
  },
};
</script>
