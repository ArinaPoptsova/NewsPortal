# Generated by Django 4.1.4 on 2022-12-19 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name_plural': 'PostCategories'},
        ),
    ]
