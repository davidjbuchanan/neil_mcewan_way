# Generated by Django 3.0.8 on 2020-08-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
