import Vue from "vue";
import Vuetify from "vuetify";
import AuthLogin from "./AuthLogin.vue";
import { mount } from "@vue/test-utils";

describe("AuthLogin", () => {
  it("should render the AuthLogin component", () => {
    const wrapper = mount(AuthLogin);

    expect(wrapper.find(".v-container").exists()).toBeTruthy();
    expect(wrapper.find("v-text-field").exists()).toBeTruthy();
    expect(wrapper.find("v-btn").exists()).toBeTruthy();
  });

  it("should call the login method when the submit button is clicked", () => {
    const spy = jest.spyOn(AuthLogin.prototype, "login");

    const wrapper = mount(AuthLogin, {
      propsData: {
        form: {
          username: "user4",
          password: "user@123",
        },
      },
    });

    wrapper.find("v-btn").trigger("click");

    expect(spy).toHaveBeenCalledWith({
      username: "user4",
      password: "user@123",
    });
  });

  it("should navigate to the posts page when the login is successful", () => {
    const spy = jest.spyOn(AuthLogin.prototype, "$router");

    const wrapper = mount(AuthLogin, {
      propsData: {
        form: {
          username: "user4",
          password: "user@123",
        },
      },
    });

    wrapper.find("v-btn").trigger("click");

    expect(spy.mock.calls[0][1]).toEqual("/posts");
  });

  it("should show an error message if the login is not successful", () => {
    const wrapper = mount(AuthLogin, {
      propsData: {
        form: {
          username: "user4",
          password: "wrong_password",
        },
      },
    });

    wrapper.find("v-btn").trigger("click");

    expect(wrapper.find("#error").exists()).toBeTruthy();
  });
});
