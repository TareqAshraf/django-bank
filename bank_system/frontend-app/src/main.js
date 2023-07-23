import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";
import axios from "axios";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://127.0.0.1:8000/api";

Vue.config.productionTip = false;

Window.Vue = require("vue");

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
