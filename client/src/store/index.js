import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    questionOneData: [['View', 'Percentage'],
      ['Fairly rare', 45],
      ['Fairly widespread', 34],
      ['Very rare', 9],
      ['Very widespread', 8],
      ['Don`t know', 4]],
  },

  getters: {
    questionOneData: state => state.questionOneData,
  },

  actions: {

    // Fetch Question one data
    fetchQuestionOneData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/firstQuestionData';
      axios.post(path, payload)
        .then((res) => {
          res.data.sort((a, b) => b[1] - a[1]);
          console.log(res.data);
          commit('setQuestionOneData', res.data);
        });
    },

  },

  mutations: {

    setQuestionOneData(state, data) {
      state.questionOneData = data;
    },

  },

});
