# Generated by Django 5.0.4 on 2024-04-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapplication', '0004_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='Edit-Print', max_length=30, verbose_name='printed in/nby default is Edit-Print'),
        ),
    ]
