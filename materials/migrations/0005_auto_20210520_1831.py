# Generated by Django 2.2 on 2021-05-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_auto_20210520_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouvmenthistory',
            name='state',
            field=models.CharField(choices=[('new', 'Nouveau'), ('occasion', 'Occasion'), ('hs', 'Hors service')], max_length=10),
        ),
    ]
