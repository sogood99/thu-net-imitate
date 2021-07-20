import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
// import echarts from "echarts";
// Vue.prototype.$echarts = echarts;

createApp(App)
  .use(router)
  .mount("#app");
