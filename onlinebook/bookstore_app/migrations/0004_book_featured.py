# Generated by Django 5.0.4 on 2024-05-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0003_book_book_price_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
