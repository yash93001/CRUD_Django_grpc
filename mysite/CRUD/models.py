from django.db import models

class user_table(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    mobile_no = models.IntegerField(max_length=10)

