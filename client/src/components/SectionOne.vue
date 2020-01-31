<template>
  <div>
      <form @submit="submitSelection">
        <v-card class="mx-auto">
          <v-card-text>
            <div>Please Select from the Below:</div>
            <div>Select the Country:</div>
            <div class="select is-info is-rounded">
              <select v-model="state" name="state">
                <option v-for="state in states" v-bind:key="state" :value="state">
                  {{ state }}</option>
              </select>
            </div>
            <div>Select the Sex:</div>
            <div class="select is-info is-rounded">
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
          </v-card-text>
        </v-card>
      </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'SectionOne',
  data() {
    return {
      state: 'Austria',
      states: ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Germany',
        'Denmark', 'Estonia', 'Greece', 'Spain', 'Finland', 'France', 'Croatia',
        'Hungary', 'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Malta',
        'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden', 'Slovenia',
        'Slovakia', 'United Kingdom'],
      orientation: 'Lesbian',
      orientations: ['Lesbian', 'Gay', 'Bisexual women', 'Bisexual men', 'Transgender'],
    };
  },
  methods: {
    ...mapActions([
      'fetchChartData',
    ]),
    submitSelection(evt) {
      evt.preventDefault();
      const payload = {
        state: this.state,
        orientation: this.orientation,
      };
      this.fetchChartData({ payload });
    },
  },
};
</script>

<style scoped>

.formTitle {
  text-transform: uppercase;
}

.formTitles {
  text-transform: uppercase;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 75px;
  background-color: #00AFC9;
}

.selectionFix {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
