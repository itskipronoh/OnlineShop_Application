from django.shortcuts import render

from Customers.forms import CustomerForm


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    form = CustomerForm()
    return render(request,'contact.html',{'form':form})

