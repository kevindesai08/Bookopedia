# Generated by Django 4.2 on 2023-04-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_bookdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookDescription',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
