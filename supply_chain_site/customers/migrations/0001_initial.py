# Generated by Django 4.2.4 on 2023-08-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=2500)),
                ('street_name', models.CharField(max_length=1500)),
                ('city', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=2500)),
                ('contact_person', models.CharField(max_length=1500)),
                ('contact_person_phone', models.CharField(max_length=20)),
                ('contact_person_email', models.CharField(max_length=2500)),
            ],
        ),
    ]
