<template>
  <v-container>
    <v-form @submit.prevent="submit">
      <v-text-field
        label="Amount"
        name="amount"
        v-model="form.amount"
      ></v-text-field>

      <v-select
        label="Term"
        name="term"
        v-model="form.term"
        :items="plans"
      ></v-select>

      <v-text-field
        label="Amortization"
        name="amoritization"
        v-model="form.amoritization"
      ></v-text-field>

      <v-btn type="submit">Submit</v-btn>
    </v-form>

    <p v-if="showError" id="error">Invalid data</p>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "LoanCustomerForm",
  components: {},
  data() {
    return {
      form: {
        amount: 0,
        term: 0,
        amortization: 0,
      },
      showError: false,
      plans: [
        {
          text: "1 year",
          value: 1,
        },
        {
          text: "2 years",
          value: 2,
        },
        {
          text: "3 years",
          value: 3,
        },
      ],
      // plans: {
      //   getPlans: "loans/plans",
      // },
    };
  },
  computed: {
    ...mapGetters({
      plans: {
        getPlans: "loans/plans",
      },
    }),
    caluclatedAmorization() {
      return this.form.amount / (this.form.term * 12);
    },
    termOptions: function () {
      let terms = {};
      Object.values(this.plans).forEach(
        (plan) => (terms[plan.duration] = plan.name)
      );
      return terms;
    },
  },
  watch: {
    "form.amount": "updateAmoritization",
    "form.term": "updateAmoritization",
  },
  // mounted() {
  //   axios.get("http://localhost:3000/api/plans").then((response) => {
  //     this.plans = response.data;
  //   });
  // },
  methods: {
    ...mapActions(["createCustomerLoan"]),
    updateAmoritization() {
      this.form.amoritization = this.form.amount / (this.form.term * 12);
    },
    submit() {
      this.createCustomerLoan(this.form)
        .then((loan) => {
          console.log({ loan });
          this.showError = false;
        })
        .catch((errors) => {
          console.log({ errors });
          this.showError = true;
        });
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

/* Add a margin to the form to make it look better */
.loan-customer-form {
  margin: 20px;
}

/* Use the v-text-field component to render the amount, term, and amortization fields */
v-text-field {
  margin: 5px;
}

/* Use the v-select component to render the termOptions options */
v-select {
  margin: 5px;
}

/* Add a red background color to the error message */
#error {
  color: red;
}
</style>
