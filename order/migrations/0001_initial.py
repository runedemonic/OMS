# Generated by Django 4.1.4 on 2023-01-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=200)),
                ('product_code', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('sum', models.IntegerField()),
                ('order_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField(blank=True)),
            ],
        ),
    ]