<template>
  <v-container>
    <v-form @submit.prevent="submit">
      <v-text-field label="Username" name="username" v-model="form.username" />

      <v-text-field
        label="Password"
        name="password"
        v-model="form.password"
        type="password"
      />

      <v-btn type="submit">Submit</v-btn>
    </v-form>

    <p v-if="showError" id="error">Username or Password is incorrect</p>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "AuthLogin",
  components: {},
  data() {
    return {
      form: {
        username: "user4",
        password: "user@123",
      },
      showError: false,
    };
  },
  methods: {
    ...mapActions(["login"]),
    submit() {
      this.login({
        username: this.form.username,
        password: this.form.password,
      })
        .then(() => {
          this.$router.push("/posts");
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
