<template>
  <div>
    <section>
      <form @submit="submitSelection">

        <div class='selectionFix'>
          <h3 class='font formTitles'>Select the Country:</h3>
          <select v-model="state" name="state">
            <option v-for="state in states" v-bind:key="state" :value="state">
              {{ state }}
            </option>
          </select>
        </div>

        <div class='selectionFix'>
          <h3 class='font formTitles'>Select the Orientation:</h3>
          <select v-model="orientation" name="orientation">
            <option v-for="orientation in orientations" v-bind:key="orientation"
            :value="orientation">
              {{ orientation }}
            </option>
          </select>
        </div>

        <div class='selectionFix'>
          <button class='font formTitles'>Submit</button>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'SectionOne',
  data() {
    return {
      state: 'All',
      states: ['All', 'Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Germany',
        'Denmark', 'Estonia', 'Greece', 'Spain', 'Finland', 'France', 'Croatia',
        'Hungary', 'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Malta',
        'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden', 'Slovenia',
        'Slovakia', 'United Kingdom'],
      orientation: 'All',
      orientations: ['All', 'Lesbian', 'Gay', 'Bisexual women', 'Bisexual men', 'Transgender'],
    };
  },
  methods: {
    ...mapActions([
      'fetchQuestionOneData',
    ]),
    submitSelection(evt) {
      evt.preventDefault();
      const payload = {
        state: this.state,
        orientation: this.orientation,
      };
      this.fetchQuestionOneData({ payload });
    },
  },
};
</script>

<style scoped>

.formTitles {
  text-transform: uppercase;
}

form {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-items: center;
  padding: 75px;
  background-color: #00AFC9;
}

.selectionFix {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
