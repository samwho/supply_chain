# Generated by Django 4.2.4 on 2023-08-24 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_rename_customer_name_customer_name'),
        ('products', '0001_initial'),
        ('invoices', '0002_rename_product_row_invoice_product_rows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='productrow',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invoices.invoice'),
        ),
        migrations.AlterField(
            model_name='productrow',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
    ]
