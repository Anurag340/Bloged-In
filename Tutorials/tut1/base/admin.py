from django.contrib import admin

# Register your models here.

from .models import Roome , Messages , Topic

admin.site.register(Roome)
admin.site.register(Topic)  
admin.site.register(Messages)