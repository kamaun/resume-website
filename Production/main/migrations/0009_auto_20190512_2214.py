# Generated by Django 2.2.1 on 2019-05-13 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190512_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.URLField(blank=True, max_length=128, verbose_name='Web Link'),
        ),
        migrations.AddField(
            model_name='workplaces',
            name='link',
            field=models.URLField(blank=True, max_length=128, verbose_name='Web Link'),
        ),
    ]
