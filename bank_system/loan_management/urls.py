from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanProviderViewSet, LoanCustomerViewSet, BankPersonnelViewSet, LoanPlanViewSet, LoanFundViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'loan-providers', LoanProviderViewSet)
router.register(r'loan-customers', LoanCustomerViewSet)
router.register(r'bank-personnel', BankPersonnelViewSet)
router.register(r'loan-plans', LoanPlanViewSet)
router.register(r'loan-funds', LoanFundViewSet)
router.register(r'loans', LoanViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
