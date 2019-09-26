import Vue from "vue";
import Vuex from "vuex";

import { authenticate, register, generateforgotPasswordToken } from "@/api";
import { isValidJwt, EventBus } from "@/utils";

Vue.use(Vuex);

const state = {
  jwt: ""
};

const actions = {
  login(context, userData) {
    context.commit("setUserData", { userData });
    return authenticate(userData)
      .then(response =>
        context.commit("setJwtToken", { jwt: response.data.access_token })
      )
      .catch(error => {
        console.log("Error Authenticating: ", error);
        EventBus.$emit("failedAuthentication", error);
      });
  },
  register(context, userData) {
    context.commit("setUserData", { userData });
    return register(userData)
      .then(context.dispatch("login", userData))
      .catch(error => {
        console.log("Error Registering: ", error);
        EventBus.$emit("failedRegistering: ", error);
      });
  },
  generateforgotPasswordToken(context, userData) {
    context.commit("setUserData", { userData });
    return generateforgotPasswordToken(userData)
      .then(context.dispatch("login", userData))
      .catch(error => {
        console.log("Error Sending reset email: ", error);
        EventBus.$emit("failedResetEmail: ", error);
      });
  },
  logout(context) {
    context.commit("clearUserData");
  }
};

const mutations = {
  setUserData(state, payload) {
    console.log("setUserData payload = ", payload);
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    console.log("setJwtToken payload = ", payload);
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
  clearUserData(state) {
    state.userData = "";
    state.jwt = "";
  }
};

const getters = {
  // reusable data accessors
  isAuthenticated(state) {
    return isValidJwt(state.jwt);
  }
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
});

export default store;
