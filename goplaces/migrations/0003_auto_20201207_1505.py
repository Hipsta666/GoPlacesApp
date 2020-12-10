# Generated by Django 3.1.4 on 2020-12-07 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goplaces', '0002_auto_20201207_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnaire_name', models.CharField(default=None, max_length=100, verbose_name='Опросный лист')),
            ],
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ManyToManyField(blank=True, related_name='questions', to='goplaces.Questionnaire', verbose_name='Опросный лист'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goplaces.question'),
        ),
    ]
