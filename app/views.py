from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import (
    Customer,
    Product,
    Carts,
    OrderPlaces
)

class ProductView(View):
    def get(self, request):
        camera = Product.objects.filter(category='C')
        men = Product.objects.filter(category='M')
        women = Product.objects.filter(category='W')
        sunglasses = Product.objects.filter(category='S')
        shoes = Product.objects.filter(category='Sh')
        context = {
            'camera' : camera,
            'men' : men,
            'women' : women,
            'sunglasses' : sunglasses,
            'shoes' : shoes
        }
        return render(request, 'index.html', context)


class ProductDetails(View):
    def get(Self, request, id):
        product = Product.objects.get(pk=id)
        return render(request, 'productDetails.html', {'product':product})



def shoes(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='Sh')
    elif data == 'campus':
        products = Product.objects.filter(category='Sh').filter(brand = 'Campus')
    elif data == 'nike':
        products = Product.objects.filter(category='Sh').filter(brand = 'Nike')

    elif data == 'below':
        products = Product.objects.filter(category='Sh').filter(discounted_price__lt = 100)

    elif data == 'above':
        products = Product.objects.filter(category='Sh').filter(discounted_price__gt = 49)
    return render(request, 'shoes.html', {'products': products})


def men(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='M')
    elif data == 'balenciaga':
        products = Product.objects.filter(category='M').filter(brand = 'Balenciaga')
    elif data == 'clvinklein':
        products = Product.objects.filter(category='M').filter(brand = 'Clvin Klein')
    elif data == 'adidas':
        products = Product.objects.filter(category='M').filter(brand = 'Adidas')
    elif data == "levi's":
        products = Product.objects.filter(category='M').filter(brand = "levi's")

    elif data == 'below':
        products = Product.objects.filter(category='M').filter(discounted_price__lt = 150)

    elif data == 'above':
        products = Product.objects.filter(category='M').filter(discounted_price__gt = 50)
    return render(request, 'men.html', {'products': products})


def women(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='W')
    elif data == 'biba':
        products = Product.objects.filter(category='W').filter(brand = 'Biba')
    elif data == 'clvinklein':
        products = Product.objects.filter(category='W').filter(brand = 'Clvin Klein')
    elif data == 'zara':
        products = Product.objects.filter(category='W').filter(brand = 'Zara')
    elif data == "levi's":
        products = Product.objects.filter(category='W').filter(brand = "levi's")
    
    elif data == 'below':
        products = Product.objects.filter(category='W').filter(discounted_price__lt = 150)

    elif data == 'above':
        products = Product.objects.filter(category='W').filter(discounted_price__gt = 50)
    return render(request, 'women.html', {'products': products})


def sunglasses(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='S')
    elif data == 'prada':
        products = Product.objects.filter(category='S').filter(brand = 'Prada')
    elif data == 'ran-ban':
        products = Product.objects.filter(category='S').filter(brand = 'Ran-Ban')

    elif data == 'below':
        products = Product.objects.filter(category='S').filter(discounted_price__lt = 100)

    elif data == 'above':
        products = Product.objects.filter(category='S').filter(discounted_price__gt = 49)
    return render(request, 'sunglasses.html', {'products': products})


def camera(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='C')
    elif data == 'canon':
        products = Product.objects.filter(category='C').filter(brand = 'Canon')
    elif data == 'nikon':
        products = Product.objects.filter(category='C').filter(brand = 'Nikon')
    elif data == 'sony':
        products = Product.objects.filter(category='C').filter(brand = 'Sony')

    elif data == 'below':
        products = Product.objects.filter(category='C').filter(discounted_price__lt = 200)

    elif data == 'above':
        products = Product.objects.filter(category='C').filter(discounted_price__gt = 100)
    return render(request, 'camera.html', {'products': products})



def search(request):
    q = request.GET.get('query')
    data = Product.objects.filter(product_name__icontains = q)
    return render(request, 'search.html', {'data':data, 'q':q})



class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registrations.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation! Registered Successfully')
            form.save()
        return render(request, 'registrations.html', {'form': form})



def home(request):
    return render(request, 'index.html')


def addToCart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('pro_id')
        product = Product.objects.get(id = product_id)
        for user in User.objects.all():
            User.objects.get_or_create(username=user)
        Carts(user=request.user, product=product).save()
        return redirect('/')
    else:
        return redirect('login')


def carts(request):
    user = request.user
    cartitems = 0
    if request.user.is_authenticated:
        items = Carts.objects.filter(user = request.user)
        for i in items:
            cartitems = cartitems + 1
    total_price = 0
    for i in items:
        total_price += i.product.discounted_price * i.quantity

    return render(request, 'carts.html', {'items': items, 'cartitems':cartitems})

class ProductDetails(View):
    def get(self, request ,id):
        product = Product.objects.get(pk = id)
        return render(request, 'productDetails.html', {'product':product})




def contact(request):
    return render(request, 'contact.html')

def buynow(request):
    return render(request, 'buynow.html')



def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

def logout(request):
    return render(request, 'logout.html')






