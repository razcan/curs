from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=15)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)



    def __str__(self):
            return self.name

class Item(models.Model):
    supplier = models.ForeignKey(Supplier, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank =True, null = True)
    code = models.CharField(max_length=15)
    category = models.CharField(max_length=50)
    image = models.ImageField(blank =True, null = True)
    price = models.FloatField()    
    
    
    def __str__(self):
            return self.name