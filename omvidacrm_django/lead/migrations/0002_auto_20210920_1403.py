# Generated by Django 3.2.7 on 2021-09-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('medium', 'Medium'), ('high', 'High'), ('low', 'Low')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('lost', 'Lost'), ('inprogress', 'In progress'), ('contacted', 'Contacted'), ('won', 'Won'), ('new', 'New')], default='new', max_length=25),
        ),
    ]