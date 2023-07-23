from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LoanProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LoanCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BankPersonnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LoanPlan(models.Model):
    LOAN_TYPE_CHOICES = (
        ('loan_provider', 'Loan Provider'),
        ('loan_customer', 'Loan Customer'),
    )

    # bank_personnel = models.OneToOneField(BankPersonnel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.PositiveIntegerField()
    loan_type = models.CharField(max_length=15, choices=LOAN_TYPE_CHOICES)


class LoanFund(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_plan = models.ForeignKey(
        LoanPlan, on_delete=models.CASCADE)
    loan_provider = models.ForeignKey(
        LoanProvider, on_delete=models.CASCADE)


class Loan(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    month_paid = models.DecimalField(max_digits=10, decimal_places=2)
    loan_plan = models.ForeignKey(
        LoanPlan, on_delete=models.CASCADE)
    loan_customer = models.ForeignKey(
        LoanCustomer, on_delete=models.CASCADE)
