<template>
  <v-container>
    <v-form @submit.prevent="submit">
      <v-text-field label="Name" name="name" v-model="form.name"></v-text-field>

      <v-text-field
        label="Min Amount"
        name="min_amount"
        v-model="form.min_amount"
      ></v-text-field>

      <v-text-field
        label="Max Amount"
        name="max_amount"
        v-model="form.max_amount"
      ></v-text-field>

      <v-text-field
        label="Interest Rate"
        name="interest_rate"
        v-model="form.interest_rate"
      ></v-text-field>

      <v-text-field
        label="Duration"
        name="duration"
        v-model="form.duration"
      ></v-text-field>

      <v-select
        label="Loan Plan"
        name="loan_type"
        v-model="form.loan_type"
        :items="loanTypes"
      ></v-select>

      <v-btn type="submit">Submit</v-btn>
    </v-form>

    <p v-if="showError" id="error">Invalid data</p>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

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
        loan_type: null,
      },
      loanTypes: [
        {
          text: "Loan Provider",
          value: "loan_provider",
        },
        {
          text: "Loan Customer",
          value: "loan_customer",
        },
      ],
      showError: false,
    };
  },
  methods: {
    ...mapActions(["createPersonnelBank"]),
    submit() {
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

/* Add a margin to the form to make it look better */
.personnel-bank-form {
  margin: 20px;
}

/* Use the v-text-field component to render the name, min_amount, max_amount, interest_rate, duration, and loan_type fields */
v-text-field {
  margin: 5px;
}

/* Use the v-select component to render the loanTypes options */
v-select {
  margin: 5px;
}

/* Add a red background color to the error message */
#error {
  color: red;
}
</style>
