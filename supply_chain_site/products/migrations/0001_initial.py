# Generated by Django 4.2.4 on 2023-08-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('product_description', models.CharField(max_length=2500)),
                ('price', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
        ),
    ]
