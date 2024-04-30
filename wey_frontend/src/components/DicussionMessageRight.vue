<template>
  <div class="col-start-6 col-end-13 p-3 rounded-lg">
    <div class="flex items-center justify-start flex-row-reverse">
      <div
        class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0"
      >
        {{ initial }}
      </div>
      <div class="relative mr-3 text-sm bg-indigo-100 py-2 px-4 shadow rounded-xl">
        <div>{{ message }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    message: "",
    initial: "",
  },

  setup(props) {},
};
</script>
