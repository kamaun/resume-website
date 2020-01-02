# Generated by Django 3.0.1 on 2019-12-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bitbucket',
            field=models.URLField(default='https://bitbucket.org/knjeri', verbose_name='Bitbucket'),
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(default='https://github.com/kamaun', verbose_name='Git Hub'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(default='https://www.linkedin.com/in/kelvinnjeri/', verbose_name='LinkedIn'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location_city',
            field=models.CharField(default='Deerfield Beach', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='location_state',
            field=models.CharField(default='Florida', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='Software Engineer', max_length=20),
        ),
    ]
