from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from shop.models import *

# Register your models here.

# Method- Manually registering all apps

# admin.site.register(Product)
# admin.site.register(Category)

# automatically fetch all the models in all the apps and register them with the admin interface

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except AlreadyRegistered:
#          pass      

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created','available']
    list_filter = ['available','created']
    list_editable = ['available']
    prepopulated_fields = {'slug':['name','category']}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']  
    prepopulated_fields = {'slug':['name']}