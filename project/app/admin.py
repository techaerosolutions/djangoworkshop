from django.contrib import admin
from .models import Product
from .models import Manager


# Register your models here.
admin.site.register(Manager)
admin.site.register(Product)
