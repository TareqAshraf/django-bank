# serializers.py

from rest_framework import serializers
from .models import LoanProvider, LoanCustomer, BankPersonnel, LoanPlan, LoanFund, Loan


class LoanProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProvider
        fields = "__all__"


class LoanCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanCustomer
        fields = "__all__"


class BankPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankPersonnel
        fields = "__all__"


class LoanPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPlan
        fields = "__all__"


class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = "__all__"
        read_only_fields = (
            "loan_provider",
            "amount_with_interest",
        )


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = (
            "loan_customer",
            "amount_with_interest",
            "month_paid",
        )
