from django.contrib import admin
from .models import Client, ContactDetails, BusinessInfo, LoanDetails, BankCard

admin.site.register(Client)
admin.site.register(ContactDetails)
admin.site.register(BusinessInfo)
admin.site.register(LoanDetails)
admin.site.register(BankCard)
