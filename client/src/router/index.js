import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Success from "../components/Success.vue";
import Plot from "../components/Plot.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/success",
    name: "Success",
    component: Success,
    props: true,
  },
  {
    path: "/stats",
    name: "Plot",
    component: Plot,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
