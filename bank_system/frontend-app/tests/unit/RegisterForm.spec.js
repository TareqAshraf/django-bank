import Vue from "vue";
import Vuetify from "vuetify";
import RegisterForm from "./RegisterForm.vue";
import { mount, createLocalVue } from "@vue/test-utils";

const localVue = createLocalVue();
localVue.use(Vuetify);

describe("RegisterForm", () => {
  it("should render the RegisterForm component", () => {
    const wrapper = mount(RegisterForm, {
      localVue,
    });

    expect(wrapper.find(".register").exists()).toBeTruthy();
  });

  it("should submit the form and redirect to the correct page", () => {
    const wrapper = mount(RegisterForm, {
      localVue,
    });

    wrapper.find('[name="username"]').setValue("test-user");
    wrapper.find('[name="password"]').setValue("test-password");
    wrapper.find('[name="confirmPassword"]').setValue("test-password");
    wrapper.find('[name="role"]').setValue(1);

    wrapper.trigger("submit");

    expect(wrapper.vm.$router.currentRoute.name).toBe("loan-provider");
  });

  it("should show an error message if the username already exists", () => {
    const wrapper = mount(RegisterForm, {
      localVue,
    });

    wrapper.find('[name="username"]').setValue("test-user");
    wrapper.find('[name="password"]').setValue("test-password");
    wrapper.find('[name="confirmPassword"]').setValue("test-password");
    wrapper.find('[name="role"]').setValue(1);

    wrapper.vm.$store.state.users.push({ username: "test-user" });

    wrapper.trigger("submit");

    expect(wrapper.find("#error").exists()).toBeTruthy();
  });
});
