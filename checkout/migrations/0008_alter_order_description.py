# Generated by Django 3.2.25 on 2024-04-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, max_length=254),
        ),
    ]
