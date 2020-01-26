<template>
  <div>
    <form @submit="submitForm">

      <button>Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'MapForm',
  methods: {
    submitForm(evt) {
      evt.preventDefault();
    },
  },
};
</script>
<style scoped>
</style>
