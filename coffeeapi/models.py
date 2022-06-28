from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID') 
    name = models.CharField(null=True, max_length=60)
    birth_date = models.DateField(null=True)
    gender = models.CharField(null=True, max_length=60)
    email = models.CharField(null=True, max_length=60)
    password = models.CharField(null=True, max_length=60)


    def __str__(self):
        return self.id, self.name, self.birth_date, self.gender, self.email, self.password

class Menu(models.Model): 
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID') 
    menu_name = models.CharField(null=True, max_length=60)
    price = models.CharField(null=True, max_length=60)
    image = models.URLField(null=True, blank=True, max_length=250)
    temperature = models.CharField(null=True, max_length=60)

    def __str__(self):
        return self.id, self.menu_name, self.price, self.image, self.temperature