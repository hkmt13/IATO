# Generated by Django 3.1.5 on 2021-03-17 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_auto_20210318_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='BigService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_name', models.CharField(max_length=255)),
                ('ser_type', models.CharField(max_length=50)),
                ('ser_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateField(blank=True, null=True)),
                ('travel_date', models.DateField(blank=True, null=True)),
                ('arrival_date', models.DateField(blank=True, null=True)),
                ('internal_travel_date', models.DateField(blank=True, null=True)),
                ('internal_arrival_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField(auto_now=True)),
                ('bill_number', models.IntegerField()),
                ('bill_type', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('cusotmer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill_cust', to='service.customer')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organzition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SmallService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_name', models.CharField(max_length=255)),
                ('ser_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceBookDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('big_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serv_bigserv', to='service.bigservice')),
                ('customer_bill_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_bill_Customer', to='service.customerbill')),
                ('small_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serv_smallserv', to='service.smallservice')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_desc', models.CharField(max_length=255, unique=True)),
                ('big_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serv_big', to='service.bigservice')),
                ('small_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serv_small', to='service.smallservice')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('Notification_date', models.DateTimeField(auto_now=True)),
                ('service_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notif_serv', to='service.bookservice')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notif_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='organzition_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cus_org', to='service.organzition'),
        ),
        migrations.AddField(
            model_name='bookservice',
            name='customer_bill_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_bill', to='service.customerbill'),
        ),
        migrations.AddField(
            model_name='bookservice',
            name='organzition_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_org', to='service.organzition'),
        ),
        migrations.AddField(
            model_name='bookservice',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
