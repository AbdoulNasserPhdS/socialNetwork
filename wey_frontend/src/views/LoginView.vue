<template>
  <div class="max-w-7xl mx-auto flex justify-center items-center h-screen p-10">
    <div
      class="flex flex-col md:flex-row w-full md:max-w-5xl bg-white rounded-lg shadow-lg overflow-hidden"
    >
      <!-- Image de fond -->
      <div class="md:w-1/2 relative">
        <img
          src="./../assets/logo.png"
          alt="Background"
          class="object-cover w-full h-full md:block hidden"
        />
        <div
          class="absolute inset-0 bg-gradient-to-r from-purple-500 to-blue-500 opacity-80"
        ></div>
        <div class="absolute inset-0 flex justify-center items-center">
          <h1 class="text-4xl font-bold text-white uppercase text-center">
            Welcome to My Social Network
          </h1>
        </div>
      </div>
      <!-- Formulaire de connexion -->
      <div class="md:w-1/2 p-8">
        <h2 class="text-3xl font-bold mb-8 text-gray-800">
          Log in to your account
        </h2>
        <form @submit.prevent="submitForm" class="space-y-6">
          <div>
            <label for="email" class="block text-gray-700">E-mail</label>
            <input
              type="email"
              v-model.trim="form.email"
              id="email"
              placeholder="Your email address"
              class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
            />
          </div>
          <div>
            <label for="password" class="block text-gray-700">Password</label>
            <input
              type="password"
              v-model.trim="form.password"
              id="password"
              placeholder="Your password"
              class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
            />
          </div>
          <button
            type="submit"
            class="w-full py-3 px-4 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition duration-200"
          >
            Sign in
          </button>
        </form>
        <!-- Affichage des erreurs -->
        <div v-if="errors.length > 0" class="mt-4">
          <div v-for="(error, index) in errors" :key="index" class="text-red-600">
            {{ error }}
          </div>
        </div>
        <!-- Lien vers la page d'inscription -->
        <p class="mt-4 text-gray-700">
          Don't have an account?
          <router-link
            to="/signup"
            class="font-bold text-purple-600 hover:text-purple-700"
            >Subscribe here</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },

  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];

      if (this.form.email === "") {
        this.errors.push("Your e-mail is missing");
      }

      if (this.form.password === "") {
        this.errors.push("Your password is missing");
      }

      if (this.errors.length === 0) {
        await axios
          .post("/api/login/", this.form)
          .then((response) => {
            this.userStore.setToken(response.data);

            axios.defaults.headers.common["Authorization"] =
              "Bearer " + response.data.access;
          })
          .catch((error) => {
            console.log("error", error);

            this.errors.push(
              "The email or password is incorrect! Or the user is not activated!"
            );
          });
      }

      if (this.errors.length === 0) {
        await axios
          .get("/api/me/")
          .then((response) => {
            this.userStore.setUserInfo(response.data);

            this.$router.push("/");
          })
          .catch((error) => {
            console.log("error", error);
          });
      }
    },
  },
};
</script>
