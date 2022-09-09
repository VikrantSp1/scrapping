from django.db import models

class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class scrapData(models.Model):
    prod_des=models.CharField(max_length=70)
    prod_link=models.URLField(max_length = 200)   
    prod_rate=models.IntegerField(max_length=20)
