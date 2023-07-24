import Vue from "vue";
import Vuetify from "vuetify";
import LoanCustomerForm from "./LoanCustomerForm.vue";
import { mount, createLocalVue } from "@vue/test-utils";

const localVue = createLocalVue();
localVue.use(Vuetify);

describe("LoanCustomerForm", () => {
  it("should render the LoanCustomerForm component", () => {
    const wrapper = mount(LoanCustomerForm, {
      localVue,
    });

    expect(wrapper.find(".loan-customer-form").exists()).toBeTruthy();
  });

  it("should submit the form and create a customer loan", () => {
    const wrapper = mount(LoanCustomerForm, {
      localVue,
    });

    wrapper.find('[name="amount"]').setValue(1000);
    wrapper.find('[name="term"]').setValue(1);

    wrapper.trigger("submit");

    expect(wrapper.vm.$refs.form.valid).toBeTruthy();
    expect(wrapper.vm.showError).toBeFalsy();
  });

  it("should show an error message if the form is invalid", () => {
    const wrapper = mount(LoanCustomerForm, {
      localVue,
    });

    wrapper.trigger("submit");

    expect(wrapper.vm.$refs.form.valid).toBeFalsy();
    expect(wrapper.vm.showError).toBeTruthy();
  });
});
