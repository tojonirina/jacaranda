# Generated by Django 2.2 on 2021-06-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0002_auto_20210519_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]
