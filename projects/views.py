from django.shortcuts import render
from .models import Product
from .models import UserProfile
from .cart import Cart
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout

# This view will render your homepage (index.html)
def home(request):
    products = Product.objects.all()  
    return render(request, 'index.html', {'products': products})


def product_listing(request):
    products = Product.objects.all()  # Fetch all products from the database
    context = {'products': products}
    return render(request, 'product_listing.html', context)

def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'user_profile.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    messages.success(request, 'Item added to cart successfully!')
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})






