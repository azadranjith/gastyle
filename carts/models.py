
from django.db import models
from accounts.models import Account

from store.models import Product,Variation
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length = 100,blank = True,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id  

class CartItem(models.Model):

    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True,blank=True) #when user is deleted cart item also get deleted

    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    variations = models.ManyToManyField(Variation,blank=True)
    
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null = True)

    quantity = models.IntegerField()

    is_active = models.BooleanField(default=True)


    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
