<template>
  <div>
    <div class="title">
      <div>
        Sign Up
      </div>
    </div>
    <div id="sign-up-content">
      <!-- Username -->
      <b-form-group id="input-group-1" label="Username" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="username"
          required
          placeholder="Enter Username"
        ></b-form-input>
      </b-form-group>

      <!-- Email -->
      <b-form-group id="input-group-2" label="Email" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="email"
          type="email"
          required
          placeholder="Enter Email"
        ></b-form-input>
      </b-form-group>

      <!-- Password -->
      <b-form-group id="input-group-3" label="Password" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="password"
          type="password"
          required
          placeholder="Enter Password"
        ></b-form-input>
      </b-form-group>

      <!-- Confirm Password -->
      <b-form-group
        id="input-group-4"
        label="Confirm Password"
        label-for="input-4"
      >
        <b-form-input
          id="input-4"
          v-model="comfirmPassword"
          type="password"
          required
          placeholder="Enter Password"
        ></b-form-input>
      </b-form-group>

      <!-- checkbox -->
      <b-form-checkbox id="checkbox-1" v-model="checkbox" name="checkbox-1">
        I accept
      </b-form-checkbox>
      <b-button
        id="sign-btn"
        pill
        size="lg"
        block
        variant="info"
        to="/sign/verifyEmail"
        >SIGN UP</b-button
      >
      <b-button
        id="sign-btn"
        pill
        size="lg"
        block
        variant="outline-secondary"
        to="/sign/signIn"
        >SIGN IN</b-button
      >
    </div>
  </div>
</template>
<script>
// import VueX
import { mapState, mapMutations } from "vuex";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      comfirmPassword: "",
      checkbox: "",
    };
  },
  computed: {
    // get data from vuex
    ...mapState({
      baseURL: (state) => {
        return state.api.baseURL;
      },
      signUpURL: (state) => {
        return state.api.signUpURL;
      },
    }),
  },
};
</script>
<style>
#sign-up-content {
  padding: 2rem;
}
#sign-btn {
  margin-top: 1rem;
}
.title {
  font-size: 3rem;
  text-align: start;
  padding-left: 2rem;
}
</style>
