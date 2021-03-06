# Generated by Django 2.2.5 on 2021-05-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_num',
            field=models.IntegerField(verbose_name='Mobile phone number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.IntegerField(verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(verbose_name='Zip code'),
        ),
    ]
