<template>
  <div>
    <form @submit="submitForm">

      <div class='selectionFix'>
        <h3 class='font formTitles'>Select the Question:</h3>
        <select v-model="question" name="question">
          <option v-for="question in questions" v-bind:key="question" :value="question">
            {{ question }}
          </option>
        </select>
      </div>

      <div class='selectionFix'>
        <h3 class='font formTitles'>Select the Answer to be examined:</h3>
        <select v-model="answer" name="answer">
          <option v-for="answer in answers" v-bind:key="answer" :value="answer">
            {{ answer }}
          </option>
        </select>
      </div>

      <button>Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'MapForm',
  data() {
    return {
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
    submitForm(evt) {
      evt.preventDefault();
      const payload = {
        question: this.question,
        answer: this.answer,
      };
      console.log({ payload });
    },
  },
};
</script>

<style scoped>
</style>
