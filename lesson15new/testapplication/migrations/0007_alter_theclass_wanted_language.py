# Generated by Django 5.0.4 on 2024-04-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapplication', '0006_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theclass',
            name='wanted_language',
            field=models.CharField(default='English', max_length=30, verbose_name='foreign languages (by default is English)'),
        ),
    ]
