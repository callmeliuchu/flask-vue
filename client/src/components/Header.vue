<template>
  <div>
    <b-navbar type="dark" variant="dark" fixed="top">
      <b-navbar-nav>
        <b-nav-item>
          <router-link to="/">Home</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
          <span v-if="isAuthenticated"><a @click="logout">Logout</a></span>
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => this.$router.push("/"));
    }
  }
};
</script>
