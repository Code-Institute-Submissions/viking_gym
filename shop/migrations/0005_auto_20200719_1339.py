# Generated by Django 3.0.8 on 2020-07-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200712_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='master_category',
            field=models.CharField(blank=True, choices=[('AC', 'Accessories'), ('CL', 'Clothing'), ('TR', 'Trainers'), ('SA', 'On sale')], default='CL', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(default='Unisex', max_length=10),
        ),
    ]