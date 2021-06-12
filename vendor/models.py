from django.db import models

# Create your models here.

class restuarantInformation(models.Model):

    Email = models.CharField(max_length=200, blank=True)
    Name = models.CharField(max_length=200, primary_key=True)
    Address = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=200, blank=True)
    Zip = models.IntegerField()
    Description = models.CharField(max_length=500, blank=True)
    Event = models.CharField(max_length=100, blank=True)
    FoodType = models.CharField(max_length=100, blank=True)
    PaymentMethod = models.CharField(max_length=100, blank=True)
    Image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.Name



class addDeal(models.Model):

    Name = models.CharField(max_length=200)
    Email = models.ForeignKey('restuarantInformation', db_column='Email', blank=False,null=False, on_delete=models.CASCADE)


    Price = models.IntegerField()
    Description = models.CharField(max_length=500, blank=True)

    Image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.Name


