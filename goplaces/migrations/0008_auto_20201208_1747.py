# Generated by Django 3.1.4 on 2020-12-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goplaces', '0007_auto_20201208_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='poster',
            field=models.ImageField(upload_to='goplaces/img/posters/', verbose_name='Постер'),
        ),
    ]