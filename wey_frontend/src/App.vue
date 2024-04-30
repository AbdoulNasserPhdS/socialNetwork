<template>
  <div class="flex">
    <!-- Sidebar -->
    <aside
      class="flex-shrink-0 w-64 bg-gray-900 p-5 overflow-y-auto hidden md:block h-screen"
      v-if="userStore.user.isAuthenticated"
    >
      <!-- Logo -->
      <div class="flex items-center mx-10 mb-8">
        <img src="./assets/logo.png" alt="Logo" class="h-20 w-auto" />
      </div>
      <!-- Navigation -->
      <nav>
        <ul class="space-y-3">
          <!-- Liens de navigation -->
          <li>
            <router-link
              to="/"
              class="text-gray-300 hover:text-white block py-2 px-4 rounded transition duration-200"
            >
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
            </router-link>
          </li>
          <li>
            <router-link
              to="/friends"
              class="text-gray-300 hover:text-white block py-2 px-4 rounded transition duration-200"
            >
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
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                ></path>
              </svg>
              Friends
            </router-link>
          </li>
          <li>
            <router-link
              to="/chat"
              class="text-gray-300 hover:text-white block py-2 px-4 rounded transition duration-200"
            >
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
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                ></path>
              </svg>
              Chat
            </router-link>
          </li>
          <li>
            <router-link
              :to="{ name: 'search', params: { keyword: ' ' } }"
              class="text-gray-300 hover:text-white block py-2 px-4 rounded transition duration-200"
            >
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
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                ></path>
              </svg>
              Search
            </router-link>
          </li>

          <li>
            <router-link
              to="/notification"
              class="text-gray-300 hover:text-white block py-2 px-4 rounded transition duration-200"
            >
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
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                ></path>
              </svg>
              Notification
            </router-link>
          </li>
        </ul>
      </nav>
      <!-- Profil -->
      <div class="mt-8">
        <router-link
          v-if="userStore.user.id"
          :to="{ name: 'profil', params: { id: userStore.user.id } }"
          class="block text-gray-300 hover:text-white py-2 px-4 rounded transition duration-200"
        >
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
              d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
            ></path>
          </svg>
          Profile
        </router-link>
        <router-link
          v-else
          to="/login"
          class="block text-gray-300 hover:text-white py-2 px-4 rounded transition duration-200"
        >
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
              d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
            ></path>
          </svg>
          Login
        </router-link>
      </div>
    </aside>
    <!-- Contenu principal -->
    <main class="flex-1">
      <router-view></router-view>
    </main>

    <footer
      v-if="userStore.user.isAuthenticated"
      class="fixed bottom-0 w-full bg-gradient-to-t from-gray-800 via-gray-700 to-gray-900 text-white shadow-lg max-h-25 md:invisible"
    >
      <link
        rel="stylesheet"
        href="https://cdn.materialdesignicons.com/6.5.95/css/materialdesignicons.min.css"
      />

      <div class="container mx-auto py-4 px-8">
        <div class="flex justify-between items-center">
          <router-link
            to="/"
            class="hover:text-yellow-500 transition duration-300 flex flex-col items-center"
          >
            <i class="mdi mdi-home mdi-24px"></i>
            <span class="text-xs">Home</span>
          </router-link>

          <router-link
            to="/chat"
            class="hover:text-yellow-500 transition duration-300 flex flex-col items-center"
          >
            <i class="mdi mdi-message-text mdi-24px"></i>
            <span class="text-xs">Chat</span>
          </router-link>
          <router-link
            :to="{ name: 'search', params: { keyword: 'all' } }"
            class="hover:text-yellow-500 transition duration-300 flex flex-col items-center"
          >
            <i class="mdi mdi-magnify mdi-24px"></i>
            <span class="text-xs">Search</span>
          </router-link>
          <router-link
            to="/friends"
            class="hover:text-yellow-500 transition duration-300 flex flex-col items-center"
          >
            <i class="mdi mdi-account-group mdi-24px"></i>
            <span class="text-xs">Friend</span>
          </router-link>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import Toast from "@/components/Toast.vue";
import { useUserStore } from "@/stores/user";
import { RouterLink, useRouter } from "vue-router";
import { reactive, onMounted, watch } from "vue";
export default {
  setup() {
    const userStore = useUserStore();
    const state = reactive({ isHomePage: false });
    const router = useRouter();

    const beforeCreate = () => {
      this.userStore.initStore();

      const token = this.userStore.user.access;

      if (token) {
        axios.defaults.headers.common["Authorization"] = "Bearer " + token;
      } else {
        axios.defaults.headers.common["Authorization"] = "";
      }
    };

    const log_out = () => {
      axios
        .post("api/logout/")
        .then((response) => {
          console.log("deconnecter !");
        })
        .catch((error) => {
          console.log("Erreur de deconnection !");
        });
    };

    // const isHomePage = ()=>{
    //   if(router.value.path=='/login'){
    //     return true
    //   }
    // }

    onMounted(() => {
      const isAuthenticated = userStore.user.isAuthenticated;
      if (!isAuthenticated) {
        router.push("/login");
      }
    });

    watch(
      () => userStore.user.isAuthenticated,
      (isAuthenticated) => {
        if (!isAuthenticated) {
          router.push("/login");
        }
      }
    );

    return {
      userStore,
      beforeCreate,
      log_out,
    };
  },
};
</script>
