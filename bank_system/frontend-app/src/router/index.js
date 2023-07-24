import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";
import middlewarePipeline from "../router/middlewarePipeline";

// middlewares
// import guest from "../middlewares/guest";
// import auth from "../middlewares/auth";
// import optionalAuth from "../middlewares/optionalAuth";

// auth routes
import HomePage from "../views/HomePage.vue";
import Register from "../views/Auth/RegisterForm.vue";
import Login from "../views/Auth/LoginForm.vue";

// loan forms
import LoanCustomerForm from "../views/Loans/LoanCustomerForm.vue";
import LoanProviderForm from "../views/Loans/LoanProviderForm.vue";
import PersonnelBankForm from "../views/Loans/PersonnelBankForm.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { guest: true },
  },

  // Loans
  {
    path: "/loan-customer",
    name: "LoanCustomerForm",
    component: LoanCustomerForm,
    meta: { middleware: [auth] },
  },
  {
    path: "/loan-provider",
    name: "LoanProviderForm",
    component: LoanProviderForm,
    meta: { middleware: [auth] },
  },
  {
    path: "/personnel-bank",
    name: "PersonnelBankForm",
    component: PersonnelBankForm,
    meta: { middleware: [auth] },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.meta.middleware) {
    const middleware = to.meta.middleware;
    const context = {
      to,
      from,
      next,
      store,
    };

    return middleware[0]({
      ...context,
      next: middlewarePipeline(context, middleware, 1),
    });
  }

  return next();
});

export default router;
