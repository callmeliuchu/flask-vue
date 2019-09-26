<template>
  <div class="action">
    <b-container id="loginForm">
      <b-row align-h="center" align-v="center">
        <b-form @submit="authenticate">
          <b-form-group>
            <b-form-input
              v-model="email"
              type="text"
              placeholder="Email"
              required
            />
          </b-form-group>
          <b-form-group :invalid-feedback="invalidFeedback">
            <b-form-input
              v-model="password"
              type="password"
              placeholder="Password"
              required
            />
          </b-form-group>

          <div class="text-center">
            <button type="submit" variant="primary" block>Sing In</button>
          </div>
        </b-form>
      </b-row>
    </b-container>
  </div>
</template>



<script>
  import { EventBus } from '@/utils'
  export default {
    data(){
      return {
        email:"",
        password:"",
        errorMsg:""
      };
    },
    methods:{
      authenticate(){
        this.$store
          .dispatch("login",{email:this.email,password:this.password})
          .then(() => this.$router.push("/"));
      },
      register(){
        this.$store
          .dispatch("register",{email:this.email,password:this.password})
          .then(() => this.$router.push("/"));
      }
    },
    mounted(){
     EventBus.$on("failedRegistering",msg => {
       this.errorMsg = msg;
     });
     EventBus.$on("failedAuthentication",msg =>{
       this.errorMsg = msg;
     });
    },
    beforeDestroy(){
       EventBus.$off("failedRegistering");
       EventBus.$off("failedAuthentication");
    }
  }
</script>

<style scoped>
.action {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>
