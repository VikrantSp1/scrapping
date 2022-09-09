from django.shortcuts import render
from models import scrapData

# Create your views here.



def datainsert(data):
    if scrapData.object.create(prod_des=data['title'],prod_link=data['link'],prod_rate=data['price']).count()==0:

        scrapData.object.create(prod_des=data['title'],prod_link=data['link'],prod_rate=data['price'])
    





