# Generated by Django 2.2 on 2021-05-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('login', models.CharField(max_length=50)),
                ('logged', models.BooleanField(default=True)),
                ('user_agent', models.CharField(max_length=100)),
                ('computer_user', models.CharField(max_length=50)),
                ('computer_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'session_history',
            },
        ),
    ]
