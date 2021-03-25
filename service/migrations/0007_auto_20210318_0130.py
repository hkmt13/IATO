# Generated by Django 3.1.5 on 2021-03-17 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20210318_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='big_service',
        ),
        migrations.RemoveField(
            model_name='service',
            name='small_service',
        ),
        migrations.AddField(
            model_name='bigservice',
            name='service_desc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servsbi_type', to='service.service'),
        ),
        migrations.AddField(
            model_name='smallservice',
            name='service_desc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servsma_type', to='service.service'),
        ),
    ]
