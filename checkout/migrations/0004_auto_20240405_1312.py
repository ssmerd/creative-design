# Generated by Django 3.2.25 on 2024-04-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20240329_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.TextField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='original_quote',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(blank=True, choices=[('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('X', 'X'), ('YouTube', 'YouTube'), ('Pinterest', 'Pinterest'), ('Snapchat', 'Snapchat'), ('Custom', 'Custom')], max_length=32),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
