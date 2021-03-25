# Generated by Django 3.1.5 on 2021-03-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20210319_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicebookdetails',
            name='price',
        ),
        migrations.AddField(
            model_name='bigservice',
            name='Condition',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bigservice',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='smallservice',
            name='Condition',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='smallservice',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]