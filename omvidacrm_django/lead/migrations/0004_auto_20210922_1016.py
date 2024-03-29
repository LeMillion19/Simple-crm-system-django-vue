# Generated by Django 3.2.7 on 2021-09-22 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0003_auto_20210920_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedleads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('medium', 'Medium'), ('low', 'Low'), ('high', 'High')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('won', 'Won'), ('contacted', 'Contacted'), ('lost', 'Lost'), ('new', 'New'), ('inprogress', 'In progress')], default='new', max_length=25),
        ),
    ]
