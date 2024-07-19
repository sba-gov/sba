from django.shortcuts import render, redirect
from .forms import ClientForm, ContactDetailsForm, BusinessInfoForm, LoanDetailsForm, BankCardForm
from .models import Client

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def success(request):
    return render(request, 'app/success.html')

def apply(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST, request.FILES)
        contact_details_form = ContactDetailsForm(request.POST)
        business_info_form = BusinessInfoForm(request.POST)
        loan_details_form = LoanDetailsForm(request.POST)
        bank_card_form = BankCardForm(request.POST)

        print("Client Form Valid:", client_form.is_valid())
        print("Contact Details Form Valid:", contact_details_form.is_valid())
        print("Business Info Form Valid:", business_info_form.is_valid())
        print("Loan Details Form Valid:", loan_details_form.is_valid())
        print("Bank Card Form Valid:", bank_card_form.is_valid())

        if client_form.is_valid() and contact_details_form.is_valid() and business_info_form.is_valid() and loan_details_form.is_valid() and bank_card_form.is_valid():
            client = client_form.save()
            contact_details = contact_details_form.save(commit=False)
            contact_details.client = client
            contact_details.save()
            business_info = business_info_form.save(commit=False)
            business_info.client = client
            business_info.save()
            loan_details = loan_details_form.save(commit=False)
            loan_details.client = client
            loan_details.save()
            bank_card = bank_card_form.save(commit=False)
            bank_card.client = client
            bank_card.save()

            return redirect('app:success')
        else:
            print("Errors:", client_form.errors, contact_details_form.errors, business_info_form.errors, loan_details_form.errors, bank_card_form.errors)
    else:
        client_form = ClientForm()
        contact_details_form = ContactDetailsForm()
        business_info_form = BusinessInfoForm()
        loan_details_form = LoanDetailsForm()
        bank_card_form = BankCardForm()

    return render(request, 'app/apply.html', {
        'client_form': client_form,
        'contact_details_form': contact_details_form,
        'business_info_form': business_info_form,
        'loan_details_form': loan_details_form,
        'bank_card_form': bank_card_form,
    })


def signin(request):
    return render(request, 'app/signin.html')


def clientdetails(request):
    clients = Client.objects.all()
    return render(request, 'app/pro.html', {'clients': clients})