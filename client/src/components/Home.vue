<template>
  <div class="homeTemplate">
    <h1 v-if="!isAuthenticated">{{ msg }}</h1>
    <h1 v-else>You are logged in!</h1>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  }
};
</script>

<style>
.homeTemplate {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>
