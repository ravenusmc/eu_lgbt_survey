import Vue from 'vue';
import VueCharts from 'vue-charts';
import VueGoogleCharts from 'vue-google-charts';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

// Google charts plugin
Vue.use(VueCharts);
Vue.use(VueGoogleCharts);
// Vuetify code
Vue.use(Vuetify);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
