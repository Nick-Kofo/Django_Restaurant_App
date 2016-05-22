from django.contrib import admin
from .models import Dish  # import Post model so we can register to Admin Administration

# Register your models here.

admin.site.register(Dish)  # register Dish (model)
