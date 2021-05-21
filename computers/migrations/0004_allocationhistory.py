# Generated by Django 2.2 on 2021-05-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0003_auto_20210520_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('assigned_to', models.CharField(max_length=50, verbose_name='is assigned')),
                ('assigned_by', models.CharField(max_length=50)),
                ('note', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'allocation_history',
            },
        ),
    ]