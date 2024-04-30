<template>

<MobileHeader title="Friends" redirect_url="/friends" class="md:hidden"></MobileHeader>

  <div class="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-700 py-6 sm:py-12">
  
  
    <div class="mx-auto max-w-screen-xl px-4 w-full">
      <!-- Section Amis -->
      <div class="h-screen">
      
        <h2 v-if="friends" class="mb-4 font-bold text-2xl text-gray-100 hidden md:block">Friends</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          <FriendListItem
            v-for="friend in friends"
            :key="friend.id"
            :friend="friend"
            :friends="friends"
            :friendshipRequests="friendshipRequests"
          ></FriendListItem>
        </div>
      </div>
      <!-- Section Demandes d'amis -->
      <div class="mt-12">
        <h2 v-if="friendshipRequests" class="mb-4 font-bold text-2xl text-gray-100">Friends Request</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          <FriendshipRequestListItem
            v-for="request in friendshipRequests"
            :key="request.id"
            :friendship="request"
            :friends="friends"
            :friendshipRequests="friendshipRequests"
          ></FriendshipRequestListItem>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

import FriendshipRequestListItem from '@/components/FriendshipRequestListItem.vue'
import FriendListItem from '@/components/FriendListItem.vue'
import UserService from '@/service/UserService';
import {ref,onMounted} from 'vue'
import { useRoute } from "vue-router";
import { useUserStore } from "@/stores/user";
import MobileHeader from "@/components/MobileHeader.vue";




export default{

  components :{
    FriendshipRequestListItem,
    FriendListItem,
    MobileHeader
  },

  setup(){
    const friends=ref([]);
    const friendshipRequests=ref([])

    const userStore = useUserStore();

    const  getFriendsAndRequest = async () => {
      const response = await UserService.getFriendRequest()
      friendshipRequests.value=response.resquest.data;

      const response2 = await UserService.getFriends(userStore.user.id)
      friends.value=response2.data.friends;
      console.log(response2.data.friends)
      
    }

    onMounted(getFriendsAndRequest)

    return {friends,friendshipRequests};
  }
}
</script>