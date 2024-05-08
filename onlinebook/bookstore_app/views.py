from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Profile, CartItem, Cart
from .forms import RegistrationForm, UserProfileForm
from django.contrib import messages
# Create your views here.




def home(request):
    featured_data = Book.objects.filter(featured=True)
    return render(request, 'home.html', {'featured_data': featured_data})


def book(request):
    book_data = Book.objects.order_by('-created_at')
    return render(request, 'books.html', {'book_data':book_data})


def book_detail(request, id):
    detailed_data = get_object_or_404(Book, id=id)
    return render(request, 'detail.html', {'detailed_data':detailed_data})


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful!!')
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def user_login(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('profile')
        else:
            messages.error(request, 'Username or Password Wrong!!')
            return redirect ('login')
    
    return render(request, 'login.html', {'login_form':login_form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def user_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    cart_items = CartItem.objects.all()

    return render(request, 'profile.html', {'profile':profile, 'cart_items':cart_items})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
          form.save()
          messages.success(request, 'Profile Updated!')
          return redirect ('profile')
    else:
        form = UserProfileForm(instance=request.user)

    return redirect ('profile')


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(pk=book_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('profile') 


@login_required
def cart_delete(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)

    if cart_item.cart.user != request.user:
        return redirect('profile')
    
    cart_item.delete()
    messages.success(request, 'Deleted Success!')

    return redirect('profile')