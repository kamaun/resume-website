# Generated by Django 2.2.1 on 2019-05-19 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190517_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='workplaces',
            name='extra',
            field=models.BooleanField(default=False),
        ),
    ]
