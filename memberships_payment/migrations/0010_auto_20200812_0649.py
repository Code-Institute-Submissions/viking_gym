# Generated by Django 3.0.8 on 2020-08-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships_payment', '0009_auto_20200812_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]