# Generated by Django 3.1.4 on 2020-12-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goplaces', '0004_auto_20201207_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='answers', to='goplaces.Tag', verbose_name='Теги'),
        ),
    ]
