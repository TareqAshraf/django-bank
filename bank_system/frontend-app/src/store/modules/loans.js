import axios from "axios";

const state = {
  customer_loans: [],
  plans: {},
  providers: {},
};

const getters = {
  plans: (state) => state.plans,
};

const actions = {
  getLoanPlans({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .post("plans")
        .then(({ data }) => {
          commit("FETCH_LOAN_PLANS", data);
          resolve(data);
        })
        .catch((res) => reject(res.data.errors));
    });
  },
  createCustomerLoan({ commit }, form) {
    return new Promise((resolve, reject) => {
      axios
        .post("api/loans", form)
        .then(({ data }) => {
          console.log({ data });
          commit("CREATE_CUSTOMER_LOAN", data);
          resolve(data);
        })
        .catch((res) => reject(res.data.errors));
    });
  },
  createLoanProvider({ commit }, form) {
    return new Promise((resolve, reject) => {
      axios
        .post("api/loan-provider", form)
        .then(({ data }) => {
          console.log({ data });
          commit("CREATE_LOAN_PROVIDER", data);
          resolve(data);
        })
        .catch((res) => reject(res.data.errors));
    });
  },
  createPersonnelBank({ commit }, form) {
    return new Promise((resolve, reject) => {
      axios
        .post("api/personnel-bank", form)
        .then(({ data }) => {
          console.log({ data });
          commit("CREATE_PERSONNEL_BANK", data);
          resolve(data);
        })
        .catch((res) => reject(res.data.errors));
    });
  },
  // createPersonnelLoan({}, form) {
  //   return new Promise((resolve, reject) => {
  //     axios
  //       .post("api/loans", form)
  //       .then(({ data }) => {
  //         console.log({ data });
  //         resolve(data);
  //       })
  //       .catch((res) => reject(res.data.errors));
  //   });
  // },
};

const mutations = {
  FETCH_LOAN_PLANS(state, plans) {
    plans.forEach((plan) => {
      state.plans[plan.id] = plan;
    });
    // state.plans = plans;
  },
  CREATE_CUSTOMER_LOAN(state, loan) {
    state.customer_loans.push(loan);
  },
  CREATE_LOAN_PROVIDER(state, providers) {
    providers.forEach((provider) => {
      state.providers[provider.id] = provider;
    });
  },
  CREATE_PERSONNEL_BANK(state, personnelBanks) {
    personnelBanks.forEach((bank) => {
      state.personnelBanks[bank.id] = bank;
    });
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
