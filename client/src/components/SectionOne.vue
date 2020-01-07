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
  data() {
    states: ['All', 'Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Germany',
     'Denmark', 'Estonia', 'Greece', 'Spain', 'Finland', 'France', 'Croatia',
     'Hungary', 'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Malta',
     'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden', 'Slovenia',
     'Slovakia', 'United Kingdom']
  },
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
