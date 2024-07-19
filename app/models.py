from django.db import models

# Create your models here.

# Client model
class Client(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    social_security_number = models.CharField(max_length=11)
    date_of_birth = models.CharField(max_length=100)

    def upload_to_ssn_front(instance, filename):
        return f'{instance.firstname}_{instance.lastname}/ssn_image/front_{filename}'

    def upload_to_ssn_back(instance, filename):
        return f'{instance.firstname}_{instance.lastname}/ssn_image/back_{filename}'

    def upload_to_driver_license_front(instance, filename):
        return f'{instance.firstname}_{instance.lastname}/driver_license_image/front_{filename}'

    def upload_to_driver_license_back(instance, filename):
        return f'{instance.firstname}_{instance.lastname}/driver_license_image/back_{filename}'

    def upload_to_passport(instance, filename):
        return f'{instance.firstname}_{instance.lastname}/passport_image/{filename}'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    image_ssn_front = models.ImageField(upload_to=upload_to_ssn_front)
    image_ssn_back = models.ImageField(upload_to=upload_to_ssn_back)
    image_driver_license_front = models.ImageField(upload_to=upload_to_driver_license_front)
    image_driver_license_back = models.ImageField(upload_to_driver_license_back)
    image_passport = models.ImageField(upload_to=upload_to_passport, blank=True, null=True)  # Allow blank and null for optional field


# ContactDetails model
class ContactDetails(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='contact_details')
    email_address = models.EmailField(max_length=254)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.client.firstname} {self.client.lastname} - {self.email_address}'


# BusinessInfo model
class BusinessInfo(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='business_info')
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    years_in_business = models.PositiveIntegerField()
    annual_revenue = models.DecimalField(max_digits=100, decimal_places=4)

    def __str__(self):
        return self.business_name


# LoanDetails model
class LoanDetails(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='loan_details')
    loan_amount = models.DecimalField(max_digits=100, decimal_places=4)
    purpose_of_loan = models.TextField()

    def __str__(self):
        return f'Loan for {self.client.firstname} {self.client.lastname}'


# BankCard model
class BankCard(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='bank_card')
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=19)
    cvv = models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=5)  # Format: MM/YY

    def __str__(self):
        return f'Card ending in {self.card_number[-4:]} for {self.client.firstname} {self.client.lastname}'
