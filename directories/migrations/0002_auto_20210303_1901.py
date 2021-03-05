# Generated by Django 2.2 on 2021-03-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directories',
            name='function',
            field=models.CharField(default='DAF', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='directories',
            name='avatar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='directories',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]