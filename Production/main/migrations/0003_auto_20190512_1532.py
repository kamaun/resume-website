# Generated by Django 2.2.1 on 2019-05-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190512_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='years',
            field=models.IntegerField(),
        ),
    ]
