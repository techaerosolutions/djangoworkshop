from django.shortcuts import render
from .models import Product
from .form import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def detail(request):
    product = Product.objects.all()
    return render(request, "detail.html", {'product':product})

def addproduct(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addproduct?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "addproduct.html", {'form':form, 'submitted': submitted})