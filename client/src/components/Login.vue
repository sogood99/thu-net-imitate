<template>
  <div class="container">
    <img src="../assets/logo.gif" alt="Wifi Logo" class="wifi" />
    <div class="thu-text-container">
      <h1 class="text1">清华大学</h1>
      <h1 class="text2">无线校园网</h1>
      <h1 class="text3">Tsinghua University Wireless Network</h1>
    </div>
    <div class="qr-container">
      <img
        src="../assets/qrcode_for_258.jpg"
        alt="QR Code"
        height="126"
        width="126"
        class="qr"
      />
      <figcaption class="qr">
        欢迎关注 “清华大学信息服务”
      </figcaption>
    </div>
    <img src="../assets/attsinghua.png" alt="At Tsinghua" class="at-thu" />
    <div class="background-box">
      <div class="welcome-text">
        <h2>;)</h2>
        <h3>你好,Hi,</h3>
      </div>
      <div class="notification">
        <img
          src="../assets/notice.png"
          alt="Notification Text"
          class="notification-text"
        />
        <div class="notification-triangle-container">
          <div class="notification-triangle"></div>
        </div>
        <div class="fold-notification-triangle-container">
          <div class="fold-notification-triangle"></div>
        </div>
      </div>
      <div class="front-box">
        <div class="grid">
          <div class="user-label">
            <h3>用户名</h3>
            <h4>User ID</h4>
          </div>
          <input type="text" v-model="user" class="user-input" />
          <div class="password-label">
            <h3>密码</h3>
            <h4>Password</h4>
          </div>
          <input type="password" v-model="pass" class="pass-input" />
          <button v-on:click="submit" class="connect">
            <div class="text-top">连接</div>
            <div class="text-bottom">Connect</div>
          </button>
        </div>
        <div class="triangle-container">
          <div class="triangle"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  created() {
    if (localStorage.user != null && localStorage.user != "") {
      this.$router.push({ name: "Success" });
    }
  },
  data() {
    return {
      user: "",
      pass: "",
    };
  },
  methods: {
    submit: function() {
      var gResponse = fetch("http://localhost:5000/get", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: this.user, password: this.pass }),
      })
        .then((response) => response.json())
        .then((response) => {
          console.log(response);
          if (response.username != null) {
            localStorage.user = response.username;
            localStorage.usage = response.usage;
            this.$router.push({ name: "Success" });
          } else {
            window.alert("Incorrect Password");
          }
        });
    },
  },
};
</script>

<style scoped src="../styles/login.css"></style>
