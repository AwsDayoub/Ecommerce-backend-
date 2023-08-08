from django.db import models
from users.models import User
# Create your models here.




class Product(models.Model):
    namee = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.namee
    


class Order(models.Model):
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.quantity for item in orderitems])
        return total

    def __str__(self):
        return str(self.id)
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address