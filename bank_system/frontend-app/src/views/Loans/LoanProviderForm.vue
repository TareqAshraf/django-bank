<template>
  <div class="loan-customer-form">
    <div>
      <form @submit.prevent="submit">
        <div>
          <label for="amount">amount:</label>
          <input type="number" name="amount" v-model="form.amount" />
        </div>

        <!-- loan_plan -->
        <div>
          <label for="loan_plan">loan plan:</label>
          <v-select
            type="number"
            name="loan_plan"
            v-model="form.loan_plan"
            :items="planOptions"
          />
        </div>

        <button type="submit">Submit</button>
      </form>

      <p v-if="showError" id="error">Invalid data</p>
    </div>
  </div>
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
label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}
button[type="submit"] {
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
  border-radius: 30px;
}
button[type="submit"]:hover {
  background-color: #45a049;
}
input {
  margin: 5px;
  box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
  padding: 10px;
  border-radius: 30px;
}
#error {
  color: red;
}
</style>