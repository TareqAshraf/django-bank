export default function auth({ next, store }) {
  if (store.getters["auth/user"]) {
    return next();
  }

  return next("/login");
}

/*
export default function isLoanProvider({ next, store }) {
  let user = store.getters["auth/user"];

  if (user && user.role == 'loan_provider') {
      return next();
  }

  return next("/login");
}0
*/
