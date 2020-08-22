# Generated by Django 3.0.8 on 2020-08-22 08:41

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200821_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_first_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_last_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_phone_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_street_address1',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_town_or_city',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
