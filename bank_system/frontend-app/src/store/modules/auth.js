import axios from "axios";

const state = {
  user: null,
  posts: null,
};

const getters = {
  //
};

const actions = {
  async Register({ dispatch }, form) {
    await axios.post("domain.dev/api/v1/register/register", form);
    let UserForm = new FormData();
    UserForm.append("username", form.username);
    UserForm.append("password", form.password);
    await dispatch("LogIn", UserForm);
  },
  LogIn({ commit }, form) {
    return new Promise((resolve, reject) => {
      axios
        .post("login", form)
        .then(async (response) => {
          try {
            console.log({ response });
            await commit("setUser", response);
            resolve(response.data);
          } catch (e) {
            console.log({ e });
          }
        })
        .catch((errors) => {
          console.log({ errors });
          reject(errors);
        });
    });
  },
  async LogOut({ commit }) {
    let user = null;
    commit("logout", user);
  },
  async CreatePost({ dispatch }, post) {
    await axios.post("post", post);
    await dispatch("GetPosts");
  },
  async GetPosts({ commit }) {
    let response = await axios.get("posts");
    commit("setPosts", response.data);
  },
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setPosts(state, posts) {
    state.posts = posts;
  },
  LogOut(state) {
    state.user = null;
    state.posts = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
