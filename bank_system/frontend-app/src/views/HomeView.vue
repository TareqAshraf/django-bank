<template>
  <v-container>
    <v-img
      alt="Vue logo"
      src="../assets/logo.png"
      class="mx-auto"
      max-height="100"
    />

    <v-card>
      <v-card-title> Welcome to Your Vue.js App </v-card-title>

      <v-card-text>
        <HelloWorld msg="This is a Vuetify component" />
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
};
</script>
