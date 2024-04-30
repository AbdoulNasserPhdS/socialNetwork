<style></style>

<template>
  <!-- component -->
  <form v-on:submit.prevent="submitForm">
    <div class="bg-green-100 relative">
      <div
        class="flex flex-col items-center justify-between pt-0  pb-0 mt-0 mr-auto mb-0 ml-auto max-w-7xl xl:px-5 lg:flex-row"
      >
        <div
          class="flex flex-col items-center w-full pr-10 pb-20 pl-10 lg:pt-20 lg:flex-row"
        >
          <div class="w-full bg-cover relative max-w-md lg:max-w-2xl lg:w-7/12">
            <div
              class="flex flex-col items-center justify-center w-full h-full relative lg:pr-10"
            >
              <img
                src="https://res.cloudinary.com/macxenon/image/upload/v1631570592/Run_-_Health_qcghbu.png"
                class="btn-"
              />
            </div>
          </div>

          <div
            class="w-full mt-20 mr-0 mb-0 ml-0 relative z-10 max-w-2xl lg:mt-0 lg:w-5/12"
          >
            <div
              class="flex flex-col items-start justify-start pt-10 pr-10 pb-10 pl-10 bg-white shadow-2xl rounded-xl relative z-10"
            >
              <p class="w-full text-4xl font-medium text-center leading-snug font-serif">
                Sign up for an account
              </p>
              <div class="w-full mt-6 mr-0 mb-0 ml-0 relative space-y-8">
                <div class="relative">
                  <p
                    class="bg-white pt-0 pr-2 pb-0 pl-2 -mt-3 mr-0 mb-0 ml-2 font-medium text-gray-600 absolute"
                  >
                    Username
                  </p>
                  <input
                    placeholder="John"
                    type="text"
                    v-model="form.name"
                    class="border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md"
                  />
                </div>
                <div class="relative">
                  <p
                    class="bg-white pt-0 pr-2 pb-0 pl-2 -mt-3 mr-0 mb-0 ml-2 font-medium text-gray-600 absolute"
                  >
                    Email
                  </p>
                  <input
                    placeholder="123@ex.com"
                    type="text"
                    v-model="form.email"
                    class="border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md"
                  />
                </div>
                <div class="relative">
                  <p
                    class="bg-white pt-0 pr-2 pb-0 pl-2 -mt-3 mr-0 mb-0 ml-2 font-medium text-gray-600 absolute"
                  >
                    Password
                  </p>
                  <input
                    placeholder="Password"
                    type="password"
                    v-model="form.password1"
                    class="border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md"
                  />
                </div>

                <div class="relative">
                  <p
                    class="bg-white pt-0 pr-2 pb-0 pl-2 -mt-3 mr-0 mb-0 ml-2 font-medium text-gray-600 absolute"
                  >
                    Repeat Password
                  </p>
                  <input
                    placeholder="Password"
                    type="password"
                    v-model="form.password2"
                    class="border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md"
                  />
                </div>

                <template v-if="errors.length > 0">
                  <div class="bg-red-300 text-white rounded-lg p-6">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                  </div>
                </template>

                <div class="relative">
                  <button
                    type="submit"
                    class="w-full inline-block pt-4 pr-5 pb-4 pl-5 text-xl font-medium text-center text-white bg-indigo-500 rounded-lg transition duration-200 hover:bg-indigo-600 ease"
                  >
                    Submit
                  </button>
                  <!-- <a class="w-full inline-block pt-4 pr-5 pb-4 pl-5 text-xl font-medium text-center text-white bg-indigo-500
                    rounded-lg transition duration-200 hover:bg-indigo-600 ease">Submit</a> -->
                </div>
              </div>
            </div>
            <svg
              viewbox="0 0 91 91"
              class="absolute top-0 left-0 z-0 w-32 h-32 -mt-12 -ml-12 text-yellow-300 fill-current"
            >
              <g stroke="none" strokewidth="1" fillrule="evenodd">
                <g fillrule="nonzero">
                  <g>
                    <g>
                      <circle cx="3.261" cy="3.445" r="2.72" />
                      <circle cx="15.296" cy="3.445" r="2.719" />
                      <circle cx="27.333" cy="3.445" r="2.72" />
                      <circle cx="39.369" cy="3.445" r="2.72" />
                      <circle cx="51.405" cy="3.445" r="2.72" />
                      <circle cx="63.441" cy="3.445" r="2.72" />
                      <circle cx="75.479" cy="3.445" r="2.72" />
                      <circle cx="87.514" cy="3.445" r="2.719" />
                    </g>
                    <g transform="translate(0 12)">
                      <circle cx="3.261" cy="3.525" r="2.72" />
                      <circle cx="15.296" cy="3.525" r="2.719" />
                      <circle cx="27.333" cy="3.525" r="2.72" />
                      <circle cx="39.369" cy="3.525" r="2.72" />
                      <circle cx="51.405" cy="3.525" r="2.72" />
                      <circle cx="63.441" cy="3.525" r="2.72" />
                      <circle cx="75.479" cy="3.525" r="2.72" />
                      <circle cx="87.514" cy="3.525" r="2.719" />
                    </g>
                    <g transform="translate(0 24)">
                      <circle cx="3.261" cy="3.605" r="2.72" />
                      <circle cx="15.296" cy="3.605" r="2.719" />
                      <circle cx="27.333" cy="3.605" r="2.72" />
                      <circle cx="39.369" cy="3.605" r="2.72" />
                      <circle cx="51.405" cy="3.605" r="2.72" />
                      <circle cx="63.441" cy="3.605" r="2.72" />
                      <circle cx="75.479" cy="3.605" r="2.72" />
                      <circle cx="87.514" cy="3.605" r="2.719" />
                    </g>
                    <g transform="translate(0 36)">
                      <circle cx="3.261" cy="3.686" r="2.72" />
                      <circle cx="15.296" cy="3.686" r="2.719" />
                      <circle cx="27.333" cy="3.686" r="2.72" />
                      <circle cx="39.369" cy="3.686" r="2.72" />
                      <circle cx="51.405" cy="3.686" r="2.72" />
                      <circle cx="63.441" cy="3.686" r="2.72" />
                      <circle cx="75.479" cy="3.686" r="2.72" />
                      <circle cx="87.514" cy="3.686" r="2.719" />
                    </g>
                    <g transform="translate(0 49)">
                      <circle cx="3.261" cy="2.767" r="2.72" />
                      <circle cx="15.296" cy="2.767" r="2.719" />
                      <circle cx="27.333" cy="2.767" r="2.72" />
                      <circle cx="39.369" cy="2.767" r="2.72" />
                      <circle cx="51.405" cy="2.767" r="2.72" />
                      <circle cx="63.441" cy="2.767" r="2.72" />
                      <circle cx="75.479" cy="2.767" r="2.72" />
                      <circle cx="87.514" cy="2.767" r="2.719" />
                    </g>
                    <g transform="translate(0 61)">
                      <circle cx="3.261" cy="2.846" r="2.72" />
                      <circle cx="15.296" cy="2.846" r="2.719" />
                      <circle cx="27.333" cy="2.846" r="2.72" />
                      <circle cx="39.369" cy="2.846" r="2.72" />
                      <circle cx="51.405" cy="2.846" r="2.72" />
                      <circle cx="63.441" cy="2.846" r="2.72" />
                      <circle cx="75.479" cy="2.846" r="2.72" />
                      <circle cx="87.514" cy="2.846" r="2.719" />
                    </g>
                    <g transform="translate(0 73)">
                      <circle cx="3.261" cy="2.926" r="2.72" />
                      <circle cx="15.296" cy="2.926" r="2.719" />
                      <circle cx="27.333" cy="2.926" r="2.72" />
                      <circle cx="39.369" cy="2.926" r="2.72" />
                      <circle cx="51.405" cy="2.926" r="2.72" />
                      <circle cx="63.441" cy="2.926" r="2.72" />
                      <circle cx="75.479" cy="2.926" r="2.72" />
                      <circle cx="87.514" cy="2.926" r="2.719" />
                    </g>
                    <g transform="translate(0 85)">
                      <circle cx="3.261" cy="3.006" r="2.72" />
                      <circle cx="15.296" cy="3.006" r="2.719" />
                      <circle cx="27.333" cy="3.006" r="2.72" />
                      <circle cx="39.369" cy="3.006" r="2.72" />
                      <circle cx="51.405" cy="3.006" r="2.72" />
                      <circle cx="63.441" cy="3.006" r="2.72" />
                      <circle cx="75.479" cy="3.006" r="2.72" />
                      <circle cx="87.514" cy="3.006" r="2.719" />
                    </g>
                  </g>
                </g>
              </g>
            </svg>
            <svg
              viewbox="0 0 91 91"
              class="absolute bottom-0 right-0 z-0 w-32 h-32 -mb-12 -mr-12 text-indigo-500 fill-current"
            >
              <g stroke="none" strokewidth="1" fillrule="evenodd">
                <g fillrule="nonzero">
                  <g>
                    <g>
                      <circle cx="3.261" cy="3.445" r="2.72" />
                      <circle cx="15.296" cy="3.445" r="2.719" />
                      <circle cx="27.333" cy="3.445" r="2.72" />
                      <circle cx="39.369" cy="3.445" r="2.72" />
                      <circle cx="51.405" cy="3.445" r="2.72" />
                      <circle cx="63.441" cy="3.445" r="2.72" />
                      <circle cx="75.479" cy="3.445" r="2.72" />
                      <circle cx="87.514" cy="3.445" r="2.719" />
                    </g>
                    <g transform="translate(0 12)">
                      <circle cx="3.261" cy="3.525" r="2.72" />
                      <circle cx="15.296" cy="3.525" r="2.719" />
                      <circle cx="27.333" cy="3.525" r="2.72" />
                      <circle cx="39.369" cy="3.525" r="2.72" />
                      <circle cx="51.405" cy="3.525" r="2.72" />
                      <circle cx="63.441" cy="3.525" r="2.72" />
                      <circle cx="75.479" cy="3.525" r="2.72" />
                      <circle cx="87.514" cy="3.525" r="2.719" />
                    </g>
                    <g transform="translate(0 24)">
                      <circle cx="3.261" cy="3.605" r="2.72" />
                      <circle cx="15.296" cy="3.605" r="2.719" />
                      <circle cx="27.333" cy="3.605" r="2.72" />
                      <circle cx="39.369" cy="3.605" r="2.72" />
                      <circle cx="51.405" cy="3.605" r="2.72" />
                      <circle cx="63.441" cy="3.605" r="2.72" />
                      <circle cx="75.479" cy="3.605" r="2.72" />
                      <circle cx="87.514" cy="3.605" r="2.719" />
                    </g>
                    <g transform="translate(0 36)">
                      <circle cx="3.261" cy="3.686" r="2.72" />
                      <circle cx="15.296" cy="3.686" r="2.719" />
                      <circle cx="27.333" cy="3.686" r="2.72" />
                      <circle cx="39.369" cy="3.686" r="2.72" />
                      <circle cx="51.405" cy="3.686" r="2.72" />
                      <circle cx="63.441" cy="3.686" r="2.72" />
                      <circle cx="75.479" cy="3.686" r="2.72" />
                      <circle cx="87.514" cy="3.686" r="2.719" />
                    </g>
                    <g transform="translate(0 49)">
                      <circle cx="3.261" cy="2.767" r="2.72" />
                      <circle cx="15.296" cy="2.767" r="2.719" />
                      <circle cx="27.333" cy="2.767" r="2.72" />
                      <circle cx="39.369" cy="2.767" r="2.72" />
                      <circle cx="51.405" cy="2.767" r="2.72" />
                      <circle cx="63.441" cy="2.767" r="2.72" />
                      <circle cx="75.479" cy="2.767" r="2.72" />
                      <circle cx="87.514" cy="2.767" r="2.719" />
                    </g>
                    <g transform="translate(0 61)">
                      <circle cx="3.261" cy="2.846" r="2.72" />
                      <circle cx="15.296" cy="2.846" r="2.719" />
                      <circle cx="27.333" cy="2.846" r="2.72" />
                      <circle cx="39.369" cy="2.846" r="2.72" />
                      <circle cx="51.405" cy="2.846" r="2.72" />
                      <circle cx="63.441" cy="2.846" r="2.72" />
                      <circle cx="75.479" cy="2.846" r="2.72" />
                      <circle cx="87.514" cy="2.846" r="2.719" />
                    </g>
                    <g transform="translate(0 73)">
                      <circle cx="3.261" cy="2.926" r="2.72" />
                      <circle cx="15.296" cy="2.926" r="2.719" />
                      <circle cx="27.333" cy="2.926" r="2.72" />
                      <circle cx="39.369" cy="2.926" r="2.72" />
                      <circle cx="51.405" cy="2.926" r="2.72" />
                      <circle cx="63.441" cy="2.926" r="2.72" />
                      <circle cx="75.479" cy="2.926" r="2.72" />
                      <circle cx="87.514" cy="2.926" r="2.719" />
                    </g>
                    <g transform="translate(0 85)">
                      <circle cx="3.261" cy="3.006" r="2.72" />
                      <circle cx="15.296" cy="3.006" r="2.719" />
                      <circle cx="27.333" cy="3.006" r="2.72" />
                      <circle cx="39.369" cy="3.006" r="2.72" />
                      <circle cx="51.405" cy="3.006" r="2.72" />
                      <circle cx="63.441" cy="3.006" r="2.72" />
                      <circle cx="75.479" cy="3.006" r="2.72" />
                      <circle cx="87.514" cy="3.006" r="2.719" />
                    </g>
                  </g>
                </g>
              </g>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "axios";
