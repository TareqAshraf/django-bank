from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LoanProviderViewSet,
    LoanCustomerViewSet,
    BankPersonnelViewSet,
    LoanPlanViewSet,
    LoanFundViewSet,
    LoanViewSet,
)
from . import views


router = DefaultRouter()
router.register(r"loan-providers", LoanProviderViewSet)
router.register(r"loan-customers", LoanCustomerViewSet)
router.register(r"bank-personnel", BankPersonnelViewSet)
router.register(r"loan-plans", LoanPlanViewSet)
router.register(r"loan-funds", LoanFundViewSet)
router.register(r"loans", LoanViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "loan-funds/get-sum",
    #     LoanFundViewSet.get_sum_of_all_loan_funds_that_not_ended,
    # ),
]
