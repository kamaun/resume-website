# Generated by Django 2.2.1 on 2019-05-14 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_techused_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(default='Project Description', max_length=600),
        ),
        migrations.AlterField(
            model_name='techused',
            name='purpose',
            field=models.TextField(default='Technology use', max_length=200),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=600)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Projects')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.School')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.WorkPlaces')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
