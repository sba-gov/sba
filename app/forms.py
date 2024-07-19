from django import forms
from .models import Client, ContactDetails, BusinessInfo, LoanDetails, BankCard

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'social_security_number', 'date_of_birth', 'image_ssn_front', 'image_ssn_back', 'image_driver_license_front', 'image_driver_license_back','image_passport']

class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['email_address', 'address', 'phone']

class BusinessInfoForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo
        fields = ['business_name', 'business_type', 'years_in_business', 'annual_revenue']

class LoanDetailsForm(forms.ModelForm):
    class Meta:
        model = LoanDetails
        fields = ['loan_amount', 'purpose_of_loan']

class BankCardForm(forms.ModelForm):
    class Meta:
        model = BankCard
        fields = ['cardholder_name', 'card_number', 'cvv', 'expiry_date']
