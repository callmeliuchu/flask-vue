<!-- components/ForgotPassword.vue -->
<template>
  <div class="action">
    <b-container id="forgotPasswordForm">
      <b-row align-h="center" align-v="center">
        <b-form @submit="generateforgotPasswordToken">
          <b-form-group>
            <b-form-input
              v-model="email"
              type="text"
              placeholder="Enter Email."
              required
            />
          </b-form-group>
          <div class="text-center">
            <b-button type="submit" variant="primary" block>Reset Password</b-button>
          </div>
        </b-form>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { EventBus } from "@/utils";

export default {
  name: "reset",
  data() {
    return {
      email: "",
      errorMsg: ""
    };
  },
  methods: {
    generateforgotPasswordToken() {
      this.$store
        .dispatch("generateforgotPasswordToken", { email: this.email })
        .then(() => this.$router.push("/"));
    }
  },
  mounted() {
    EventBus.$on("failedRegistering", msg => {
      this.errorMsg = msg;
    });
    EventBus.$on("failedAuthentication", msg => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedRegistering");
    EventBus.$off("failedAuthentication");
  }
};
</script>

<style scoped>
.action {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>
