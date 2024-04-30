<style>
.overflow-y-auto::-webkit-scrollbar,
.overflow-y-scroll::-webkit-scrollbar,
.overflow-x-auto::-webkit-scrollbar,
.overflow-x::-webkit-scrollbar,
.overflow-x-scroll::-webkit-scrollbar,
.overflow-y::-webkit-scrollbar,
body::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.overflow-y-auto,
.overflow-y-scroll,
.overflow-x-auto,
.overflow-x,
.overflow-x-scroll,
.overflow-y,
body {
  -ms-overflow-style: none;
  /* IE and Edge */
  scrollbar-width: none;
  /* Firefox */
}

.bg-dim-700 {
  --bg-opacity: 1;
  background-color: #192734;
}

html,
body {
  margin: 0;
  background-color: #15202b;
}

svg.paint-icon {
  fill: currentcolor;
}
</style>

<template>
  <div class="flex justify-center w-ful">
    <section class="w-full md:w-3/6 border border-y-0 border-gray-800">
      <!--Content (Center)-->
      <aside>
        <MobileHeader title="Home" redirect_url="/" class="md:hidden"></MobileHeader>

        <div class="flex hidden md:block">
          <div class="flex-1 mx-2">
            <h2 class="px-4 py-2 text-xl font-semibold text-white">
              <svg
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
              Home
            </h2>
          </div>
          <div class="flex-1 px-4 py-2 mx-2">
            <a
              href=""
              class="text-2xl font-medium rounded-full text-white hover:bg-gray-800 hover:text-blue-300 float-right"
            >
              <svg class="m-2 h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                <g>
                  <path
                    d="M22.772 10.506l-5.618-2.192-2.16-6.5c-.102-.307-.39-.514-.712-.514s-.61.207-.712.513l-2.16 6.5-5.62 2.192c-.287.112-.477.39-.477.7s.19.585.478.698l5.62 2.192 2.16 6.5c.102.306.39.513.712.513s.61-.207.712-.513l2.16-6.5 5.62-2.192c.287-.112.477-.39.477-.7s-.19-.585-.478-.697zm-6.49 2.32c-.208.08-.37.25-.44.46l-1.56 4.695-1.56-4.693c-.07-.21-.23-.38-.438-.462l-4.155-1.62 4.154-1.622c.208-.08.37-.25.44-.462l1.56-4.693 1.56 4.694c.07.212.23.382.438.463l4.155 1.62-4.155 1.622zM6.663 3.812h-1.88V2.05c0-.414-.337-.75-.75-.75s-.75.336-.75.75v1.762H1.5c-.414 0-.75.336-.75.75s.336.75.75.75h1.782v1.762c0 .414.336.75.75.75s.75-.336.75-.75V5.312h1.88c.415 0 .75-.336.75-.75s-.335-.75-.75-.75zm2.535 15.622h-1.1v-1.016c0-.414-.335-.75-.75-.75s-.75.336-.75.75v1.016H5.57c-.414 0-.75.336-.75.75s.336.75.75.75H6.6v1.016c0 .414.335.75.75.75s.75-.336.75-.75v-1.016h1.098c.414 0 .75-.336.75-.75s-.336-.75-.75-.75z"
                  ></path>
                </g>
              </svg>
            </a>
          </div>
        </div>

        <div class="w-full my-4" v-if="userStore">
          <h1
            class="text-2xl font-semibold tracking-wider text-gray-800 capitalize dark:text-white"
          >
            Get your free account now.
          </h1>

          <p class="mt-4 text-gray-500 dark:text-gray-400">
            You are not logged in. Please login to join the revelotionnaire social network
            and share posts.
          </p>

          <div class="mt-6">
            <div class="mt-3 md:flex md:items-center md:-mx-2">
              <RouterLink
                to="login"
                class="flex justify-center w-full px-6 py-3 text-white bg-blue-500 rounded-md md:w-auto md:mx-2 focus:outline-none"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                  />
                </svg>

                <span class="mx-2"> connexion </span>
              </RouterLink>

              <RouterLink
                to="signup"
                class="flex justify-center w-full px-6 py-3 mt-4 text-blue-500 border border-blue-500 rounded-md md:mt-0 md:w-auto md:mx-2 dark:border-blue-400 dark:text-blue-400 focus:outline-none"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>

                <span class="mx-2"> Sign up </span>
              </RouterLink>
            </div>
          </div>
        </div>

        <PostAddForm :posts="posts" v-else></PostAddForm>

        <hr class="border-gray-800 border-4" />
      </aside>

      <ul class="list-none">
        <li v-for="post in posts">
          <!--second tweet-->
          <!-- First Column -->
          <PostListItem :post="post" :posts="posts" />
        </li>
      </ul>
    </section>

    <aside class="flex w-2/5 h-12 position-relative hidden md:block">
      <!--Aside menu (right side)-->
      <div style="max-width: 350px">
        <div class="overflow-y-auto fixed h-screen">
          <Trend></Trend>
          <!--people suggetion to follow section-->
          <div class="max-w-sm rounded-lg bg-dim-700 overflow-hidden shadow-lg m-4">
            <div class="flex">
              <div class="flex-1 m-2">
                <h2 class="px-4 py-2 text-xl w-48 font-semibold text-white">
                  Who to follow
                </h2>
              </div>
            </div>

            <hr class="border-gray-800" />

            <!--first person who to follow-->

            <div class="flex flex-shrink-0">
              <div class="flex-1">
                <div class="flex items-center w-48">
                  <div>
                    <img
                      class="inline-block h-10 w-auto rounded-full ml-4 mt-2"
                      src="https://pbs.twimg.com/profile_images/1121328878142853120/e-rpjoJi_bigger.png"
                      alt=""
                    />
                  </div>
                  <div class="ml-3 mt-3">
                    <p class="text-base leading-6 font-medium text-white">
                      Sonali Hirave
                    </p>
                    <p
                      class="text-sm leading-5 font-medium text-gray-400 group-hover:text-gray-300 transition ease-in-out duration-150"
                    >
                      @ShonaDesign
                    </p>
                  </div>
                </div>
              </div>
              <div class="flex-1 px-4 py-2 m-2">
                <a href="" class="float-right">
                  <button
                    class="bg-transparent hover:bg-gray-800 text-white font-semibold hover:text-white py-2 px-4 border border-white hover:border-transparent rounded-full"
                  >
                    Follow
                  </button>
                </a>
              </div>
            </div>
            <hr class="border-gray-800" />

            <!--second person who to follow-->

            <div class="flex flex-shrink-0">
              <div class="flex-1">
                <div class="flex items-center w-48">
                  <div>
                    <img
                      class="inline-block h-10 w-auto rounded-full ml-4 mt-2"
                      src="https://pbs.twimg.com/profile_images/1121328878142853120/e-rpjoJi_bigger.png"
                      alt=""
                    />
                  </div>
                  <div class="ml-3 mt-3">
                    <p class="text-base leading-6 font-medium text-white">
                      Sonali Hirave
                    </p>
                    <p
                      class="text-sm leading-5 font-medium text-gray-400 group-hover:text-gray-300 transition ease-in-out duration-150"
                    >
                      @ShonaDesign
                    </p>
                  </div>
                </div>
              </div>
              <div class="flex-1 px-4 py-2 m-2">
                <a href="" class="float-right">
                  <button
                    class="bg-transparent hover:bg-gray-800 text-white font-semibold hover:text-white py-2 px-4 border border-white hover:border-transparent rounded-full"
                  >
                    Follow
                  </button>
                </a>
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
        </div>
      </div>
    </aside>
  </div>
</template>

<script>
import { createToaster } from "@meforma/vue-toaster";

import PostListItem from "@/components/PostListItem.vue";
import PostAddForm from "@/components/PostAddForm.vue";

import { ref, onMounted } from "vue";

import PostService from "./../service/postService";

import Trend from "@/components/Trend.vue";
import MobileHeader from "@/components/MobileHeader.vue";

export default {
  components: {
    PostListItem,
    PostAddForm,
    Trend,
    MobileHeader,
  },

  setup(unshift) {
    const toaster = createToaster();
    // const toast = useToastStore();
    const posts = ref([]); // Créer un objet réactif qui encapsule les posts
    // const form = ref({
    //     body: ''
    // });
    const errors = [];

    const get_all_posts = async () => {
      try {
        const response = await PostService.get_posts_list();
        posts.value = response.data;
      } catch (error) {
        console.log(error);
      }
    };

    onMounted(get_all_posts);

    return { posts, get_all_posts, errors };
  },
};
</script>
