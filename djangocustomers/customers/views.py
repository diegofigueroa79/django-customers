from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.
def index(request):
    # list all customers
    if request.method == 'GET':
        customers = Customer.objects.all()
        context = {
            'customers': customers,
        }
        return render(request, "customers/index.html", context)

    # delete customer
    if request.method == 'POST':
        customerID = request.POST['customerID']
        try:
            customer = Customer.objects.get(pk=customerID)
            customer.delete()
        except:
            pass
        return redirect("/")

def register(request):
    if request.method == 'GET':
        context = {
            'states': Customer.STATE_CHOICES,
        }
        return render( request, "customers/register.html", context)
    
    if request.method == 'POST':
        try:
            customer = Customer(
                first_name = request.POST['fname'],
                last_name = request.POST['lname'],
                address = request.POST['address'],
                city = request.POST['city'],
                zip_code = request.POST['zipcode'],
                state = request.POST['state']
            )
            customer.save()
        except:
            pass
        return redirect("/")