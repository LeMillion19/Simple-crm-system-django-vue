# Generated by Django 3.2.7 on 2021-12-15 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210924_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='plan',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
