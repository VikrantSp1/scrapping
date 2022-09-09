from django.contrib import admin
from .models import User,scrapData
# Register your models here.

@admin.register(User,scrapData)

class UserAdmin(admin.ModelAdmin):
    lisr_display=('id','name','email','password')


class scrapAdmin(admin.ModelAdmin):
    lisr_display=('prod_des','prod_link','prod_rate')






