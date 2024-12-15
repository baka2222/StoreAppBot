from django.contrib import admin
from .models import Clothes, Category
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Clothes)