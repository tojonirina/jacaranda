# Generated by Django 2.2 on 2021-05-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='state',
            field=models.CharField(choices=[('new', 'Nouveau'), ('old', 'Ancien')], max_length=20),
        ),
    ]
