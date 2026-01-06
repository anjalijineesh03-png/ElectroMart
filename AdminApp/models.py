from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="category_image", null=True, blank=True)

class ProductDb(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    Short_Description = models.TextField(null=True, blank=True)
    detailed_Description = models.TextField(null=True, blank=True)
    Brand = models.CharField(max_length=100, null=True, blank=True)
    Product_Image1 = models.ImageField(upload_to="Product Image", null=True, blank=True)
    Product_Image2 = models.ImageField(upload_to="Product Image", null=True, blank=True)
    Product_Image3 = models.ImageField(upload_to="Product Image", null=True, blank=True)

