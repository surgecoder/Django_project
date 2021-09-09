from django.db import models


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100, required=True)


class Product(models.Model):
    title = models.CharField(max_length=100, required=True)
    price = models.DecimalField(max_digits=11, decimal_places=0)
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
