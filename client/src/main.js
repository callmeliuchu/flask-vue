// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import store from "./store";
import Vue from 'vue';
import App from './App';
import router from './router';
import Editor from 'v-markdown-editor'
import 'vue-topo/dist/vue-topo.min.css'
import Vtopo from 'vue-topo'





// global register

Vue.config.productionTip = false;

Vue.use(Editor);
Vue.use(BootstrapVue)
// Vue.use(Vtopo)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});

