import Vue from 'vue';
import VueCharts from 'vue-charts';
import VueGoogleCharts from 'vue-google-charts';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

// Google charts plugin
Vue.use(VueCharts);
Vue.use(VueGoogleCharts);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
