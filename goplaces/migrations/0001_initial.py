# Generated by Django 3.1.4 on 2020-12-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('address', models.CharField(max_length=255, verbose_name='Адресс')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('description', models.TextField(verbose_name='Описание')),
                ('average_check', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Средний чек')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер')),
                ('tags', models.ManyToManyField(blank=True, related_name='places', to='goplaces.Tag', verbose_name='Теги')),
            ],
        ),
    ]