# Generated by Django 2.2 on 2021-05-19 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directory',
            options={'ordering': ['-created_at']},
        ),
    ]