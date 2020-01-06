<template>
  <div>
    <section>
      <h1>Initial Study</h1>
      <form @submit="submitSelection">
        <div>
          <button>Submit</button>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SectionOne',
  methods: {
    submitSelection(evt) {
      evt.preventDefault();
      console.log('HI');
    },
  },
};
</script>

<style scoped>
form {
  display: 2px solid blue;
}
</style>
