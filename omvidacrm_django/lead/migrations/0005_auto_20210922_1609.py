# Generated by Django 3.2.7 on 2021-09-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_auto_20210922_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('contacted', 'Contacted'), ('won', 'Won'), ('new', 'New'), ('lost', 'Lost'), ('inprogress', 'In progress')], default='new', max_length=25),
        ),
    ]
