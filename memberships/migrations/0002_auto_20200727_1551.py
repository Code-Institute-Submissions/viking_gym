# Generated by Django 3.0.8 on 2020-07-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermembership',
            name='stripe_customer_id',
        ),
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Legend', 'lgn'), ('Pro', 'pro'), ('Basic', 'basic')], default='basic', max_length=30),
        ),
    ]
