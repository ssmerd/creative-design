from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total','order_number', 'date')
    fields = ('name', 'email', 'phone', 'total', 'category', 'description', 'size', 'stripe_pid',)
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)