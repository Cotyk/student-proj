# Generated by Django 3.1.3 on 2021-01-11 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_group',
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.group', verbose_name='Група'),
        ),
    ]
