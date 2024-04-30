<template>
  <!-- component -->

  <MobileHeader title="Search" redirect_url="/profil" class="md:hidden"></MobileHeader>

  <div class="bg-gray-100 h-screen">
    <aside class="">
      <div class="bg-white shadow rounded-lg p-10">
        <div class="flex flex-col gap-1 text-center items-center">
          <img
            class="h-32 w-32 bg-white p-2 rounded-full shadow mb-4"
            src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&amp;w=2000&amp;q=80"
            alt=""
          />
          <p class="font-semibold">{{ user?.name }}</p>
          <div
            class="text-sm leading-normal text-gray-400 flex justify-center items-center"
          >
            <svg
              viewBox="0 0 24 24"
              class="mr-1"
              width="16"
              height="16"
              stroke="currentColor"
              stroke-width="2"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Los Angeles, California
          </div>
        </div>
        <div class="flex justify-center items-center gap-2 my-3">
          <div class="font-semibold text-center mx-4">
            <p class="text-black">102</p>
            <span class="text-gray-400">Posts</span>
          </div>
          <div class="font-semibold text-center mx-4">
            <p class="text-black">102</p>
            <span class="text-gray-400">Followers</span>
          </div>
          <div class="font-semibold text-center mx-4">
            <p class="text-black">102</p>
            <span class="text-gray-400">Folowing</span>
          </div>
        </div>

        <div class="flex justify-center items-center">
          <a
            v-if="userStore?.user?.id !== user?.id"
            @click="sendFrienRequest(user?.id)"
            class="bg-blue-500 rounded-md font-bold text-white text-center px-4 py-3 transition duration-300 ease-in-out hover:bg-blue-600 mr-2"
          >
            Add As Friend
          </a>
          <a
            v-if="userStore?.user?.id == user?.id"
            href=""
            class="bg-red-500 rounded-md font-bold text-white text-center px-4 py-3 transition duration-300 ease-in-out hover:bg-red-600 ml-2"
          >
            Edit profile
          </a>
        </div>
      </div>

      <div class="bg-white shadow mt-6 rounded-lg p-6">
        <h3 class="text-gray-600 text-sm font-semibold mb-4">Following</h3>
        <ul class="flex items-center justify-center space-x-2">
          <!-- Story #1 -->
          <li
            v-for="request in friendshipRequest"
            class="flex flex-col items-center space-y-2"
          >
            <!-- Ring -->
            <a class="block bg-white p-1 rounded-full" href="#">
              <img
                class="w-16 rounded-full"
                src="https://images.unsplash.com/photo-1638612913771-8f00622b96fb?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=200&amp;h=200&amp;q=80"
              />
            </a>
            <!-- Username -->
            <span class="text-xs text-gray-500"> {{ request.created_by.name }} </span>
          </li>

          <!-- Story #1 -->
          <li class="flex flex-col items-center space-y-2">
            <!-- Ring -->
            <a class="block bg-white p-1 rounded-full" href="#">
              <img
                class="w-16 rounded-full"
                src="https://images.unsplash.com/photo-1638649602320-450b717fa622?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=200&amp;h=200&amp;q=80"
              />
            </a>

            <!-- Username -->
            <span class="text-xs text-gray-500"> Jett </span>
          </li>

          <!-- Story #2 -->
          <li class="flex flex-col items-center space-y-2">
            <!-- Ring -->
            <a class="block bg-white p-1 rounded-full" href="#">
              <!-- Thumbnail -->
              <img
                class="w-16 rounded-full"
                src="https://images.unsplash.com/photo-1638708644743-2502f38000a0?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=200&amp;h=200&amp;q=80"
              />
            </a>

            <!-- Username -->
            <span class="text-xs text-gray-500"> Sky </span>
          </li>

          <!-- Story #3 -->
          <li class="flex flex-col items-center space-y-2">
            <!-- Ring -->
            <a class="block bg-white p-1 rounded-full" href="#">
              <!-- Thumbnail -->
              <img
                class="w-16 rounded-full"
                src="https://images.unsplash.com/photo-1638691899851-0e955bceba1f?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=200&amp;h=200&amp;q=80"
              />
            </a>

            <!-- Username -->
            <span class="text-xs text-gray-500"> Olivia </span>
          </li>

          <!-- Story #4 -->
          <li class="flex flex-col items-center space-y-2">
            <!-- Ring -->
            <a class="block bg-white p-1 rounded-full" href="#">
              <img
                class="w-16 rounded-full"
                src="https://images.unsplash.com/photo-1638612913771-8f00622b96fb?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=200&amp;h=200&amp;q=80"
              />
            </a>

            <!-- Username -->
            <span class="text-xs text-gray-500"> Julia </span>
          </li>
          <!-- Story #1 -->
          <li class="flex flex-col items-center space-y-2">
            <!-- Ring -->
            <a class="block bg-white p-1 rounded-full" href="#">
              <!-- Thumbnail -->
              <img
                class="w-16 rounded-full"
                src="https://images.unsplash.com/photo-1638649602320-450b717fa622?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=200&amp;h=200&amp;q=80"
              />
            </a>

            <!-- Username -->
            <span class="text-xs text-gray-500"> Hendrick </span>
          </li>
        </ul>
      </div>

      <div class="flex bg-white shadow mt-6 rounded-lg p-2">
        <img
          src="https://images.unsplash.com/photo-1439130490301-25e322d88054?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&amp;w=1189&amp;q=80"
          alt="Just a flower"
          class="w-16 object-cover h-16 rounded-xl"
        />
        <div class="flex flex-col justify-center w-full px-2 py-1">
          <div class="flex justify-between items-center">
            <div class="flex flex-col">
              <h2 class="text-sm font-medium">Massive Dynamic</h2>
            </div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-gray-500 hover:text-blue-400 cursor-pointer"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"
              ></path>
            </svg>
          </div>
          <div class="flex pt-2 text-sm text-gray-400">
            <div class="flex items-center mr-auto">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-yellow-500 mr-1"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                ></path>
              </svg>
              <p class="font-normal">4.5</p>
            </div>
            <div class="flex items-center font-medium text-gray-900">
              $1800
              <span class="text-gray-400 text-sm font-normal"> /wk</span>
            </div>
          </div>
        </div>
      </div>

      <div
        class="grid mt-5 grid-cols-2 space-x-4 overflow-y-scroll flex justify-center items-center w-full"
      >
        <div
          class="relative flex flex-col justify-between bg-white shadow-md rounded-3xl bg-cover text-gray-800 overflow-hidden cursor-pointer w-full object-cover object-center rounded shadow-md h-64 my-2"
          style="
            background-image: url('https://images.unsplash.com/reserve/8T8J12VQxyqCiQFGa2ct_bahamas-atlantis.jpg?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=1050&amp;q=80');
          "
        >
          <div
            class="absolute bg-gradient-to-t from-green-400 to-blue-400 opacity-50 inset-0 z-0"
          ></div>
          <div class="relative flex flex-row items-end h-72 w-full">
            <div class="absolute right-0 top-0 m-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-9 w-9 p-2 text-gray-200 hover:text-blue-400 rounded-full hover:bg-white transition ease-in duration-200"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"
                ></path>
              </svg>
            </div>
            <div class="p-6 rounded-lg flex flex-col w-full">
              <h4 class="mt-1 text-white text-xl font-semibold leading-tight truncate">
                Loremipsum..
              </h4>
              <div class="flex justify-between items-center">
                <div class="flex flex-col">
                  <h2 class="text-sm flex items-center text-gray-300 font-normal">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4 mr-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                      ></path>
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                      ></path>
                    </svg>
                    Dubai
                  </h2>
                </div>
              </div>
              <div class="flex pt-4 text-sm text-gray-300">
                <div class="flex items-center mr-auto">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-yellow-500 mr-1"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    ></path>
                  </svg>
                  <p class="font-normal">4.5</p>
                </div>
                <div class="flex items-center font-medium text-white">
                  $1800
                  <span class="text-gray-300 text-sm font-normal"> /wk</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="relative flex flex-col justify-between bg-white shadow-md rounded-3xl bg-cover text-gray-800 overflow-hidden cursor-pointer w-full object-cover object-center rounded shadow-md h-64 my-2"
          style="
            background-image: url('https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=80');
          "
        >
          <div
            class="absolute bg-gradient-to-t from-blue-500 to-yellow-400 opacity-50 inset-0"
          ></div>
          <div class="relative flex flex-row items-end h-72 w-full">
            <div class="absolute right-0 top-0 m-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-9 w-9 p-2 text-gray-200 hover:text-blue-400 rounded-full hover:bg-white transition ease-in duration-200"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"
                ></path>
              </svg>
            </div>
            <div class="p-5 rounded-lg flex flex-col w-full">
              <h4 class="mt-1 text-white text-xl font-semibold leading-tight truncate">
                Loremipsum..
              </h4>
              <div class="flex justify-between items-center">
                <div class="flex flex-col">
                  <h2 class="text-sm flex items-center text-gray-300 font-normal">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4 mr-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                      ></path>
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                      ></path>
                    </svg>
                    India
                  </h2>
                </div>
              </div>
              <div class="flex pt-4 text-sm text-gray-300">
                <div class="flex items-center mr-auto">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-yellow-500 mr-1"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    ></path>
                  </svg>
                  <p class="font-normal">4.5</p>
                </div>
                <div class="flex items-center font-medium text-white">
                  $1800
                  <span class="text-gray-300 text-sm font-normal"> /wk</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <article class="">
      <PostAddForm :posts="posts"></PostAddForm>

      <div class="bg-white shadow rounded-lg" v-for="post in posts">
        <div class="flex flex-row px-2 py-3 mx-3">
          <div class="w-auto h-auto rounded-full border-2 border-green-500">
            <img
              class="w-12 h-12 object-cover rounded-full shadow cursor-pointer"
              alt="User avatar"
              src="https://images.unsplash.com/photo-1477118476589-bff2c5c4cfbb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=200&amp;q=200"
            />
          </div>
          <div class="flex flex-col mb-2 ml-4 mt-1">
            <div class="text-gray-600 text-sm font-semibold">
              {{ post.created_by.name }}
            </div>
            <div class="flex w-full mt-1">
              <div class="text-blue-700 font-base text-xs mr-1 cursor-pointer">
                UX Design
              </div>
              <div class="text-gray-400 font-thin text-xs">
                {{ post.created_at_formatted }} ago
              </div>
            </div>
          </div>
        </div>
        <div class="border-b border-gray-100"></div>
        <div class="text-gray-400 font-medium text-sm mb-7 mt-6 mx-3 px-2">
          <img class="rounded w-full" src="https://picsum.photos/536/354" />
        </div>
        <div class="text-gray-600 font-semibold mb-2 mx-3 px-2">
          Dummy text of the printing and typesetting industry
        </div>
        <div class="text-gray-500 text-sm mb-6 mx-3 px-2">{{ post.body }}</div>
        <div class="flex justify-start mb-4 border-t border-gray-100">
          <div class="flex w-full mt-1 pt-2 pl-5">
            <span
              class="bg-white transition ease-out duration-300 hover:text-red-500 border w-8 h-8 px-2 pt-2 text-center rounded-full text-gray-400 cursor-pointer mr-2"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                width="14px"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"
                ></path>
              </svg>
            </span>
            <img
              class="inline-block object-cover w-8 h-8 text-white border-2 border-white rounded-full shadow-sm cursor-pointer"
              src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2&amp;w=256&amp;h=256&amp;q=80"
              alt=""
            />
            <img
              class="inline-block object-cover w-8 h-8 -ml-2 text-white border-2 border-white rounded-full shadow-sm cursor-pointer"
              src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&amp;auto=format&amp;fit=facearea&amp;facepad=2&amp;w=256&amp;h=256&amp;q=80"
              alt=""
            />
            <img
              class="inline-block object-cover w-8 h-8 -ml-2 text-white border-2 border-white rounded-full shadow-sm cursor-pointer"
              src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=634&amp;q=80"
              alt=""
            />
            <img
              class="inline-block object-cover w-8 h-8 -ml-2 text-white border-2 border-white rounded-full shadow-sm cursor-pointer"
              src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2.25&amp;w=256&amp;h=256&amp;q=80"
              alt=""
            />
          </div>
          <div class="flex justify-end w-full mt-1 pt-2 pr-5">
            <span
              class="transition ease-out duration-300 hover:bg-blue-50 bg-blue-100 w-8 h-8 px-2 py-2 text-center rounded-full text-blue-400 cursor-pointer mr-2"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                width="14px"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"
                ></path>
              </svg>
            </span>
            <span
              class="transition ease-out duration-300 hover:bg-gray-50 bg-gray-100 h-8 px-2 py-2 text-center rounded-full text-gray-100 cursor-pointer"
            >
              <svg
                class="h-4 w-4 text-red-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"
                ></path>
              </svg>
            </span>
          </div>
        </div>
        <div class="flex w-full border-t border-gray-100">
          <div class="mt-3 mx-5 flex flex-row text-xs">
            <div class="flex text-gray-700 font-normal rounded-md mb-2 mr-4 items-center">
              Comments:
              <div class="ml-1 text-gray-400 text-ms">30</div>
            </div>
            <div class="flex text-gray-700 font-normal rounded-md mb-2 mr-4 items-center">
              Views:
              <div class="ml-1 text-gray-400 text-ms">60k</div>
            </div>
          </div>
          <div class="mt-3 mx-5 w-full flex justify-end text-xs">
            <div class="flex text-gray-700 rounded-md mb-2 mr-4 items-center">
              Likes:
              <div class="ml-1 text-gray-400 text-ms">120k</div>
            </div>
          </div>
        </div>
        <div
          class="relative flex items-center self-center w-full max-w-xl p-4 overflow-hidden text-gray-600 focus-within:text-gray-400"
        >
          <img
            class="w-10 h-10 object-cover rounded-full shadow mr-2 cursor-pointer"
            alt="User avatar"
            src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80"
          />
          <span class="absolute inset-y-0 right-0 flex items-center pr-6">
            <button
              type="submit"
              class="p-1 focus:outline-none focus:shadow-none hover:text-blue-500"
            >
              <svg
                class="w-6 h-6 transition ease-out duration-300 hover:text-blue-500 text-gray-400"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
            </button>
          </span>
          <input
            type="search"
            class="w-full py-2 pl-4 pr-10 text-sm bg-gray-100 border border-transparent appearance-none rounded-tg placeholder-gray-400 focus:bg-white focus:outline-none focus:border-blue-500 focus:text-gray-900 focus:shadow-outline-blue"
            style="border-radius: 25px"
            placeholder="Post a comment..."
            autocomplete="off"
          />
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import { useToastStore } from "@/stores/toast";
import { useUserStore } from "@/stores/user";
import { ref, onMounted, watch, toRefs } from "vue";
import PostService from "@/service/postService";

