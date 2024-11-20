from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient

from Customers.forms import CustomerForm


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = CustomerForm()
    return render(request,'contact.html',{'form':form})


    pass


def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0768008874'
    amount = 1
    reference = '0718043149'
    transaction_desc = 'test'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = client.stk_push(phone_number, amount, reference, transaction_desc, callback_url)
    return HttpResponse(response)
