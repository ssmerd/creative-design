# Generated by Django 3.2.25 on 2024-04-06 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_quote',
        ),
    ]
