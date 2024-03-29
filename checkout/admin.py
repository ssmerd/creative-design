from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)
    fields = ('order_number', 'name', 'email', 'phone', 'date', 'total',)
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)