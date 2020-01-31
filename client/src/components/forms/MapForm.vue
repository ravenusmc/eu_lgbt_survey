<template>
  <div>
    <form @submit="submitForm">

      <v-card class="mx-auto">
        <v-card-text class='formFix'>
          <div>Select the Question:</div>
          <div class="select is-info is-rounded">
            <select v-model="question" name="question">
              <option v-for="question in questions" v-bind:key="question" :value="question">
                {{ question }}
              </option>
            </select>
          </div>
          <div>Select the Answer to be examined:</div>
          <div class="select is-info is-rounded">
            <select v-model="answer" name="answer">
              <option v-for="answer in answers" v-bind:key="answer" :value="answer">
                {{ answer }}
              </option>
            </select>
          </div>
          <div>Select the Sex Choice::</div>
          <div class="select is-info is-rounded">
            <select v-model="sex" name="sex">
              <option v-for="sex in sexChoices" v-bind:key="sex" :value="sex">
                {{ sex }}
              </option>
            </select>
          </div>
          <div class='selectionFix'>
            <button>Submit</button>
          </div>
        </v-card-text>
      </v-card>


    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'MapForm',
  data() {
    return {
      sex: 'Lesbian',
      sexChoices: ['Lesbian', 'Gay', 'Bisexual women', 'Bisexual men', 'Transgender'],
      answer: 'Very widespread',
      answers: ['Very widespread', 'Fairly widespread', 'Fairly rare', 'Very rare',
        'Don`t know'],
      question: 'In your opinion, how widespread is offensive language about lesbian gay bisexual or transgender people by politicians in the country where you live?',
      questions: ['In your opinion, how widespread is offensive language about lesbian gay bisexual or transgender people by politicians in the country where you live?',
        'In your opinion, how widespread is same-sex partners holding hands in public in the country where you live?',
        'In your opinion, how widespread are expressions of hatred and aversion towards lesbian, gay, bisexual and/or transgender in public in the country where you live?',
        'In your opinion, how widespread are assaults and harassment against lesbian, gay, bisexual and/or transgender people in the country where you live?',
        'In your opinion, how widespread are casual jokes in everyday life about lesbian, gay, bisexual and/or transgender people in the country you live?'],
    };
  },
  methods: {
    ...mapActions([
      'fetchMapData',
    ]),
    submitForm(evt) {
      evt.preventDefault();
      const payload = {
        question: this.question,
        answer: this.answer,
        sex: this.sex,
      };
      this.fetchMapData({ payload });
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #00AFC9;
  padding: 20px;
}

.formFix {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.selectionFix {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
