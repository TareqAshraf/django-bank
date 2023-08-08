# views.py

from rest_framework import viewsets
from .models import LoanProvider, LoanCustomer, BankPersonnel, LoanPlan, LoanFund, Loan, Bank
from .serializers import (
    LoanProviderSerializer,
    LoanCustomerSerializer,
    BankPersonnelSerializer,
    LoanPlanSerializer,
    LoanFundSerializer,
    LoanSerializer,
    BankSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import datetime
import decimal
from django.db import models
from rest_framework.decorators import api_view


class LoanProviderViewSet(viewsets.ModelViewSet):
    queryset = LoanProvider.objects.all()
    serializer_class = LoanProviderSerializer

    def create(self, request):
        user = User.objects.filter(username=request.data["username"]).first()

        if user:
            return Response(
                {"message": "Username already exists"}, status=status.HTTP_409_CONFLICT
            )
        else:
            user = User.objects.create_user(
                username=request.data["username"],
                password=request.data["password"],
            )

        Loan_Provider = LoanProvider.objects.create(user=user)

        return Response(
            {"message": "LoanProvider created successfully"},
            status=status.HTTP_201_CREATED,
        )


class LoanCustomerViewSet(viewsets.ModelViewSet):
    queryset = LoanCustomer.objects.all()
    serializer_class = LoanCustomerSerializer

    def create(self, request):
        user = User.objects.filter(username=request.data["username"]).first()
        if user:
            return Response(
                {"message": "Username already exists"}, status=status.HTTP_409_CONFLICT
            )
        else:
            user = User.objects.create_user(
                username=request.data["username"],
                password=request.data["password"],
            )

        Loan_Customer = LoanCustomer.objects.create(user=user)

        return Response(
            {"message": "LoanCustomer created successfully"},
            status=status.HTTP_201_CREATED,
        )


class BankPersonnelViewSet(viewsets.ModelViewSet):
    queryset = BankPersonnel.objects.all()
    serializer_class = BankPersonnelSerializer

    def create(self, request):
        user = User.objects.filter(username=request.data["username"]).first()
        if user:
            return Response(
                {"message": "Username already exists"}, status=status.HTTP_409_CONFLICT
            )
        else:
            user = User.objects.create_user(
                username=request.data["username"],
                password=request.data["password"],
            )

        Bank_Personnel = BankPersonnel.objects.create(user=user)

        return Response(
            {"message": "BankPersonnel created successfully"},
            status=status.HTTP_201_CREATED,
        )


class LoanPlanViewSet(viewsets.ModelViewSet):
    queryset = LoanPlan.objects.all()
    serializer_class = LoanPlanSerializer

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user is a LoanProvider
        if user.is_authenticated and hasattr(user, "bankpersonnel"):
            serializer.save()

        else:
            # Raise a PermissionDenied exception for unauthorized users
            from rest_framework.exceptions import PermissionDenied

            raise PermissionDenied("Only bank personnel can create Loan Plan.")


class LoanFundViewSet(viewsets.ModelViewSet):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer

    # loan_provider=user.loanprovider,
    def create(self, request):
        user = self.request.user
        # Check if the user is a LoanProvider
        if user.is_authenticated and hasattr(user, "loanprovider"):
            # sum of loan found
            if (
                LoanPlan.objects.get(id=self.request.data["loan_plan"]).loan_type
                == "loan_customer"
            ):
                return Response(
                    {"message": "loan type is not correct"},
                    status=status.HTTP_409_CONFLICT,
                )
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )

        else:
            # Raise a PermissionDenied exception for unauthorized users
            from rest_framework.exceptions import PermissionDenied

            raise PermissionDenied("Only Loan Provider can create Found.")

    def perform_create(self, serializer):
        user = self.request.user
        current_date = datetime.date.today()
        new_date = current_date + datetime.timedelta(
            days=LoanPlan.objects.get(id=self.request.data["loan_plan"]).duration * 30
        )
        total_amount = float(
            serializer.validated_data["amount"]
            + (
                serializer.validated_data["amount"]
                * (
                    LoanPlan.objects.get(
                        id=self.request.data["loan_plan"]
                    ).interest_rate
                    / 100
                )
            ),
        )
        serializer.save(
            loan_provider=user.loanprovider,
            ended_at=new_date,
            amount_with_interest=(total_amount),
        )


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "loancustomer"):
            queryset = Loan.objects.filter(loan_customer=user.loancustomer)
            return queryset
        else:
            return Loan.objects.none()

    def create(self, request):
        user = self.request.user
        # Check if the user is a LoanProvider
        if user.is_authenticated and hasattr(user, "loancustomer"):
            # sum of loan found
            if (
                LoanPlan.objects.get(id=self.request.data["loan_plan"]).loan_type
                == "loan_provider"
            ):
                return Response(
                    {"message": "loan type is not correct"},
                    status=status.HTTP_409_CONFLICT,
                )
            loan_funds = LoanFund.objects.filter(ended_at__gt=datetime.date.today())
            total_amount = 0
            for loan_fund in loan_funds:
                total_amount += loan_fund.amount
            # sum of loans
            loans = Loan.objects.filter(ended_at__gt=datetime.date.today())
            for loan in loans:
                total_amount -= loan.amount
            if total_amount > self.request.data["amount"]:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED, headers=headers
                )
            elif total_amount > 0:
                return Response(
                    {"message": "the maxemum number for lons is " + str(total_amount)},
                    status=status.HTTP_409_CONFLICT,
                )
            else:
                return Response(
                    {"message": "thir are no money"},
                    status=status.HTTP_409_CONFLICT,
                )
        else:
            # Raise a PermissionDenied exception for unauthorized users
            from rest_framework.exceptions import PermissionDenied

            raise PermissionDenied("Only Loan customer can create Loan .")

    def perform_create(self, serializer):
        user = self.request.user
        current_date = datetime.date.today()
        new_date = current_date + datetime.timedelta(
            days=LoanPlan.objects.get(id=self.request.data["loan_plan"]).duration * 30
        )
        total_amount = float(
            serializer.validated_data["amount"]
            + (
                serializer.validated_data["amount"]
                * (
                    LoanPlan.objects.get(
                        id=self.request.data["loan_plan"]
                    ).interest_rate
                    / 100
                )
            ),
        )
        serializer.save(
            loan_customer=user.loancustomer,
            ended_at=new_date,
            amount_with_interest=(total_amount),
            month_paid=float(
                total_amount
                / LoanPlan.objects.get(id=self.request.data["loan_plan"]).duration
            ),
        )