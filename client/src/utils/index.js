import Vue from "vue";

export const EventBus = new Vue();

/**
 * Check to make sure the a JWT hasn't expired
 * @param {string} jwt JWT
 */
export function isValidJwt(jwt) {
  if (!jwt || jwt.split(".").length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split(".")[1]));
  const expire = new Date(data.exp * 1000);
  const now = new Date();
  return now < expire;
}
