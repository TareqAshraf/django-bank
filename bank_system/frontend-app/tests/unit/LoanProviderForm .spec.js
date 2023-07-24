import Vue from "vue";
import Vuetify from "vuetify";
import LoanProviderForm from "./LoanProviderForm.vue";
import { mount, createLocalVue } from "@vue/test-utils";

const localVue = createLocalVue();
localVue.use(Vuetify);

describe("LoanProviderForm", () => {
  it("should render the LoanProviderForm component", () => {
    const wrapper = mount(LoanProviderForm, {
      localVue,
    });

    expect(wrapper.find(".loan-provider-form").exists()).toBeTruthy();
  });

  it("should submit the form and create a loan provider", () => {
    const wrapper = mount(LoanProviderForm, {
      localVue,
    });

    wrapper.find('[name="amount"]').setValue(1000);
    wrapper.find('[name="loan_plan"]').setValue("1 year");

    wrapper.trigger("submit");

    expect(wrapper.vm.showError).toBeFalsy();
  });

  it("should show an error message if the amount is invalid", () => {
    const wrapper = mount(LoanProviderForm, {
      localVue,
    });

    wrapper.find('[name="amount"]').setValue("invalid");
    wrapper.find('[name="loan_plan"]').setValue("1 year");

    wrapper.trigger("submit");

    expect(wrapper.vm.showError).toBeTruthy();
  });

  it("should show an error message if the loan plan is invalid", () => {
    const wrapper = mount(LoanProviderForm, {
      localVue,
    });

    wrapper.find('[name="amount"]').setValue(1000);
    wrapper.find('[name="loan_plan"]').setValue("invalid");

    wrapper.trigger("submit");

    expect(wrapper.vm.showError).toBeTruthy();
  });
});
