from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


# customer
class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.first_name} {self.lastname}'

class Product(models.Model):
    name = models.CharField(max_length = 30)
    price= models.DecimalField(default=0, decimal_places=2, max_digits= 8)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length= 250, default = "", blank= True, null= True)
    image = models.ImageField(upload_to = 'uploads/products')


    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ForeignKey(Product,on_delete = models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length= 100, default= '', blank = True)
    phone = models.CharField(max_length = 15, default = '', blank = True)
    datetime =models.DateField(default = datetime.datetime.today)
    status  = models.BooleanField(default= False)

    def __str__(self):
        return self.product