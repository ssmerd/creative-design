from django.db import models
from designs.models import Category


class Quote(models.Model):

    DESIGN_SIZES  = [
        ("Instagram", "Instagram"),
        ("Facebook", "Facebook"),
        ("X", "X"),
        ("YouTube", "YouTube"),
        ("Pinterest", "Pinterest"),
        ("Snapchat", "Snapchat"),
        ("Custom", "Custom"),
    ]
    
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)   
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    size = models.CharField(max_length=32, choices=DESIGN_SIZES)


    # def __str__(self):
    #     return self.name
