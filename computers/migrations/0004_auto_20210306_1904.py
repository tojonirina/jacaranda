# Generated by Django 2.2 on 2021-03-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0003_computers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='assigned_to',
            field=models.CharField(max_length=50, null=True, verbose_name='is assigned'),
        ),
    ]