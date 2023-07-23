# views.py

from rest_framework import viewsets
from .models import LoanProvider, LoanCustomer, BankPersonnel, LoanPlan, LoanFund, Loan
from .serializers import LoanProviderSerializer, LoanCustomerSerializer, BankPersonnelSerializer, LoanPlanSerializer, LoanFundSerializer, LoanSerializer
from rest_framework.response import Response
from rest_framework import status


class LoanProviderViewSet(viewsets.ModelViewSet):
    queryset = LoanProvider.objects.all()
    serializer_class = LoanProviderSerializer


class LoanCustomerViewSet(viewsets.ModelViewSet):
    queryset = LoanCustomer.objects.all()
    serializer_class = LoanCustomerSerializer


class BankPersonnelViewSet(viewsets.ModelViewSet):
    queryset = BankPersonnel.objects.all()
    serializer_class = BankPersonnelSerializer


class LoanPlanViewSet(viewsets.ModelViewSet):
    queryset = LoanPlan.objects.all()
    serializer_class = LoanPlanSerializer

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user is a LoanProvider
        if user.is_authenticated and hasattr(user, 'bankpersonnel'):
            serializer.save()

        else:
            # Raise a PermissionDenied exception for unauthorized users
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only bank personnel can create Loan Plan.")


class LoanFundViewSet(viewsets.ModelViewSet):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user is a LoanProvider
        if user.is_authenticated and hasattr(user, 'loanprovider'):

            serializer.save(loan_provider=user.loanprovider,)

        else:
            # Raise a PermissionDenied exception for unauthorized users
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(
                "Only Loan Providers can create Loan Funds.")


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'loancustomer'):
            queryset = Loan.objects.filter(loan_customer=user.loancustomer)
            return queryset
        else:
            return Loan.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user is a LoanProvider
        if user.is_authenticated and hasattr(user, 'loancustomer'):
            serializer.save(loan_customer=user.loancustomer)

        else:
            # Raise a PermissionDenied exception for unauthorized users
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only Loan customer can create Loan .")
