from django.contrib import admin
from .models import Category , Project , Task
# Register your models here.


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_per_page = 5


@admin.register(Project)
class Projectadmin(admin.ModelAdmin):
    list_per_page = 5



@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_per_page = 5