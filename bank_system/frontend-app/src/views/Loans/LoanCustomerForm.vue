<template>
  <div class="loan-customer-form">
    <div>
      <form @submit.prevent="submit">
        <div>
          <label for="amount">amount:</label>
          <input type="number" name="amount" v-model="form.amount" />
        </div>

        <div>
          <label for="term">term:</label>
          <input type="text" name="term" v-model="form.term" />
        </div>

        <!-- term -->
        <div>
          <label for="term">Term:</label>
          <v-select
            type="number"
            name="term"
            v-model="form.term"
            :items="termOptions"
          />
        </div>

        <div>
          <label for="amoritization">amoritization:</label>
          <!-- <input
            type="number"
            name="amoritization"
            v-model="form.amoritization"
          /> -->
          <!-- <div v-text="caluclatedAmorization" /> -->
          <div v-text="form.amoritization" />
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
  name: "LoanCustomerForm",
  components: {},
  data() {
    return {
      form: {
        amount: null,
        term: null,
        amoritization: 0,
      },
      showError: false,
    };
  },
  computed: {
    ...mapGetters({
      plans: "loans/plans",
    }),
    caluclatedAmorization() {
      return this.form.amount / this.form.term;
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
  methods: {
    ...mapActions(["createCustomerLoan"]),
    updateAmoritization() {
      this.form.amoritization = this.form.amount / this.form.term;
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