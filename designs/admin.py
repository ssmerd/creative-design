from django.contrib import admin
from .models import Category, Design

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class DesignAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'image',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Design, DesignAdmin)