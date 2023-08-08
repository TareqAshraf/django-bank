from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import datetime
from rest_framework import status

from loan_management.models import (
    LoanProvider,
    LoanCustomer,
    BankPersonnel,
    LoanPlan,
    LoanFund,
    Loan,
    Bank,
)
from loan_management.serializers import (
    LoanProviderSerializer,
    BankSerializer,
)


class LoanViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.loan_plan = LoanPlan.objects.create(
            name="Loan Plan 1",
            min_amount=1000,
            max_amount=5000,
            interest_rate=5,
            duration=12,
            loan_type="loan_customer",
        )
        self.loan_fund = LoanFund.objects.create(
            amount=1000,
            loan_plan=self.loan_plan,
        )

    def test_create_loan_successfully(self):
        """
        Test that a loan can be created successfully.
        """
        user = User.objects.get(username="user2")
        self.client.force_authenticate(user=user)
        data = {
            "amount": 500,
            "loan_plan": self.loan_plan.id,
        }
        response = self.client.post(
            "/loan-management/loans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("loan_id", response.data)

    def test_create_loan_with_invalid_loan_plan(self):
        """
        Test that a loan cannot be created with an invalid loan plan id.
        """
        user = User.objects.get(username="user2")
        self.client.force_authenticate(user=user)
        data = {
            "amount": 500,
            "loan_plan": 12345,
        }
        response = self.client.post(
            "/loan-management/loans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_loan_with_insufficient_funds(self):
        """
        Test that a loan cannot be created if there are insufficient funds.
        """
        user = User.objects.get(username="user2")
        self.client.force_authenticate(user=user)
        self.loan_fund.amount = 0
        self.loan_fund.save()
        data = {
            "amount": 500,
            "loan_plan": self.loan_plan.id,
        }
        response = self.client.post(
            "/loan-management/loans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_loan_by_loan_provider(self):
        """
        Test that a loan cannot be created by a loan provider.
        """

        self.client.force_authenticate(
            user=User.objects.create_user("loan_provider", "password")
        )
        data = {
            "amount": 500,
            "loan_plan": self.loan_plan.id,
        }
        response = self.client.post(
            "/loan-management/loans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LoanFundViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.loan_provider = LoanProvider.objects.create(
            user=User.objects.create_user("loan_provider", "password")
        )
        self.loan_plan = LoanPlan.objects.create(
            name="Loan Plan 1",
            min_amount=1000,
            max_amount=5000,
            interest_rate=5,
            duration=12,
            loan_type="loan_customer",
        )

    def test_create_loan_fund_successfully(self):
        """
        Test that a loan fund can be created successfully.
        """
        user = User.objects.get(username="user3")
        self.client.force_authenticate(user=user)
        data = {
            "amount": 1000,
            "loan_plan": self.loan_plan.id,
        }
        response = self.client.post(
            "/loan-management/loan-funds/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("loan_fund_id", response.data)

    def test_create_loan_fund_with_invalid_loan_plan(self):
        """
        Test that a loan fund cannot be created with an invalid loan plan id.
        """
        user = User.objects.get(username="user3")
        self.client.force_authenticate(user=user)
        data = {
            "amount": 1000,
            "loan_plan": 12345,
        }
        response = self.client.post(
            "/loan-funds/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_loan_fund_by_loan_customer(self):
        """
        Test that a loan fund cannot be created by a loan customer.
        """
        self.client.force_authenticate(
            user=User.objects.create_user("loan_customer", "password")
        )
        data = {
            "amount": 1000,
            "loan_plan": self.loan_plan.id,
        }
        response = self.client.post(
            "/loan-funds/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LoanPlanViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bank_personnel = BankPersonnel.objects.create(
            user=User.objects.create_user("bank_personnel", "password")
        )

    def test_create_loan_plan_successfully(self):
        """
        Test that a loan plan can be created successfully.
        """
        data = {
            "name": "Loan Plan 1",
            "min_amount": 1000,
            "max_amount": 5000,
            "interest_rate": 5,
            "duration": 12,
            "loan_type": "loan_customer",
        }
        response = self.client.post(
            "/loan-plans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("loan_plan_id", response.data)

    def test_create_loan_plan_by_loan_customer(self):
        """
        Test that a loan plan cannot be created by a loan customer.
        """
        self.client.force_authenticate(
            user=User.objects.create_user("loan_customer", "password")
        )
        data = {
            "name": "Loan Plan 1",
            "min_amount": 1000,
            "max_amount": 5000,
            "interest_rate": 5,
            "duration": 12,
            "loan_type": "loan_customer",
        }
        response = self.client.post(
            "/loan-plans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BankPersonnelViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_bank_personnel_successfully(self):
        """
        Test that a bank personnel can be created successfully.
        """
        data = {
            "username": "bank_personnel",
            "password": "password",
        }
        response = self.client.post(
            "/bank-personnel/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("bank_personnel_id", response.data)

    def test_create_bank_personnel_with_duplicate_username(self):
        """
        Test that a bank personnel cannot be created with a duplicate username.
        """
        data = {
            "username": "bank_personnel",
            "password": "password",
        }
        self.client.post("/bank-personnel/", data=data, content_type="application/json")
        response = self.client.post(
            "/bank-personnel/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_bank_personnel_by_loan_customer(self):
        """
        Test that a bank personnel cannot be created by a loan customer.
        """
        self.client.force_authenticate(
            user=User.objects.create_user("loan_customer", "password")
        )
        data = {
            "username": "bank_personnel",
            "password": "password",
        }
        response = self.client.post(
            "/bank-personnel/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LoanCustomerViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_loan_customer_successfully(self):
        """
        Test that a loan customer can be created successfully.
        """
        data = {
            "username": "loan_customer",
            "password": "password",
        }
        response = self.client.post(
            "/api/loan_customers/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("loan_customer_id", response.data)

    def test_create_loan_customer_with_duplicate_username(self):
        """
        Test that a loan customer cannot be created with a duplicate username.
        """
        data = {
            "username": "loan_customer",
            "password": "password",
        }
        self.client.post("/loans/", data=data, content_type="application/json")
        response = self.client.post(
            "/loans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_loan_customer_by_bank_personnel(self):
        """
        Test that a loan customer cannot be created by a bank personnel.
        """
        self.client.force_authenticate(
            user=User.objects.create_user("bank_personnel", "password")
        )
        data = {
            "username": "loan_customer",
            "password": "password",
        }
        response = self.client.post(
            "/loans/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BankViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_bank_successfully(self):
        """
        Test that a bank can be created successfully.
        """
        data = {
            "name": "Bank 1",
        }
        response = self.client.post(
            "/api/banks/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("bank_id", response.data)

    def test_retrieve_bank(self):
        """
        Test that a bank can be retrieved.
        """
        bank = Bank.objects.create(name="Bank 1")
        response = self.client.get(f"/api/banks/{bank.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, BankSerializer(bank).data)

    def test_update_bank(self):
        """
        Test that a bank can be updated.
        """
        bank = Bank.objects.create(name="Bank 1")
        data = {
            "name": "Bank 2",
        }
        response = self.client.put(
            f"/api/banks/{bank.id}/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Bank 2")

    def test_delete_bank(self):
        """
        Test that a bank can be deleted.
        """
        bank = Bank.objects.create(name="Bank 1")
        response = self.client.delete(f"/api/banks/{bank.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class LoanProviderViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_loan_provider_successfully(self):
        """
        Test that a loan provider can be created successfully.
        """
        data = {
            "username": "loan_provider",
            "password": "password",
        }
        response = self.client.post(
            "/api/loan_providers/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("loan_provider_id", response.data)

    def test_create_loan_provider_with_duplicate_username(self):
        """
        Test that a loan provider cannot be created with a duplicate username.
        """
        data = {
            "username": "loan_provider",
            "password": "password",
        }
        self.client.post("/loan-funds/", data=data, content_type="application/json")
        response = self.client.post(
            "/api/loan_providers/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_loan_provider_by_loan_customer(self):
        """
        Test that a loan provider cannot be created by a loan customer.
        """
        self.client.force_authenticate(
            user=User.objects.create_user("loan_customer", "password")
        )
        data = {
            "username": "loan_provider",
            "password": "password",
        }
        response = self.client.post(
            "/loan-funds/", data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)