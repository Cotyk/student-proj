# Generated by Django 3.1.3 on 2021-01-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_monthjournal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120, verbose_name='Назва дисципліни')),
                ('datetime', models.DateTimeField(verbose_name='Дата/час проведення')),
                ('teacher', models.CharField(max_length=150, verbose_name='Викладач')),
                ('exam_group', models.ManyToManyField(to='students.Group', verbose_name='Група')),
            ],
            options={
                'verbose_name': 'Екзамен',
                'verbose_name_plural': 'Екзамени',
            },
        ),
    ]
