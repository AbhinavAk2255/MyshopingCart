from django.db import models

# models for products

class product(models.Model):

    LIVE = 1
    DELETE = 0
    
    DELETE_CHOICES = ((LIVE,'Live'),((DELETE,'Delete')))
    
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    genter = models.CharField(max_length=200,default='men')
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class newproducts(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    new_price = models.FloatField()
    old_price = models.FloatField()

    def __str__(self) -> str:
        return self.name
