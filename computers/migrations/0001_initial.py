# Generated by Django 2.2 on 2021-03-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='computers description')),
                ('reference', models.CharField(max_length=30, verbose_name='reference of computer')),
                ('mark', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=20, verbose_name='operating system')),
                ('category', models.CharField(max_length=30, verbose_name='category of computer')),
                ('assigned_to', models.IntegerField(null=True, verbose_name='is assigned')),
                ('assigned_at', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date of last update')),
            ],
            options={
                'verbose_name': 'Computers',
                'verbose_name_plural': 'Computers',
                'db_table': 'computers',
                'managed': True,
            },
        ),
    ]