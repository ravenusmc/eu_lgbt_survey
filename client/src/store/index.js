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
    questionTwoData: [['View', 'Percentage'],
      ['Fairly rare', 59],
      ['Very rare', 22],
      ['Fairly widespread', 15],
      ['Very widespread', 4],
      ['Don`t know', 0]],
  },

  getters: {
    questionOneData: state => state.questionOneData,
    questionTwoData: state => state.questionTwoData,
  },

  actions: {

    // Fetch Question one data
    fetchQuestionOneData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/firstQuestionData';
      axios.post(path, payload)
        .then((res) => {
          // console.log(res.data[1]);
          res.data[0].sort((a, b) => b[1] - a[1]);
          res.data[1].sort((a, b) => b[1] - a[1]);
          // console.log(res.data[1]);
          commit('setQuestionOneData', res.data[0]);
          commit('setQuestionTwoData', res.data[1]);
        });
    },

  },

  mutations: {

    setQuestionOneData(state, data) {
      state.questionOneData = data;
    },

    setQuestionTwoData(state, data) {
      state.questionTwoData = data;
    },

  },

});
