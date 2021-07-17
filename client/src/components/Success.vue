<template>
  <div class="container">
    <!-- Background Gradient Decorator (Top) -->
    <img
      src="../assets/popup_bg.png"
      alt="Background Decorator"
      class="bg-gradient"
    />
    <!-- Backgound box used as orange decoration and container -->
    <div class="background-box">
      <!-- Triangle decorator -->
      <div class="triangle-container">
        <div class="triangle"></div>
      </div>
      <!-- White Front Box used as decorator and container -->
      <div class="front-box">
        <div class="grid">
          <div class="name">
            <h3>{{ user }}</h3>
          </div>
          <div class="connect-label">
            <p>已连接</p>
            <p>Duration</p>
          </div>
          <div class="time">05:01:50</div>
          <div class="usage-label">
            <p>已用流量</p>
            <p>Usage</p>
          </div>
          <div class="usage">
            <!-- 0-50 Gb Box design -->
            <div class="box-large">
              <div class="text">50</div>
              <div class="box"></div>
            </div>
            <!-- 50-75 etc Gb Box design -->
            <div class="box-small" id="one">
              <div class="text">75</div>
              <div class="box"></div>
            </div>
            <div class="box-small" id="two">
              <div class="text">100</div>
              <div class="box"></div>
            </div>
            <div class="box-small" id="three">
              <div class="text">125</div>
              <div class="box"></div>
            </div>
            <!-- End decoration -->
            <div class="stripe-empty"></div>
            <div class="stripe"></div>
            <div class="stripe-empty"></div>
            <div class="stripe"></div>
            <div class="usage-box" v-bind:style="{ width: perc }"></div>
            <div class="usage-text">{{ usage }} G</div>
          </div>
        </div>
        <!-- Disconnect button and its container -->
        <div class="disconnect">
          <button v-on:click="logout">
            <div class="text-top">断开连接</div>
            <div class="text-bottom">Disconnect</div>
          </button>
          <div class="fold-triangle-container">
            <div class="fold-triangle"></div>
          </div>
        </div>
        <!-- Four Links Under Background (Currently not linked to anything) -->
        <div class="links">
          <ul>
            <li>
              <a href=""
                ><img src="../assets/popup_info.gif" alt="Info Icon" />Info</a
              >
            </li>
            <li>
              <a href=""
                ><img src="../assets/popup_lib.gif" alt="Lib Icon" />Lib</a
              >
            </li>
            <li>
              <a href=""
                ><img
                  src="../assets/popup_learn.gif"
                  alt="Learn Icon"
                />Learn</a
              >
            </li>
            <li>
              <a href=""
                ><img src="../assets/popup_mail.gif" alt="Mail Icon" />Mail</a
              >
            </li>
          </ul>
        </div>
        <!-- Shadow below -->
        <img
          src="../assets/popup_shadow.png"
          alt="Shadow Decorator"
          class="shadow"
        />
      </div>
      <!-- Text to decorate background box -->
      <div class="text">
        <h1>:P</h1>
        <h2>欢迎,</h2>
        <h3>Welcome</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Success",
  data() {
    return {
      // User is username, perc is usage/125 * 100
      user: "",
      usage: "",
      perc: "",
    };
  },
  created() {
    // Run on load, load the username and usage from localstorage
    this.user = localStorage.user;
    this.usage = localStorage.usage;
    this.perc = (Math.min(this.usage, 125) / 1.25).toString() + "%";
  },
  methods: {
    logout() {
      // Called by logout button, sends username to backend to add random value, then routes to login
      window.alert("连接已断开");
      fetch("http://localhost:5000/logout", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: this.user }),
      });
      localStorage.user = "";
      localStorage.time_sec = 0;
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

<style scoped src="../styles/success.css"></style>
