from django.contrib import admin

# Register your models here.

# Register your models here.
from serviceApp.models import User , Category, Service

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Service)