import { createToaster } from "@meforma/vue-toaster";
import { useToastStore } from "@/stores/toast";

export default {
  setup() {
    const toastStore = useToastStore();
    const toaster = createToaster();


    return {
      toastStore,toaster
    };
  },

  data() {
    return {
      form: {
        email: "",
        name: "",
        password1: "",
        password2: "",
      },
      errors: [],
    };
  },

  methods: {
    submitForm() {
      this.errors = [];

        // this.$toast.error(`Hey! I'm here`);
        // this.$toast.warning(`Hey! I'm here`);
        // this.$toast.info(`Hey! I'm here`);



      if (this.form.email === "") {
        this.errors.push("Your e-mail is missing");
      }

      if (this.form.name === "") {
        this.errors.push("Your name is missing");
      }

      if (this.form.password1 === "") {
        this.errors.push("Your password is missing");
      }

      if (this.form.password1 !== this.form.password2) {
        this.errors.push("The password does not match");
      }

      if (this.errors.length === 0) {
        axios
          .post("/api/signup/", this.form)
          .then((response) => {
            if (response.data.message === "success") {
                
            this.toaster.show("Registration successful, Please login to your account!", {
                type: "success",
                dismissible:true,
                position: "top",
                duration:2000,
                // all of other options may go here
                });

              this.form.email = "";
              this.form.name = "";
              this.form.password1 = "";
              this.form.password2 = "";

              setTimeout(() => {
                this.$router.push("/login");
                }, 2100);



            } else {
              const data = JSON.parse(response.data.message);
              for (const key in data) {
                this.errors.push(data[key][0].message);
              }

              this.toastStore.showToast(
                5000,
                "Something went wrong. Please try again",
                "bg-red-300"
              );
            }
          })
          .catch((error) => {
            console.log("error", error);
          });
      }
    },
  },
};
</script>
