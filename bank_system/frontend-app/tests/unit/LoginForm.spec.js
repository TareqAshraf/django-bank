import Vue from "vue";
import Vuetify from "vuetify";
import AuthLogin from "./AuthLogin.vue";
import { mount, createLocalVue } from "@vue/test-utils";

const localVue = createLocalVue();
localVue.use(Vuetify);

describe("AuthLogin", () => {
  it("should render the AuthLogin component", () => {
    const wrapper = mount(AuthLogin, {
      localVue,
    });

    expect(wrapper.find(".auth-login").exists()).toBeTruthy();
  });

  it("should submit the form and redirect to the correct page", () => {
    const wrapper = mount(AuthLogin, {
      localVue,
    });

    wrapper.find('[name="username"]').setValue("user4");
    wrapper.find('[name="password"]').setValue("user@123");

    wrapper.trigger("submit");

    expect(wrapper.vm.$router.currentRoute.name).toBe("posts");
  });

  it("should show an error message if the username or password is incorrect", () => {
    const wrapper = mount(AuthLogin, {
      localVue,
    });

    wrapper.find('[name="username"]').setValue("user5");
    wrapper.find('[name="password"]').setValue("user@123");

    wrapper.trigger("submit");

    expect(wrapper.find("#error").exists()).toBeTruthy();
  });
});
