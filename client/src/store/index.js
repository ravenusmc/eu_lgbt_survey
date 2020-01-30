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
    questionThreeData: [['View', 'Percentage'],
      ['Fairly rare', 43],
      ['Fairly widespread', 39],
      ['Very widespread', 9],
      ['Very rare', 7],
      ['Don`t know', 2]],
    questionFourData: [['View', 'Percentage'],
      ['Fairly rare', 56],
      ['Fairly widespread', 21],
      ['Very rare', 10],
      ['Don`t know', 8],
      ['Very widespread', 5]],
    questionFiveData: [['View', 'Percentage'],
      ['Fairly widespread', 46],
      ['Very widespread', 41],
      ['Fairly rare', 10],
      ['Very rare', 2],
      ['Don`t know', 1]],
    mapData: [['Austria', 8],
      ['Belgium', 2],
      ['Bulgaria', 47],
      ['Cyprus', 32],
      ['Czech Republic', 6],
      ['Germany', 2],
      ['Denmark', 2],
      ['Estonia', 4],
      ['Greece', 30],
      ['Spain', 11],
      ['Finland', 6],
      ['France', 9],
      ['Croatia', 34],
      ['Hungary', 32],
      ['Ireland', 8],
      ['Italy', 63],
      ['Lithuania', 60],
      ['Luxembourg', 0],
      ['Latvia', 36],
      ['Malta', 24],
      ['Netherlands', 2],
      ['Poland', 34],
      ['Portugal', 7],
      ['Romania', 42],
      ['Sweden', 5],
      ['Slovenia', 29],
      ['Slovakia', 32],
      ['United Kingdom', 7]],
  },

  getters: {
    questionOneData: state => state.questionOneData,
    questionTwoData: state => state.questionTwoData,
    questionThreeData: state => state.questionThreeData,
    questionFourData: state => state.questionFourData,
    questionFiveData: state => state.questionFiveData,
    mapData: state => state.mapData,
  },

  actions: {

    // Fetch and set the data for all the charts.
    fetchChartData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/firstQuestionData';
      axios.post(path, payload)
        .then((res) => {
          res.data[0].sort((a, b) => b[1] - a[1]);
          res.data[1].sort((a, b) => b[1] - a[1]);
          res.data[2].sort((a, b) => b[1] - a[1]);
          res.data[3].sort((a, b) => b[1] - a[1]);
          res.data[4].sort((a, b) => b[1] - a[1]);
          commit('setQuestionOneData', res.data[0]);
          commit('setQuestionTwoData', res.data[1]);
          commit('setQuestionThreeData', res.data[2]);
          commit('setQuestionFourData', res.data[3]);
          commit('setQuestionFiveData', res.data[4]);
        });
    },

    // This action will get the data for the map
    fetchMapData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/fetchMapData';
      axios.post(path, payload)
        .then((res) => {
          commit('setMapData', res.data);
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

    setQuestionThreeData(state, data) {
      state.questionThreeData = data;
    },

    setQuestionFourData(state, data) {
      state.questionFourData = data;
    },

    setQuestionFiveData(state, data) {
      state.questionFiveData = data;
    },

    setMapData(state, data) {
      state.mapData = data;
    },

  },

});
