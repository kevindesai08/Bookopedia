# Generated by Django 4.2 on 2023-04-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookDescription',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
