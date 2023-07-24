<template>
  <v-container>
    <v-form @submit.prevent="submit">
      <v-text-field
        label="Amount"
        name="amount"
        v-model="form.amount"
      ></v-text-field>

      <!-- loan plan -->
      <v-select
        label="Loan Plan"
        name="loan_plan"
        v-model="form.loan_plan"
        :items="planOptions"
      ></v-select>

      <v-btn type="submit">Submit</v-btn>
    </v-form>

    <p v-if="showError" id="error">Invalid data</p>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "LoanProviderForm",
  components: {},
  data() {
    return {
      form: {
        amount: null,
        loan_plan: null,
      },
      showError: false,
      planOptions: [
        {
          name: "1 year",
        },
        {
          name: "2 years",
        },
        {
          name: "3 years",
        },
      ],
    };
  },
  computed: {
    ...mapGetters({
      //plans: "loans/plans",
    }),
    // planOptions() {
    //   return this.plans.map((plan) => plan.name);
    // },
  },
  methods: {
    ...mapActions(["createLoanProvider"]),
    submit() {
      // this.$store.dispatch('loans/createLoanProvider', this.form)
      this.createLoanProvider(this.form)
        .then((loanProvider) => {
          console.log({ loanProvider });
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
.loan-provider-form {
  margin: 20px;
}

/* Use the v-text-field component to render the amount and loan_plan fields */
v-text-field {
  margin: 5px;
}

/* Use the v-select component to render the loan_plan options */
v-select {
  margin: 5px;
}

/* Add a red background color to the error message */
#error {
  color: red;
}
</style>