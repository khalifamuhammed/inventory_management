from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'KenInventory Dashboard'  # this change the name of headher in Admin panel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)



admin.site.register(Product,ProductAdmin)  # Add product catagory in admin panel
admin.site.register(Order)
admin.site.unregister(Group)