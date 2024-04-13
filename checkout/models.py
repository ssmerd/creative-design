import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from profiles.models import UserProfile

DESIGN_SIZES  = [
        ("Instagram", "Instagram"),
        ("Facebook", "Facebook"),
        ("X", "X"),
        ("YouTube", "YouTube"),
        ("Pinterest", "Pinterest"),
        ("Snapchat", "Snapchat"),
        ("Custom", "Custom"),
    ]

class Order(models.Model):
   
    order_number = models.CharField(max_length=32, null=False, editable=False)
    category = models.TextField(max_length=254, null=False, blank=True)
    description = models.TextField(max_length=254, null=False, blank=True)
    size = models.CharField(max_length=32, null=False, blank=True, choices=DESIGN_SIZES)
    name  = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    date  = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    
    # original_quote = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
