from django.shortcuts import render, redirect
from AdminApp.models import *
from WebApp.models import *

# Create your views here.
def home_page(request):
    categories = CategoryDb.objects.all()
    return render(request, "Home.html", {'categories':categories})
def about_page(request):
    categories = CategoryDb.objects.all()
    return render(request, "About.html", {'categories':categories})
def all_product(request):
    categories = CategoryDb.objects.all()
    products = ProductDb.objects.all()
    return render(request, "All_Product.html", {'products':products, 'categories':categories})
def contact(request):
    return render(request, "Contact.html")
def filtered_page(request, cat_name):
    categories = CategoryDb.objects.all()
    products = ProductDb.objects.filter(CategoryName=cat_name)
    return render(request, "Filtered_Products.html", {'products':products, 'categories':categories})
def single_product(request, pro_id):
    product = ProductDb.objects.get(id=pro_id)
    return render(request, "Single_Product.html", {'product':product})
def signin_signup(request):
    return render(request, "Signin_Signup.html")
def save_registration(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        p1 = request.POST.get('password')
        p2 = request.POST.get('confirm_password')
        email = request.POST.get('email')
        obj = User_RegistrationDB(User_name=uname, Email=email, Password=p1, Confirm_Password=p2)
        if User_RegistrationDB.objects.filter(User_name=uname).exists():
            # username already exists...!
            return redirect(signin_signup)
        elif User_RegistrationDB.objects.filter(Email=email).exists():
            # Email id already exists...!
            return redirect(signin_signup)
        else:
            obj.save()
            return redirect(signin_signup)


def user_login(request):
    if request.method == "POST":
        uname = request.POST.get('user_name')
        pswd = request.POST.get('password')
        if User_RegistrationDB.objects.filter(User_name=uname, Password=pswd).exists():
            request.session['User_name'] = uname
            request.session['Password'] = pswd
            return redirect(home_page)
        else:
            return redirect(signin_signup)
    else:
        return redirect(signin_signup)
def user_logout(request):
    del request.session['User_name']
    del request.session['Password']
    return redirect(home_page)


def save_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        obj = ContactDB(Name=name, Email=email, MobileNo=mobile, Subject=subject, Message=message)
        obj.save()
        return redirect(contact)
def help(request):
    return render(request, "Help.html")
def support_page(request):
    return render(request, "Support_Page.html")
def cart(request):
    return render(request, "Cart.html")
def checkout(request):
    return render(request, "Checkout.html")




