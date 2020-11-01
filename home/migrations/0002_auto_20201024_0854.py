# Generated by Django 3.1.2 on 2020-10-24 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_no', models.IntegerField(default=0, unique=True, verbose_name='Table number')),
                ('seat', models.IntegerField(default=4, verbose_name='Number of seats')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('0', 'Cash'), ('1', 'Card'), ('2', 'UPI')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.table'),
        ),
    ]