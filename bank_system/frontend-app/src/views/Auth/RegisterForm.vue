<template>
  <v-container class="register">
    <v-form @submit.prevent="submit">
      <v-text-field
        label="Username"
        name="username"
        v-model="form.username"
        min-width="50"
      />

      <v-select
        label="Role"
        name="role"
        v-model="form.role"
        :items="items"
        min-width="50"
      ></v-select>

      <v-text-field
        label="Password"
        name="password"
        v-model="form.password"
        type="password"
        min-width="50"
      />

      <v-text-field
        label="Confirm Password"
        name="confirmPassword"
        v-model="form.confirmPassword"
        type="password"
        min-width="50"
      />

      <v-btn type="submit">Submit</v-btn>
    </v-form>

    <p v-if="showError" id="error">Username already exists</p>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "RegisterForm",
  components: {},
  data() {
    return {
      form: {
        username: null,
        password: null,
        confirmPassword: null,
        role: null,
      },
      showError: false,
      items: [
        {
          text: "Loan Provider",
          value: 1,
        },
        {
          text: "Loan Customer",
          value: 2,
        },
        {
          text: "Bank Personnel",
          value: 3,
        },
      ],
    };
  },
  methods: {
    ...mapActions(["register"]),
    // submit() {
    //   this.register({
    //     username: this.form.username,
    //     password: this.form.password,
    //     role: this.form.role,
    //   })
    //     .then(() => {
    //       this.$router.push("/posts");
    //       this.showError = false;
    //     })
    //     .catch((error) => {
    //       console.log({ error });
    //       this.showError = true;
    //     });
    // },

    submit() {
      this.register({
        username: this.form.username,
        password: this.form.password,
        role: this.form.role,
      })
        .then(() => {
          if (this.form.role === 1) {
            this.$router.push("/loan-provider");
          } else if (this.form.role === 2) {
            this.$router.push("/loan-customer");
          } else if (this.form.role === 3) {
            this.$router.push("/personnel-bank");
          }
          this.showError = false;
        })
        .catch((error) => {
          console.log({ error });
          this.showError = true;
        });
    },
  },
};
</script>