import UserService from "@/service/UserService";

import PostAddForm from "@/components/PostAddForm.vue";

import { useRoute } from "vue-router";

import { createToaster } from "@meforma/vue-toaster";
import MobileHeader from "@/components/MobileHeader.vue";

export default {
  components: {
    PostAddForm,
    MobileHeader,
  },

  setup(props) {
    const toast = useToastStore();
    const userStore = useUserStore();

    const posts = ref([]);
    const friendshipRequest = ref([]);

    const form = ref({
      body: "",
    });

    const user = ref({});
    const errors = ref([]);

    const route = useRoute();

    const toaster = createToaster();

    const getUserData = async () => {
      try {
        console.log(userStore.user);

        const response = await PostService.get_list_posts_by_user(route.params.id);
        // posts.value = response.data.posts;
        console.log(response);

        posts.value = response.data;
        user.value = response.user;

        const response2 = await UserService.getFriendRequest();
        friendshipRequest.value = response2.resquest.data;
        // console.log('______________')
        // console.log(response2.resquest.data)
      } catch (error) {
        console.log(error);
        errors.value.push(error.message);
      }
    };

    const sendFrienRequest = async (user_id) => {
      const response = await UserService.sendFriendRequest(user_id);
      if (response.resquest.message == "request send !") {
        toaster.success(response.resquest.message);
        // ajouter element dans la liste de requete
      } else {
        toaster.show(response.resquest.message);
      }
    };

    onMounted(getUserData);

    watch(
      () => route.params.id,
      (newValue, oldValue) => {
        getUserData();
      }
    );

    return {
      toast,
      userStore,
      form,
      errors,
      posts,
      getUserData,
      user,
      sendFrienRequest,
      friendshipRequest,
    };
  },
};
</script>
