from django.shortcuts import render, redirect
from AdminApp.models import CategoryDb,ProductDb
from django.core.files.storage import  FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from WebApp.models import *

# Create your views here.

def dashboard(request):
    category = CategoryDb.objects.count()
    product = ProductDb.objects.count()
    return render(request, "dashboard.html",
                  {'category':category, 'product':product})
def add_category(request):
    return render(request, "Add_Category.html")
def save_category(request):
    if request.method == "POST":
        category_name = request.POST.get("name")
        Description = request.POST.get("description")
        img = request.FILES['category_image']
        obj = CategoryDb(Category_Name=category_name, Description=Description,Image=img)
        obj.save()
        return redirect(add_category)
def display_category(request):
    data = CategoryDb.objects.all()
    return render(request, "Display_Category.html", {'data':data})

def edit_category(request, category_id):
    data = CategoryDb.objects.get(id=category_id)
    return render(request, "Edit_Category.html", {'data':data})

def delete_category(request,category_id):
    data = CategoryDb.objects.filter(id=category_id)
    data.delete()
    return redirect(display_category)

def update_category(request, category_id):
    if request.method == "POST":
        category_name = request.POST.get("name")
        Description = request.POST.get("description")
        try:
            img = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=category_id).Image
        CategoryDb.objects.filter(id=category_id).update(Category_Name=category_name, Description=Description,
                          Image=file)
        return redirect(display_category)

#********************************************************************************


def add_product(request):
    categories = CategoryDb.objects.all()
    return render(request, "Add_Product.html", {'categories':categories})

def display_product(request):
    data = ProductDb.objects.all()
    return render(request, "Display_product.html", {'data':data})

def save_product(request):
    if request.method == "POST":
        product_category = request.POST.get("product_category")
        product_name = request.POST.get("productname")
        price = request.POST.get("price")
        short_description = request.POST.get("Short_desc")
        detailed_description = request.POST.get("detailed_desc")
        brand = request.POST.get("brand")
        img1 = request.FILES['product_image1']
        img2 = request.FILES['product_image2']
        img3 = request.FILES['product_image3']
        obj = ProductDb(CategoryName=product_category, Product_Name=product_name,price=price,
                        Short_Description=short_description, detailed_Description=detailed_description,
                        Brand=brand, Product_Image1=img1, Product_Image2=img2, Product_Image3=img3)
        obj.save()
        return redirect(add_product)

def update_product(request, product_id):
    if request.method == "POST":
        product_category = request.POST.get("product_category")
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        short_description = request.POST.get("short_description")
        detailed_description = request.POST.get("detailed_description")
        brand = request.POST.get("brand")
        try:
            img = request.FILES['category_image1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=product_id).Product_Image1

        try:
            img = request.FILES['category_image2']
            fs = FileSystemStorage()
            file2 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=product_id).Product_Image2

        try:
            img = request.FILES['category_image3']
            fs = FileSystemStorage()
            file3 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file3 = ProductDb.objects.get(id=product_id).Product_Image3
        ProductDb.objects.filter(id=product_id).update(CategoryName=product_category, Product_Name=product_name,
                          price=price, Short_Description=short_description, detailed_Description=detailed_description,
                          Brand=brand, Product_Image1=file1,Product_Image2=file2, Product_Image3=file3)
        return redirect(display_product)


def edit_product(request, product_id):
    categories = CategoryDb.objects.all()
    data = ProductDb.objects.get(id=product_id)
    return render(request, "Edit_Product.html", {'data':data, 'categories':categories})

def delete_product(request,product_id):
    data = ProductDb.objects.filter(id=product_id)
    data.delete()
    return redirect(display_product)

#*******************************************************************************************

def admin_page(request):
    return render(request, "Admin_Loginpage.html")


def admin_login(request):
    if request.method == "POST":
        u_name = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username__contains=u_name).exists():
            data = authenticate(username=u_name, password=password)
            if data is not None:
                login(request, data)
                request.session['username'] = u_name
                request.session['password'] = password
                return redirect(dashboard)
            else:
                return redirect(admin_page)
        else:
            return redirect(admin_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_page)

def contact_details(request):
    data = ContactDB.objects.all()
    return render(request, "Contact_Details.html", {'data':data})

def delete_contact(request,contact_id):
    data = ContactDB.objects.filter(id=contact_id)
    data.delete()
    return redirect(contact_details)