import Vuex from "vuex";
import Vue from "vue";
// import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import loans from "./modules/loans";

// Load Vuex
Vue.use(Vuex);
// Create store
export default new Vuex.Store({
  modules: {
    auth,
    loans,
  },
  // plugins: [createPersistedState()],
});
