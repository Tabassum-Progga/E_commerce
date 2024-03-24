from django.contrib import admin
from .models import Rating,Product,Order

# Register your models here.
admin.site.register([Rating,Product,Order])

