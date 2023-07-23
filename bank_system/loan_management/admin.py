from django.contrib import admin
from .models import LoanProvider, LoanCustomer, BankPersonnel, LoanPlan, LoanFund, Loan


admin.site.register(LoanProvider)
admin.site.register(LoanCustomer)
admin.site.register(BankPersonnel)
admin.site.register(LoanPlan)
admin.site.register(LoanFund)
admin.site.register(Loan)
