from django.db import models
from ..products.models import Product
from ..customers.models import Customer


# Create your models here.
class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=False)

    def __str__(self):
        return self.date
