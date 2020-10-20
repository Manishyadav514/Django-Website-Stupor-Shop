from django.db import models

# Create your models here.
class super(models.Model):
    name = models.CharField(max_length=100)
    desc = models.IntegerField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    delete = models.IntegerField()
    img=  models.ImageField(upload_to='pics')
