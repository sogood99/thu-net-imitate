import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Success from "../components/Success.vue";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
