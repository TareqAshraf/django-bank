<template>
  <div class="loan-customer-form">
    <div>
      <form @submit.prevent="submit">
        <!-- name -->
        <div>
          <label for="name">name:</label>
          <input type="text" name="name" v-model="form.name" />
        </div>

        <!-- min_amount -->
        <div>
          <label for="min_amount">min amount:</label>
          <input type="number" name="min_amount" v-model="form.min_amount" />
        </div>

        <!-- max_amount -->
        <div>
          <label for="max_amount">max amount:</label>
          <input type="number" name="max_amount" v-model="form.max_amount" />
        </div>

        <!-- interest_rate -->
        <div>
          <label for="interest_rate">Interest rate:</label>
          <input
            type="number"
            name="interest_rate"
            v-model="form.interest_rate"
          />
        </div>

        <!-- duration -->
        <div>
          <label for="duration">Interest rate:</label>
          <input type="number" name="duration" v-model="form.duration" />
        </div>

        <!-- loan_type -->
        <div>
          <label for="loan_type">loan plan:</label>
          <v-select
            name="loan_type"
            v-model="form.loan_type"
            :items="loanTypes"
          />
        </div>

        <button type="submit">Submit</button>
      </form>

      <p v-if="showError" id="error">Invalid data</p>
    </div>
    Invalid data
  </div>
</template>
    
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "PersonnelBankForm",
  components: {},
  data() {
    return {
      form: {
        name: null,
        min_amount: null,
        max_amount: null,
        interest_rate: null,
        duration: null,
        loan_typ: null,
      },
      loanTypes: {
        loan_provider: "Loan Provider",
        loan_customer: "Loan Customer",
      },
      showError: false,
    };
  },
  computed: {
    ...mapGetters({
      plans: "loans/plans",
    }),
    planOptions() {
      return this.plans.map((plan) => plan.name);
    },
  },
  methods: {
    ...mapActions(["createPersonnelBank"]),
    submit() {
      // this.$store.dispatch('loans/createPersonnelBank', this.form)
      this.createPersonnelBank(this.form)
        .then((personnelBank) => {
          console.log({ personnelBank });
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