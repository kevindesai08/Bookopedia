# Generated by Django 4.2 on 2023-04-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_bookqty_book_bookquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
